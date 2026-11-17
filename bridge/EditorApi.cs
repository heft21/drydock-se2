using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Threading;
using Microsoft.CodeAnalysis.CSharp.Scripting;
using Microsoft.CodeAnalysis.Scripting;

namespace SE2McpBridge
{
    /// <summary>
    /// Everything the bridge can do to the running editor.
    ///
    /// The editor's own service interfaces (ISelectionService, IProjectsService,
    /// ...) are declared `internal`, so they cannot be named from this assembly.
    /// Reflection over the live objects is the only route, which is also why
    /// <see cref="Eval"/> matters: it lets the caller write whatever reflection
    /// the moment requires instead of waiting for a typed wrapper.
    /// </summary>
    public static class EditorApi
    {
        private static readonly List<IDisposable> Subscriptions = new List<IDisposable>();
        private static ScriptState<object> _scriptState;
        private static readonly object ScriptLock = new object();

        // ---------------------------------------------------------------
        // Type and service lookup
        // ---------------------------------------------------------------

        public static Type FindType(string fullName)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                Type t;
                try { t = asm.GetType(fullName, false); }
                catch (Exception) { continue; }
                if (t != null) return t;
            }
            // Fall back to a suffix match so callers can pass a short name.
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                Type[] types;
                try { types = asm.GetTypes(); }
                catch (ReflectionTypeLoadException ex) { types = ex.Types.Where(x => x != null).ToArray(); }
                catch (Exception) { continue; }
                var hit = types.FirstOrDefault(x =>
                    x.FullName != null &&
                    (x.FullName.EndsWith("." + fullName, StringComparison.Ordinal) ||
                     x.Name == fullName));
                if (hit != null) return hit;
            }
            return null;
        }

        /// <summary>
        /// Resolve one of the editor's registered services by type name.
        /// Goes through Avalonia's locator directly, because VRageAvaloniaLocator's
        /// generic accessor cannot be called for an internal interface.
        /// </summary>
        public static object GetService(string typeName)
        {
            var t = FindType(typeName);
            if (t == null) return null;
            return AvaloniaLocator.Current?.GetService(t);
        }

        // ---------------------------------------------------------------
        // Live watching
        // ---------------------------------------------------------------

        /// <summary>
        /// Subscribe to the editor's selection observables so that opening or
        /// inspecting an asset shows up in the event stream.
        /// </summary>
        public static void OnProjectLoaded()
        {
            TryDescribeProject();
            TrySubscribeSelection();
        }

        private static void TryDescribeProject()
        {
            try
            {
                var svc = GetService("Keen.VRage.Editor.Services.Project.IProjectsService");
                if (svc == null) { EventLog.Add("project", "IProjectsService not registered"); return; }
                var current = svc.GetType().GetProperty("Current")?.GetValue(svc);
                EventLog.Add("project", "Loaded project: " + Describe(current));
            }
            catch (Exception ex) { EventLog.Add("error", "TryDescribeProject: " + ex.Message); }
        }

        private static void TrySubscribeSelection()
        {
            try
            {
                var svc = GetService("Keen.VRage.Editor.Services.Selection.ISelectionService");
                if (svc == null) { EventLog.Add("selection", "ISelectionService not registered"); return; }

                foreach (var name in new[] { "SelectedChanged", "OpenedChanged", "InspectedChanged" })
                {
                    var prop = svc.GetType().GetProperty(name);
                    var observable = prop?.GetValue(svc);
                    if (observable == null) continue;
                    var sub = SubscribeObservable(observable, name);
                    if (sub != null) Subscriptions.Add(sub);
                }
                EventLog.Add("selection", "Subscribed to " + Subscriptions.Count + " selection observable(s)");
            }
            catch (Exception ex) { EventLog.Add("error", "TrySubscribeSelection: " + ex.Message); }
        }

        /// <summary>
        /// IObservable&lt;T&gt;.Subscribe needs an IObserver&lt;T&gt;; building one for a
        /// type only known at run time means a small dynamic proxy.
        /// </summary>
        private static IDisposable SubscribeObservable(object observable, string label)
        {
            var iface = observable.GetType().GetInterfaces()
                .FirstOrDefault(i => i.IsGenericType &&
                                     i.GetGenericTypeDefinition() == typeof(IObservable<>));
            if (iface == null) return null;
            var itemType = iface.GetGenericArguments()[0];

            var observerType = typeof(RelayObserver<>).MakeGenericType(itemType);
            var observer = Activator.CreateInstance(observerType, new object[] { label });
            return (IDisposable)iface.GetMethod("Subscribe").Invoke(observable, new[] { observer });
        }

        private sealed class RelayObserver<T> : IObserver<T>
        {
            private readonly string _label;
            public RelayObserver(string label) { _label = label; }
            public void OnCompleted() { EventLog.Add(_label, "<completed>"); }
            public void OnError(Exception error) { EventLog.Add("error", _label + ": " + error.Message); }
            public void OnNext(T value) { EventLog.Add(_label, Describe(value)); }
        }

        public static string Describe(object value)
        {
            if (value == null) return "<null>";
            try
            {
                var t = value.GetType();
                var name = t.GetProperty("Name")?.GetValue(value)
                           ?? t.GetProperty("DisplayName")?.GetValue(value)
                           ?? t.GetProperty("Title")?.GetValue(value);
                var text = value.ToString();
                if (name != null && !string.Equals(name.ToString(), text, StringComparison.Ordinal))
                {
                    return t.Name + " '" + name + "'";
                }
                return t.Name + " " + text;
            }
            catch (Exception) { return value.GetType().Name; }
        }

        // ---------------------------------------------------------------
        // State snapshot
        // ---------------------------------------------------------------

        public static Dictionary<string, object> State()
        {
            var state = new Dictionary<string, object>();
            try
            {
                var projects = GetService("Keen.VRage.Editor.Services.Project.IProjectsService");
                var current = projects?.GetType().GetProperty("Current")?.GetValue(projects);
                state["project"] = Describe(current);

                var selection = GetService("Keen.VRage.Editor.Services.Selection.ISelectionService");
                if (selection != null)
                {
                    var st = selection.GetType();
                    state["selected_asset"] = Describe(st.GetProperty("SelectedAsset")?.GetValue(selection));
                    state["opened_asset"] = Describe(st.GetProperty("OpenedAsset")?.GetValue(selection));
                    state["inspected_asset"] = Describe(st.GetProperty("InspectedAsset")?.GetValue(selection));
                }
                else
                {
                    state["selection"] = "ISelectionService not available";
                }

                state["window_title"] = MainWindowTitle();
                state["latest_event_id"] = EventLog.LatestId;
                state["subscriptions"] = Subscriptions.Count;

                // If a script is wedged, this is the one place a caller can find
                // out without waiting for another call to time out.
                var running = RunningScript();
                if (running != null) state["running_script"] = running;
            }
            catch (Exception ex) { state["error"] = ex.Message; }
            return state;
        }

        private static string MainWindowTitle()
        {
            try
            {
                // Avalonia controls may only be touched from the UI thread;
                // reading Title from the HTTP worker throws.
                var task = Dispatcher.UIThread.InvokeAsync(
                    () => MainWindow()?.Title ?? "<no window>").GetTask();
                return task.Wait(3000) ? task.Result : "<ui thread busy>";
            }
            catch (Exception ex) { return "<unavailable: " + ex.Message + ">"; }
        }

        private static Window MainWindow()
        {
            var lifetime = Application.Current?.ApplicationLifetime as IClassicDesktopStyleApplicationLifetime;
            return lifetime?.MainWindow;
        }

        // ---------------------------------------------------------------
        // Screenshot
        // ---------------------------------------------------------------

        [DllImport("user32.dll")]
        private static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);

        [DllImport("user32.dll")]
        private static extern bool PrintWindow(IntPtr hWnd, IntPtr hdcBlt, uint nFlags);

        [StructLayout(LayoutKind.Sequential)]
        private struct RECT { public int Left, Top, Right, Bottom; }

        /// <summary>Include layered/GPU-composited children, not just the frame.</summary>
        private const uint PW_RENDERFULLCONTENT = 0x00000002;

        /// <summary>
        /// Capture the editor window as PNG bytes.
        ///
        /// PrintWindow asks the window to redraw itself into our device context,
        /// so the capture is current even when the editor sits behind other
        /// windows. A plain screen copy returns whatever the compositor last
        /// showed, which for an unfocused window is a stale frame — that is only
        /// used as a fallback when PrintWindow refuses.
        ///
        /// Avalonia's own bitmap export is not an option: the 3D viewport is a
        /// native GPU surface and comes out as an empty rectangle.
        /// </summary>
        public static byte[] Screenshot()
        {
            IntPtr hwnd = IntPtr.Zero;
            var done = Dispatcher.UIThread.InvokeAsync(() =>
            {
                var w = MainWindow();
                var handle = w?.TryGetPlatformHandle();
                hwnd = handle?.Handle ?? IntPtr.Zero;
            });
            done.GetTask().Wait(5000);

            if (hwnd == IntPtr.Zero) throw new InvalidOperationException("Editor window handle not available");
            if (!GetWindowRect(hwnd, out var r)) throw new InvalidOperationException("GetWindowRect failed");

            int width = Math.Max(1, r.Right - r.Left);
            int height = Math.Max(1, r.Bottom - r.Top);

            using (var bmp = new Bitmap(width, height, PixelFormat.Format32bppArgb))
            {
                bool printed = false;
                using (var g = Graphics.FromImage(bmp))
                {
                    IntPtr hdc = g.GetHdc();
                    try { printed = PrintWindow(hwnd, hdc, PW_RENDERFULLCONTENT); }
                    finally { g.ReleaseHdc(hdc); }
                }

                if (!printed)
                {
                    using var g2 = Graphics.FromImage(bmp);
                    g2.CopyFromScreen(r.Left, r.Top, 0, 0,
                        new System.Drawing.Size(width, height), CopyPixelOperation.SourceCopy);
                }

                using (var ms = new MemoryStream())
                {
                    bmp.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }

        // ---------------------------------------------------------------
        // In-process C#
        // ---------------------------------------------------------------

        /// <summary>
        /// Compile and run C# inside the editor process.
        ///
        /// State carries over between calls, so a session can build up context.
        /// When <paramref name="onUiThread"/> is set the script runs on the
        /// Avalonia UI thread, which is required for anything that touches
        /// windows, view models or the render view — the editor is no more
        /// thread-safe than any other UI application.
        /// </summary>
        // What is running right now, so a second caller can be told rather than
        // silently queued behind it.
        private static volatile string _busyCode;
        private static DateTime _busyStarted;
        private static DateTime _deadline = DateTime.MaxValue;

        /// <summary>
        /// The budget check a long-running script is expected to call.
        ///
        /// On the UI thread a script cannot be aborted: .NET Core has no
        /// Thread.Abort, and Roslyn's cancellation token is only observed
        /// between statements and at await points — a tight `while (true)` sails
        /// straight past it and freezes the editor's dispatcher. So the honest
        /// design is cooperative: call this inside any loop and it throws once
        /// the time budget is spent. Every snippet this bridge ships does.
        /// </summary>
        public static void Watchdog()
        {
            if (DateTime.UtcNow > _deadline)
            {
                throw new TimeoutException(
                    "Script exceeded its time budget. Raise timeout_ms, or move the "
                    + "work off the UI thread with ui_thread=false.");
            }
        }

        /// <summary>Alias, because `Tick()` is what people write in a loop.</summary>
        public static void Tick() => Watchdog();

        /// <summary>What is currently executing, or null. Reported by /state.</summary>
        public static object RunningScript()
        {
            var code = _busyCode;
            if (code == null) return null;
            return new Dictionary<string, object>
            {
                ["running_for_seconds"] = Math.Round((DateTime.UtcNow - _busyStarted).TotalSeconds, 1),
                ["code"] = code.Length <= 200 ? code : code.Substring(0, 200) + " …",
            };
        }

        public static object Eval(string code, bool onUiThread, int timeoutMs)
        {
            if (string.IsNullOrWhiteSpace(code)) throw new ArgumentException("code is empty");

            // A script already stuck on the UI thread has frozen the dispatcher.
            // Posting another one there would queue behind it and time out too,
            // so the caller would learn nothing and the editor would fall further
            // behind. Refuse immediately and say what is holding it.
            var busy = _busyCode;
            if (busy != null)
            {
                throw new InvalidOperationException(
                    "Another script has been running for "
                    + Math.Round((DateTime.UtcNow - _busyStarted).TotalSeconds, 1)
                    + "s and has not returned: \""
                    + (busy.Length <= 120 ? busy : busy.Substring(0, 120) + " …")
                    + "\". The editor cannot interrupt it; restart the editor if it "
                    + "never finishes.");
            }

            var budget = Math.Max(1000, timeoutMs);

            // Start the script's clock here rather than inside `run`. Dispatching
            // to the UI thread can take a moment when it is busy, and a deadline
            // measured from execution instead of from arrival drifts past the
            // outer wait by exactly that delay — which is how the outer timeout
            // ends up winning a race it is only meant to backstop.
            _busyCode = code;
            _busyStarted = DateTime.UtcNow;
            _deadline = _busyStarted.AddMilliseconds(budget);

            Func<object> run = () =>
            {
                lock (ScriptLock)
                {
                    try
                    {
                        if (_scriptState == null)
                        {
                            var options = ScriptOptions.Default
                                .WithReferences(AppDomain.CurrentDomain.GetAssemblies()
                                    .Where(a => !a.IsDynamic && !string.IsNullOrEmpty(a.Location)))
                                .WithImports(
                                    "System", "System.Linq", "System.Collections.Generic",
                                    "System.Reflection", "Avalonia", "SE2McpBridge");
                            _scriptState = CSharpScript.RunAsync(code, options).GetAwaiter().GetResult();
                        }
                        else
                        {
                            _scriptState = _scriptState.ContinueWithAsync(code).GetAwaiter().GetResult();
                        }
                        return _scriptState.ReturnValue;
                    }
                    finally
                    {
                        _busyCode = null;
                        _deadline = DateTime.MaxValue;
                    }
                }
            };

            // The script's own budget expires at `budget`; this wait has to
            // expire later, or the two race and the outer timeout wins — which
            // reports "the editor is stuck" for a script that was in the act of
            // stopping itself cleanly. The grace period lets the cooperative
            // path finish and produce the message that actually helps.
            var grace = budget + 1500;

            if (!onUiThread) return RunWithTimeout(run, grace);

            var task = Dispatcher.UIThread.InvokeAsync(run).GetTask();
            if (!task.Wait(grace))
            {
                throw new TimeoutException(
                    "Script did not finish within " + grace + " ms on the UI thread. "
                    + "It is still running and the editor is unresponsive until it "
                    + "returns. Call EditorApi.Watchdog() inside loops so a script "
                    + "can stop itself, or pass ui_thread=false for pure computation.");
            }
            return task.Result;
        }

        private static object RunWithTimeout(Func<object> run, int timeoutMs)
        {
            var task = Task.Run(run);
            if (!task.Wait(timeoutMs))
            {
                throw new TimeoutException("Script did not finish within " + timeoutMs + " ms and did not stop itself. Call EditorApi.Watchdog() inside loops.");
            }
            return task.Result;
        }

        public static void ResetScriptState()
        {
            lock (ScriptLock) { _scriptState = null; }
        }
    }
}
