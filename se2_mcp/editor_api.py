"""Typed operations that run inside the editor process.

The editor's service and view-model types are `internal`, so they cannot be
named from outside the assembly; everything has to go through reflection from
within the process. This module keeps that reflection code as C# snippets, so
the common operations do not have to be hand-written every time — while
`editor_eval` stays available as the escape hatch.

The snippets are written defensively: when a member is missing they return what
they *did* find rather than throwing, because these types change between SDK
versions and a list of what exists is the fastest way to adapt.
"""

from __future__ import annotations

# Every snippet returns a single line of JSON, which the Python side parses.
_PRELUDE = r"""
using System.Linq;
using System.Collections;
using System.Reflection;

object Svc(string n) => EditorApi.GetService(n);

object Prop(object o, string name) {
    if (o == null) return null;
    var p = o.GetType().GetProperty(name,
        BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
    return p == null ? null : p.GetValue(o);
}

object StaticProp(string typeName, string name) {
    var t = EditorApi.FindType(typeName);
    if (t == null) return null;
    var p = t.GetProperty(name, BindingFlags.Public | BindingFlags.NonPublic |
                                BindingFlags.Static | BindingFlags.FlattenHierarchy);
    return p == null ? null : p.GetValue(null);
}

string J(object v) => System.Text.Json.JsonSerializer.Serialize(v);

// Call inside any loop. The editor cannot abort a script running on its UI
// thread, so a long one has to agree to stop itself; this throws once the
// call's time budget is spent.
void Tick() => EditorApi.Watchdog();
"""


def snippet(body: str) -> str:
    return _PRELUDE + "\n" + body


# --------------------------------------------------------------------------
# Asset Validation - the thing that blocks publishing
# --------------------------------------------------------------------------

VALIDATION = snippet(r"""
var mainVm = StaticProp("Keen.VRage.Editor.Core.MainViewModel", "Instance");
if (mainVm == null) return J(new { error = "MainViewModel.Instance not found" });

var vms = Prop(mainVm, "ViewModels") as IEnumerable;
if (vms == null) return J(new { error = "MainViewModel.ViewModels could not be read" });

object val = null;
var names = new List<string>();
foreach (var vm in vms) {
    if (vm == null) continue;
    names.Add(vm.GetType().Name);
    if (vm.GetType().Name == "AssetValidationViewModel") val = vm;
}
if (val == null)
    return J(new { error = "AssetValidationViewModel is not present", viewmodels = names });

var summary = Prop(val, "Summary") as string;
var states = Prop(val, "InvalidValidationStates") as IEnumerable;
var rows = new List<object>();
if (states != null) {
    foreach (var st in states) {
        if (rows.Count >= 60) break;
        var ctrl = Prop(st, "ValidationController");
        var asset = ctrl != null ? Prop(ctrl, "Asset") : null;
        var issues = Prop(st, "Issues") as IEnumerable;
        var msgs = new List<string>();
        if (issues != null)
            foreach (var i in issues) {
                if (msgs.Count >= 8) break;
                msgs.Add((Prop(i, "Message") ?? Prop(i, "Text") ?? i).ToString());
            }
        rows.Add(new {
            asset = asset == null ? "?" : (Prop(asset, "Name") ?? asset).ToString(),
            severity = (Prop(st, "Severity") ?? "?").ToString(),
            issues = msgs
        });
    }
}
return J(new { summary, invalid_count = rows.Count, problems = rows });
""")


# --------------------------------------------------------------------------
# Building - the editor's own cache generation. The CLI cannot load Vanilla,
# so for a real mod this is the only route.
# --------------------------------------------------------------------------

BUILD = snippet(r"""
var svc = Svc("Keen.VRage.Editor.Services.Project.IProjectsService");
if (svc == null) return J(new { error = "IProjectsService is not registered" });
var m = svc.GetType().GetMethod("GenerateCacheAndDefinitionSet");
if (m == null) return J(new {
    error = "IProjectsService has no GenerateCacheAndDefinitionSet method",
    methods = svc.GetType().GetMethods().Select(x => x.Name).Distinct().Take(30)
});
var ps = m.GetParameters();
var args = new object[ps.Length];
for (int i = 0; i < ps.Length; i++)
    args[i] = ps[i].Name == "withBlobs" ? (object)WITH_BLOBS
            : ps[i].Name == "withDependencies" ? (object)WITH_DEPS
            : (ps[i].HasDefaultValue ? ps[i].DefaultValue : null);
m.Invoke(svc, args);
return J(new { ok = true, invoked = "GenerateCacheAndDefinitionSet",
               args = ps.Select(p => p.Name) });
""")


PROJECT_INFO = snippet(r"""
var svc = Svc("Keen.VRage.Editor.Services.Project.IProjectsService");
var cur = Prop(svc, "Current");
if (cur == null) return J(new { loaded = false });
var root = Prop(cur, "RootProject");
var vr = root != null ? Prop(root, "VRageProject") : null;
return J(new {
    loaded = true,
    root = root == null ? null : (Prop(root, "Name") ?? root).ToString(),
    project_type = vr == null ? null : (Prop(vr, "Type") ?? "").ToString(),
    dag = cur.GetType().Name
});
""")


VIEWMODELS = snippet(r"""
var mainVm = StaticProp("Keen.VRage.Editor.Core.MainViewModel", "Instance");
if (mainVm == null) return J(new { error = "MainViewModel.Instance not found" });
var vms = Prop(mainVm, "ViewModels") as IEnumerable;
var rows = new List<object>();
if (vms != null)
    foreach (var vm in vms) {
        if (vm == null) continue;
        rows.Add(new {
            name = vm.GetType().Name,
            full = vm.GetType().FullName,
            props = vm.GetType().GetProperties(BindingFlags.Public | BindingFlags.Instance)
                      .Select(p => p.Name).Take(24)
        });
    }
return J(new { count = rows.Count, viewmodels = rows });
""")


SELECTION = snippet(r"""
var sel = Svc("Keen.VRage.Editor.Services.Selection.ISelectionService");
if (sel == null) return J(new { error = "ISelectionService is not registered" });
string Describe(object o) => o == null ? null : (Prop(o, "Name") ?? o).ToString();
return J(new {
    selected = Describe(Prop(sel, "SelectedAsset")),
    opened = Describe(Prop(sel, "OpenedAsset")),
    inspected = Describe(Prop(sel, "InspectedAsset"))
});
""")


def vm_of(name: str) -> str:
    """C# that picks one view-model out of MainViewModel.ViewModels by name."""
    return f'''
var _mv = StaticProp("Keen.VRage.Editor.Core.MainViewModel", "Instance");
if (_mv == null) return J(new {{ error = "MainViewModel.Instance not found" }});
var _vms = Prop(_mv, "ViewModels") as IEnumerable;
object VM = null;
if (_vms != null) foreach (var v in _vms)
    if (v != null && v.GetType().Name == "{name}") VM = v;
if (VM == null) return J(new {{ error = "{name} is not among the live view-models" }});
'''


# Walking the project tree: which folder is shown, and what is in it.
EXPLORER = snippet(vm_of("ProjectExplorerViewModel") + r"""
string Nm(object o) => o == null ? null : (Prop(o, "Name") ?? o).ToString();

var folder = Prop(VM, "ShownFolder");
var rows = new List<object>();
var grid = Prop(Prop(VM, "ExplorerGrid"), "Items") as IEnumerable;
if (grid != null)
    foreach (var it in grid) {
        if (rows.Count >= 120) break;
        if (it == null) continue;
        rows.Add(new { name = Nm(it), kind = it.GetType().Name });
    }
return J(new {
    main_project = Nm(Prop(VM, "MainProject")),
    shown_folder = Nm(folder),
    items = rows,
    item_count = rows.Count
});
""")


# Selecting/opening an asset: find it in the explorer by name, hand it to the
# selection service.
OPEN_ASSET = snippet(vm_of("ProjectExplorerViewModel") + r"""
string Nm(object o) => o == null ? null : (Prop(o, "Name") ?? o).ToString();
var target = "TARGET_NAME";

object hit = null;
var grid = Prop(Prop(VM, "ExplorerGrid"), "Items") as IEnumerable;
var seen = new List<string>();
if (grid != null)
    foreach (var it in grid) {
        var n = Nm(it);
        if (n == null) continue;
        seen.Add(n);
        if (string.Equals(n, target, StringComparison.OrdinalIgnoreCase)) { hit = it; break; }
    }
if (hit == null)
    foreach (var n in seen)
        if (n.IndexOf(target, StringComparison.OrdinalIgnoreCase) >= 0) {
            foreach (var it in grid) if (Nm(it) == n) { hit = it; break; }
            break;
        }
if (hit == null)
    return J(new { error = "No asset named: " + target, visible = seen.Take(40) });

var sel = Svc("Keen.VRage.Editor.Services.Selection.ISelectionService");
if (sel == null) return J(new { error = "ISelectionService is not registered" });
var st = sel.GetType();
st.GetProperty("SelectedAsset").SetValue(sel, hit);
if (SET_OPEN) {
    var op = st.GetProperty("OpenedAsset");
    if (op != null && op.PropertyType.IsInstanceOfType(hit)) op.SetValue(sel, hit);
}
var ins = st.GetProperty("InspectedAsset");
if (ins != null && ins.PropertyType.IsInstanceOfType(hit)) ins.SetValue(sel, hit);
return J(new { ok = true, selected = Nm(hit), type = hit.GetType().Name });
""")


# Bring the window back before a screen capture.
#
# The capture is a PrintWindow of the window rect, so a minimized editor — which
# Windows parks at -32000,-32000 with a title-bar-sized rect — yields a valid
# PNG a couple of hundred pixels wide instead of an error. That is the worst
# kind of failure to hand a model: it looks like it worked. Restoring first
# removes the failure rather than reporting it.
SHOW_WINDOW = snippet(r"""
var lt = Avalonia.Application.Current?.ApplicationLifetime
         as Avalonia.Controls.ApplicationLifetimes.IClassicDesktopStyleApplicationLifetime;
var w = lt?.MainWindow;
if (w == null) return J(new { error = "No main window" });
var was = w.WindowState.ToString();
if (w.WindowState == Avalonia.Controls.WindowState.Minimized)
    w.WindowState = Avalonia.Controls.WindowState.Normal;
w.Show();
w.Activate();
return J(new { was_state = was, state = w.WindowState.ToString(),
               width = w.Width, height = w.Height,
               x = w.Position.X, y = w.Position.Y });
""")


SAVE = snippet(r"""
var mainVm = StaticProp("Keen.VRage.Editor.Core.MainViewModel", "Instance");
if (mainVm == null) return J(new { error = "MainViewModel.Instance not found" });
var cands = mainVm.GetType().GetMethods(BindingFlags.Public | BindingFlags.NonPublic |
                                        BindingFlags.Instance)
    .Where(m => m.GetParameters().Length == 0 &&
                (m.Name.Contains("Save") || m.Name.Contains("save")))
    .Select(m => m.Name).Distinct().ToList();
return J(new { save_like_methods = cands,
               hint = "Call the appropriate one with editor_eval" });
""")


# The "Create Prefab" / "Create Asset" context menus.
#
# These are a MenuItemViewModel tree: Header is the visible label, Items the
# submenu, and Command a ReactiveCommand<ProjectExplorerFolderViewModel, Unit>.
# A ReactiveCommand is also an ICommand, so Execute(folder) runs it directly --
# which is what makes generating a block from a template possible at all.
_MENU_WALK = r"""
void Walk(IEnumerable src, string prefix, List<object> outp) {
    if (src == null) return;
    foreach (var o in src) {
        if (o == null || outp.Count >= 200) return;
        var header = (Prop(o, "Header") ?? "").ToString();
        var path = prefix.Length == 0 ? header : prefix + "/" + header;
        var kids = Prop(o, "Items") as IEnumerable;
        bool hasKids = false;
        if (kids != null) foreach (var _ in kids) { hasKids = true; break; }
        if (hasKids) Walk(kids, path, outp);
        else {
            if (FILTER.Length > 0 &&
                path.IndexOf(FILTER, StringComparison.OrdinalIgnoreCase) < 0) continue;
            var en = Prop(o, "IsEnabled");
            // Disabled entries need their reason; on enabled ones the tooltip
            // just repeats the label.
            if (en is bool b && b) outp.Add(new { path });
            else outp.Add(new { path, enabled = false,
                                reason = (Prop(o, "ToolTip") ?? "").ToString() });
        }
    }
}
"""

GENERATORS = snippet(vm_of("ProjectExplorerViewModel") + _MENU_WALK + r"""
var grid = Prop(VM, "ExplorerGrid");
if (grid == null) return J(new { error = "ProjectExplorer has no ExplorerGrid" });
var assets = new List<object>();
var prefabs = new List<object>();
Walk(Prop(grid, "AssetGenerators") as IEnumerable, "", assets);
Walk(Prop(grid, "PrefabGenerators") as IEnumerable, "", prefabs);
var folder = Prop(VM, "ShownFolder");
return J(new {
    target_folder = folder == null ? null : (Prop(folder, "Name") ?? folder).ToString(),
    filter = FILTER.Length == 0 ? null : FILTER,
    asset_generators = assets,
    prefab_generators = prefabs,
    hint = "Narrow a long list with `contains`; a path here is what editor_create_from_template takes."
});
""")


# Execute a menu path: generates an asset or prefab from its template.
CREATE_FROM_TEMPLATE = snippet(vm_of("ProjectExplorerViewModel") + r"""
var wanted = "MENU_PATH";
var which = "WHICH_MENU";
var grid = Prop(VM, "ExplorerGrid");
if (grid == null) return J(new { error = "ProjectExplorer has no ExplorerGrid" });

object found = null;
var available = new List<string>();
void Find(IEnumerable src, string prefix) {
    if (src == null || found != null) return;
    foreach (var o in src) {
        if (o == null || found != null) return;
        var header = (Prop(o, "Header") ?? "").ToString();
        var path = prefix.Length == 0 ? header : prefix + "/" + header;
        var kids = Prop(o, "Items") as IEnumerable;
        bool hasKids = false;
        if (kids != null) foreach (var _ in kids) { hasKids = true; break; }
        if (hasKids) { Find(kids, path); continue; }
        available.Add(path);
        if (string.Equals(path, wanted, StringComparison.OrdinalIgnoreCase)) found = o;
    }
}
Find(Prop(grid, which) as IEnumerable, "");
if (found == null)
    return J(new { error = "No such menu path: " + wanted, available = available.Take(60) });
if (!(Prop(found, "IsEnabled") is bool en) || !en)
    return J(new { error = "That template is currently disabled",
                   reason = (Prop(found, "ToolTip") ?? "").ToString() });

var folder = Prop(VM, "ShownFolder");
if (folder == null) return J(new { error = "No target folder; open a folder in the Project Explorer first" });

var cmd = Prop(found, "Command") as System.Windows.Input.ICommand;
if (cmd == null) return J(new { error = "Menu entry exposes no ICommand" });
cmd.Execute(folder);
return J(new { ok = true, executed = wanted,
               folder = (Prop(folder, "Name") ?? folder).ToString(),
               note = "The editor may now be showing its own name prompt window." });
""")
