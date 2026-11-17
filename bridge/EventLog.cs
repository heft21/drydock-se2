using System;
using System.Collections.Generic;

namespace SE2McpBridge
{
    /// <summary>
    /// A bounded, monotonically numbered event buffer.
    ///
    /// This is what makes "watch the editor moment to moment" possible without
    /// a socket push: every event gets an increasing id, and a client polls
    /// /events?since=&lt;last id&gt; to receive exactly what it has not seen.
    /// Nothing is ever pushed, so a disconnected client costs nothing.
    /// </summary>
    public static class EventLog
    {
        public sealed class Entry
        {
            public long Id { get; set; }
            public string Time { get; set; }
            public string Kind { get; set; }
            public string Message { get; set; }
        }

        private const int Capacity = 500;

        private static readonly object Lock = new object();
        private static readonly Queue<Entry> Entries = new Queue<Entry>(Capacity);
        private static long _next = 1;

        public static void Add(string kind, string message)
        {
            lock (Lock)
            {
                if (Entries.Count >= Capacity)
                {
                    Entries.Dequeue();
                }
                Entries.Enqueue(new Entry
                {
                    Id = _next++,
                    Time = DateTime.Now.ToString("HH:mm:ss.fff"),
                    Kind = kind,
                    Message = message ?? string.Empty,
                });
            }
        }

        /// <summary>Events newer than <paramref name="since"/>, oldest first.</summary>
        public static List<Entry> Since(long since, int limit)
        {
            var result = new List<Entry>();
            lock (Lock)
            {
                foreach (var e in Entries)
                {
                    if (e.Id > since)
                    {
                        result.Add(e);
                    }
                }
            }
            if (limit > 0 && result.Count > limit)
            {
                result.RemoveRange(0, result.Count - limit);
            }
            return result;
        }

        public static long LatestId
        {
            get { lock (Lock) { return _next - 1; } }
        }
    }
}
