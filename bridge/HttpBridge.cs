using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Text;
using System.Text.Json;
using System.Threading;

namespace SE2McpBridge
{
    /// <summary>
    /// Minimal HTTP server running inside the editor process.
    ///
    /// HttpListener is used rather than a web framework because it is part of
    /// the runtime: the plugin ships as a single DLL with no dependency that
    /// could clash with the ones the editor already loaded.
    ///
    /// Bound to 127.0.0.1 only. This endpoint executes arbitrary code in the
    /// editor process, so it must never be reachable from another machine.
    /// </summary>
    internal sealed class HttpBridge : IDisposable
    {
        private const int DefaultPort = 8765;

        private readonly HttpListener _listener = new HttpListener();
        private Thread _thread;
        private volatile bool _running;
        private readonly byte[] _token;
        private readonly int _port;

        public string Prefix { get; private set; }
        public string TokenPath { get; private set; }

        public HttpBridge()
        {
            var configured = Environment.GetEnvironmentVariable("SE2_MCP_BRIDGE_PORT");
            _port = int.TryParse(configured, out var p) ? p : DefaultPort;
            Prefix = "http://127.0.0.1:" + _port + "/";
            _listener.Prefixes.Add(Prefix);

            _token = Encoding.ASCII.GetBytes(NewToken());
        }

        /// <summary>
        /// A fresh bearer token for this editor run.
        ///
        /// Binding to 127.0.0.1 is not on its own a protection: a web page the
        /// user happens to be viewing can POST to localhost, and a body sent as
        /// text/plain is a "simple request" that skips the CORS preflight
        /// entirely. Since this endpoint compiles and runs arbitrary C# inside
        /// the editor, an unauthenticated listener is a real hole rather than a
        /// missing feature — so every state-changing call has to carry a secret
        /// that a cross-origin page cannot know.
        /// </summary>
        private static string NewToken()
        {
            var bytes = new byte[32];
            using (var rng = System.Security.Cryptography.RandomNumberGenerator.Create())
            {
                rng.GetBytes(bytes);
            }
            return Convert.ToBase64String(bytes).TrimEnd('=').Replace('+', '-').Replace('/', '_');
        }

        /// <summary>
        /// Hand the token to the MCP server through the file system.
        ///
        /// The two processes share no other channel, and the client is started
        /// independently of the editor, so a file in the server's own cache
        /// directory is the only handover that needs no coordination. It lands
        /// where the Python side already looks: SE2_MCP_CACHE, or
        /// %LOCALAPPDATA%/se2-mcp.
        /// </summary>
        private string WriteToken()
        {
            var dir = Environment.GetEnvironmentVariable("SE2_MCP_CACHE");
            if (string.IsNullOrEmpty(dir))
            {
                dir = Path.Combine(
                    Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                    "se2-mcp");
            }
            Directory.CreateDirectory(dir);
            var path = Path.Combine(dir, "bridge-token.txt");
            File.WriteAllText(path, _port + "\n" + Encoding.ASCII.GetString(_token) + "\n");
            return path;
        }

        /// <summary>Length-independent comparison, so timing reveals nothing.</summary>
        private bool TokenMatches(string presented)
        {
            if (string.IsNullOrEmpty(presented)) return false;
            var given = Encoding.ASCII.GetBytes(presented);
            int diff = given.Length ^ _token.Length;
            for (int i = 0; i < given.Length; i++)
            {
                diff |= given[i] ^ _token[i % _token.Length];
            }
            return diff == 0;
        }

        /// <summary>
        /// Reject a Host header that is not our own loopback address.
        ///
        /// Without this, a hostile page can point a name it controls at
        /// 127.0.0.1 (DNS rebinding) and reach the listener as a same-origin
        /// request, which sidesteps the browser checks entirely.
        /// </summary>
        private bool HostIsLoopback(string host)
        {
            if (string.IsNullOrEmpty(host)) return false;
            var colon = host.LastIndexOf(':');
            var name = colon > 0 ? host.Substring(0, colon) : host;
            var port = colon > 0 ? host.Substring(colon + 1) : "80";
            if (port != _port.ToString()) return false;
            return name == "127.0.0.1" || name == "localhost" || name == "[::1]";
        }

        public void Start()
        {
            // Bind first, publish the token second. A second editor instance
            // cannot take the port, so it must not be allowed to overwrite the
            // token of the instance that did — that would leave the working
            // bridge unreachable with a 401 and no obvious cause.
            _listener.Start();
            TokenPath = WriteToken();
            _running = true;
            _thread = new Thread(Loop) { IsBackground = true, Name = "SE2McpBridge" };
            _thread.Start();
        }

        private void Loop()
        {
            while (_running)
            {
                HttpListenerContext ctx;
                try { ctx = _listener.GetContext(); }
                catch (Exception) { return; }   // listener stopped

                // Each request gets its own thread. Handling them in this loop
                // would serialise everything behind the longest one — and the
                // longest one is always /eval, which is exactly when a caller
                // most needs /state and /ping to answer and say what is stuck.
                ThreadPool.QueueUserWorkItem(_ =>
                {
                    try { Handle(ctx); }
                    catch (Exception ex)
                    {
                        try { WriteJson(ctx, 500, new Dictionary<string, object> { ["error"] = ex.ToString() }); }
                        catch (Exception) { /* client vanished */ }
                    }
                });
            }
        }

        private void Handle(HttpListenerContext ctx)
        {
            var path = ctx.Request.Url?.AbsolutePath?.TrimEnd('/');
            if (string.IsNullOrEmpty(path)) path = "/";
            var query = ctx.Request.QueryString;

            if (!HostIsLoopback(ctx.Request.Headers["Host"]))
            {
                WriteJson(ctx, 403, new Dictionary<string, object>
                {
                    ["error"] = "Host header is not this bridge's loopback address.",
                });
                return;
            }

            var isPing = path == "/" || path == "/ping";
            if (!isPing)
            {
                var header = ctx.Request.Headers["Authorization"] ?? string.Empty;
                var presented = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
                    ? header.Substring(7).Trim()
                    : null;
                if (!TokenMatches(presented))
                {
                    WriteJson(ctx, 401, new Dictionary<string, object>
                    {
                        ["error"] = "Missing or wrong bearer token.",
                        ["token_file"] = TokenPath,
                        ["hint"] = "The MCP server reads the token from that file. "
                                 + "If the editor was restarted, the token changed.",
                    });
                    return;
                }

                // A cross-origin POST only escapes the CORS preflight while its
                // content type stays "simple", so requiring application/json is
                // a second, independent lock on the same door.
                if (string.Equals(ctx.Request.HttpMethod, "POST", StringComparison.OrdinalIgnoreCase))
                {
                    var ct = ctx.Request.ContentType ?? string.Empty;
                    if (ct.IndexOf("application/json", StringComparison.OrdinalIgnoreCase) < 0)
                    {
                        WriteJson(ctx, 415, new Dictionary<string, object>
                        {
                            ["error"] = "POST requires Content-Type: application/json.",
                        });
                        return;
                    }
                }
            }

            switch (path)
            {
                case "/":
                case "/ping":
                    // Deliberately thin: this is the one route without a token,
                    // so that a client with a stale token can still tell "editor
                    // not running" from "token no longer matches".
                    WriteJson(ctx, 200, new Dictionary<string, object>
                    {
                        ["ok"] = true,
                        ["bridge"] = "SE2McpBridge",
                        ["version"] = typeof(HttpBridge).Assembly.GetName().Version?.ToString(),
                        ["process_id"] = Environment.ProcessId,
                        ["latest_event_id"] = EventLog.LatestId,
                        ["auth"] = "bearer",
                        ["token_file"] = TokenPath,
                    });
                    return;

                case "/state":
                    WriteJson(ctx, 200, EditorApi.State());
                    return;

                case "/events":
                {
                    long since = ParseLong(query["since"], 0);
                    int limit = (int)ParseLong(query["limit"], 100);
                    var events = EventLog.Since(since, limit);
                    WriteJson(ctx, 200, new Dictionary<string, object>
                    {
                        ["latest_event_id"] = EventLog.LatestId,
                        ["count"] = events.Count,
                        ["events"] = events,
                    });
                    return;
                }

                case "/service":
                {
                    var name = query["type"] ?? string.Empty;
                    var svc = EditorApi.GetService(name);
                    WriteJson(ctx, 200, new Dictionary<string, object>
                    {
                        ["type"] = name,
                        ["found"] = svc != null,
                        ["value"] = EditorApi.Describe(svc),
                        ["runtime_type"] = svc?.GetType().FullName,
                    });
                    return;
                }

                case "/screenshot":
                {
                    var png = EditorApi.Screenshot();
                    ctx.Response.StatusCode = 200;
                    ctx.Response.ContentType = "image/png";
                    ctx.Response.ContentLength64 = png.Length;
                    ctx.Response.OutputStream.Write(png, 0, png.Length);
                    ctx.Response.OutputStream.Close();
                    return;
                }

                case "/eval":
                {
                    if (!string.Equals(ctx.Request.HttpMethod, "POST", StringComparison.OrdinalIgnoreCase))
                    {
                        WriteJson(ctx, 405, new Dictionary<string, object> { ["error"] = "POST required" });
                        return;
                    }
                    string body;
                    using (var reader = new StreamReader(ctx.Request.InputStream, Encoding.UTF8))
                    {
                        body = reader.ReadToEnd();
                    }

                    string code = null;
                    bool onUiThread = true;
                    int timeoutMs = 30000;
                    try
                    {
                        using var doc = JsonDocument.Parse(body);
                        var root = doc.RootElement;
                        if (root.TryGetProperty("code", out var c)) code = c.GetString();
                        if (root.TryGetProperty("ui_thread", out var u)) onUiThread = u.GetBoolean();
                        if (root.TryGetProperty("timeout_ms", out var t)) timeoutMs = t.GetInt32();
                    }
                    catch (JsonException ex)
                    {
                        WriteJson(ctx, 400, new Dictionary<string, object> { ["error"] = "Bad JSON: " + ex.Message });
                        return;
                    }

                    EventLog.Add("eval", Shorten(code));
                    try
                    {
                        var result = EditorApi.Eval(code, onUiThread, timeoutMs);
                        WriteJson(ctx, 200, new Dictionary<string, object>
                        {
                            ["ok"] = true,
                            ["result"] = result?.ToString(),
                            ["result_type"] = result?.GetType().FullName,
                        });
                    }
                    catch (Exception ex)
                    {
                        // Script errors are an expected outcome, not a bridge
                        // failure: report them as data so the caller can fix
                        // the code and retry.
                        var inner = ex is AggregateException agg && agg.InnerException != null
                            ? agg.InnerException : ex;
                        EventLog.Add("eval-error", inner.Message);
                        WriteJson(ctx, 200, new Dictionary<string, object>
                        {
                            ["ok"] = false,
                            ["error"] = inner.Message,
                            ["error_type"] = inner.GetType().Name,
                        });
                    }
                    return;
                }

                case "/eval/reset":
                    EditorApi.ResetScriptState();
                    WriteJson(ctx, 200, new Dictionary<string, object> { ["ok"] = true });
                    return;

                default:
                    WriteJson(ctx, 404, new Dictionary<string, object>
                    {
                        ["error"] = "Unknown path: " + path,
                        ["paths"] = new[] { "/ping", "/state", "/events", "/service", "/screenshot", "/eval", "/eval/reset" },
                    });
                    return;
            }
        }

        private static string Shorten(string s)
        {
            if (string.IsNullOrEmpty(s)) return string.Empty;
            s = s.Replace("\r", " ").Replace("\n", " ");
            return s.Length <= 120 ? s : s.Substring(0, 120) + " …";
        }

        private static long ParseLong(string s, long fallback)
        {
            return long.TryParse(s, out var v) ? v : fallback;
        }

        private static void WriteJson(HttpListenerContext ctx, int status, object payload)
        {
            var json = JsonSerializer.SerializeToUtf8Bytes(payload,
                new JsonSerializerOptions { WriteIndented = false });
            ctx.Response.StatusCode = status;
            ctx.Response.ContentType = "application/json; charset=utf-8";
            ctx.Response.ContentLength64 = json.Length;
            ctx.Response.OutputStream.Write(json, 0, json.Length);
            ctx.Response.OutputStream.Close();
        }

        public void Dispose()
        {
            _running = false;
            try { _listener.Stop(); } catch (Exception) { }
            try { _listener.Close(); } catch (Exception) { }
        }
    }
}
