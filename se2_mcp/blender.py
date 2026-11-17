"""Client for a running Blender with the BlenderMCP add-on, plus SE2 helpers.

Blender is where SE2 models are actually made: Keen ships an official add-on,
``vrage_tools``, whose 27 operators produce exactly the FBX/LOD/collision layout
the content pipeline expects. The BlenderMCP add-on listens on 127.0.0.1:9876
and speaks newline-free JSON over a raw socket, so this module is a direct
client — no second MCP server in the loop.

Two measured constraints shape everything here:

* ``execute_code`` returns whatever the snippet printed to **stdout**. Assigning
  to a variable returns nothing, so every helper ends in ``print()``.
* ``bpy.ops.*()`` called from a script runs ``execute()`` directly and never
  shows the operator's confirmation popup, which is what makes VRAGE Tools
  scriptable at all.
"""

from __future__ import annotations

import json
import os
import socket
from pathlib import Path
from typing import Any

from . import toolkit
from .config import PATHS

DEFAULT_PORT = 9876

# The shipped material library. Vanilla blocks share these materials rather than
# carrying per-block textures, so importing it is how a model gets SE2-correct
# surfacing without painting anything.
MATERIAL_LIBRARY = PATHS.sdk / "BlenderMaterialLibrary" / "SE2Decal&Material.zip"

# Keen's reference art: an FBX/LOD/collision set laid out the way the pipeline
# wants, useful both as a template and as a source of real materials.
EXAMPLE_MOD = PATHS.sdk / "ExampleMod1"

EXPORT_VARIANTS = ("NON_FRACTURED", "FRACTURED", "DEFORMED", "NONE")
EXPORT_LIMITS = ("SELECTED_OBJECTS", "ACTIVE_COLLECTION", "VISIBLE_OBJECTS")


class BlenderDown(RuntimeError):
    """Blender is not running, or the BlenderMCP add-on is not listening."""


def port() -> int:
    return int(os.environ.get("SE2_MCP_BLENDER_PORT", DEFAULT_PORT))


def address() -> str:
    return f"127.0.0.1:{port()}"


def call(command: str, params: dict | None = None, timeout: float = 120) -> Any:
    """Send one command and return the add-on's parsed reply.

    The add-on writes a single JSON document and keeps the socket open, so the
    end of the message has to be found by trying to parse what has arrived so
    far rather than by waiting for EOF.
    """
    sock = socket.socket()
    sock.settimeout(timeout)
    try:
        sock.connect(("127.0.0.1", port()))
    except OSError as exc:
        sock.close()          # the finally below is only reached once connected
        raise BlenderDown(
            f"No BlenderMCP at {address()}: {toolkit.describe_os_error(exc)}. "
            f"Start Blender, then enable the BlenderMCP add-on and press "
            f"'Connect to Claude'."
        ) from exc
    try:
        sock.sendall(json.dumps({"type": command, "params": params or {}}).encode())
        buf = b""
        while True:
            try:
                chunk = sock.recv(65536)
            except socket.timeout as exc:
                raise BlenderDown(f"Blender did not answer within {timeout}s") from exc
            if not chunk:
                break
            buf += chunk
            try:
                return json.loads(buf)
            except json.JSONDecodeError:
                continue          # message still arriving
        raise BlenderDown("Blender closed the connection without a full reply")
    finally:
        sock.close()


def run_python(code: str, timeout: float = 120) -> dict[str, Any]:
    """Execute a snippet in Blender and return what it printed."""
    reply = call("execute_code", {"code": code}, timeout=timeout)
    if reply.get("status") != "success":
        return {"ok": False, "error": reply.get("message") or reply}
    result = reply.get("result")
    if isinstance(result, dict):
        result = result.get("result", result)
    return {"ok": True, "output": result if isinstance(result, str) else json.dumps(result)}


def run_json(code: str, timeout: float = 120) -> Any:
    """Run a snippet whose last line prints one JSON document, and parse it."""
    out = run_python(code, timeout=timeout)
    if not out["ok"]:
        return out
    text = (out["output"] or "").strip()
    # Snippets may print progress before the payload; the document is last.
    for start in range(len(text)):
        if text[start] in "{[":
            try:
                return json.loads(text[start:])
            except json.JSONDecodeError:
                continue
    return {"ok": False, "error": "Snippet printed no JSON", "output": text[:2000]}


def is_up() -> bool:
    try:
        call("get_scene_info", timeout=5)
        return True
    except (BlenderDown, json.JSONDecodeError):
        return False


# ---------------------------------------------------------------------------
# Snippets
# ---------------------------------------------------------------------------

STATUS = r"""
import bpy, addon_utils, json
mods = [m.__name__ for m in addon_utils.modules()]
vrage = [m for m in mods if "vrage" in m.lower()]
enabled = [m for m in vrage if addon_utils.check(m)[1]]
scene = bpy.context.scene
vrt = getattr(scene, "vrt", None)
meshes = [o for o in scene.objects if o.type == "MESH"]
tris = 0
for o in meshes:
    try:
        tris += sum(len(p.vertices) - 2 for p in o.data.polygons)
    except Exception:
        pass
print(json.dumps({
    "blender": bpy.app.version_string,
    "blend_file": bpy.data.filepath or None,
    "vrage_tools_installed": bool(vrage),
    "vrage_tools_enabled": bool(enabled),
    "vrage_operators": len([o for o in dir(bpy.ops.scene) if o.startswith("vrt")])
                     + len([o for o in dir(bpy.ops.object) if o.startswith("vrt")]),
    "scene": scene.name,
    "objects": len(scene.objects),
    "meshes": len(meshes),
    "triangles": tris,
    "materials": len(bpy.data.materials),
    "material_names": sorted(m.name for m in bpy.data.materials)[:40],
    "export_name": getattr(vrt, "export_name", None),
    "export_directory": getattr(vrt, "export_directory", None),
}))
"""

# SE2 block sizing, measured from vanilla FBX imports: the number in a block's
# name is its largest dimension in centimetres, so a "250" block must fit in
# 2.5 m. Reporting the fit is more useful than reporting raw dimensions.
MEASURE = r"""
import bpy, json
sel = [o for o in bpy.context.selected_objects if o.type == "MESH"] \
      or [o for o in bpy.context.scene.objects if o.type == "MESH"]
out = []
gmin = [1e9, 1e9, 1e9]
gmax = [-1e9, -1e9, -1e9]
total_tris = 0
total_verts = 0
for o in sel:
    tris = sum(len(p.vertices) - 2 for p in o.data.polygons)
    total_tris += tris
    total_verts += len(o.data.vertices)
    for corner in o.bound_box:
        w = o.matrix_world @ __import__("mathutils").Vector(corner)
        for i in range(3):
            gmin[i] = min(gmin[i], w[i])
            gmax[i] = max(gmax[i], w[i])
    out.append({
        "name": o.name, "triangles": tris, "vertices": len(o.data.vertices),
        "materials": [m.name for m in o.data.materials if m],
        "modifiers": [m.type for m in o.modifiers],
        "scale": list(o.scale),
        "ngons": sum(1 for p in o.data.polygons if len(p.vertices) > 4),
        "unapplied_scale": [round(s, 4) for s in o.scale] != [1.0, 1.0, 1.0],
    })
size = [round(gmax[i] - gmin[i], 4) for i in range(3)] if out else [0, 0, 0]
print(json.dumps({
    "objects": out,
    "total_triangles": total_tris,
    "total_vertices": total_verts,
    "bounding_size_m": size,
    "largest_dimension_m": max(size) if out else 0,
}))
"""


def status() -> dict[str, Any]:
    """Is Blender reachable, and is it set up for SE2 work?"""
    out: dict[str, Any] = {
        "address": address(),
        "material_library": str(MATERIAL_LIBRARY),
        "material_library_present": MATERIAL_LIBRARY.is_file(),
        "example_mod": str(EXAMPLE_MOD) if EXAMPLE_MOD.is_dir() else None,
    }
    try:
        info = run_json(STATUS, timeout=30)
    except BlenderDown as exc:
        out["connected"] = False
        out["reason"] = str(exc)
        return out
    out["connected"] = True
    if isinstance(info, dict):
        out.update(info)
    if not out.get("vrage_tools_enabled"):
        out["warning"] = (
            "VRAGE Tools is not enabled. Without it there is no SE2-correct FBX "
            "export; install it from the Mod SDK and enable it in Blender's "
            "add-on preferences."
        )
    return out


def measure(subject: str = "") -> dict[str, Any]:
    """Geometry report for the selection, judged against SE2 block limits."""
    info = run_json(MEASURE, timeout=60)
    if not isinstance(info, dict) or "bounding_size_m" not in info:
        return info if isinstance(info, dict) else {"ok": False, "error": str(info)}

    largest = info.get("largest_dimension_m") or 0
    info["block_size_note"] = (
        "A block's name carries its largest dimension in centimetres "
        "(IonThruster500 measures 5.006 x 2.511 x 2.514 m). A model that "
        "exceeds its declared size places incorrectly."
    )
    if subject:
        digits = "".join(c for c in subject if c.isdigit())
        if digits:
            limit = int(digits) / 100.0
            info["declared_size_m"] = limit
            info["fits_declared_size"] = largest <= limit * 1.02
            if not info["fits_declared_size"]:
                info["problem"] = (
                    f"Model is {largest:.3f} m across but '{subject}' declares "
                    f"{limit:.2f} m. Scale it down or rename the block."
                )
    info["suggested_size_class"] = int(round(largest * 100)) if largest else None
    return info


def export_model(
    name: str,
    models_dir: str | Path,
    *,
    variant: str = "NON_FRACTURED",
    limit: str = "SELECTED_OBJECTS",
    lods: tuple[int, ...] | list[int] = (0,),
    collisions: bool = False,
) -> dict[str, Any]:
    """Drive VRAGE Tools' exporter to write the layout the pipeline expects.

    ``models_dir`` is the *parent* of the variant folder: the operator creates
    ``NonFractured/`` (or ``Fractured/``, ``Deformed/``) underneath it and writes
    ``<name>.fbx`` plus ``<name>_LOD1..3.fbx`` and the collision glTF there,
    matching Keen's ExampleMod1 exactly.
    """
    if variant not in EXPORT_VARIANTS:
        return {"ok": False, "error": f"variant must be one of {EXPORT_VARIANTS}"}
    if limit not in EXPORT_LIMITS:
        return {"ok": False, "error": f"limit must be one of {EXPORT_LIMITS}"}

    target = Path(models_dir)
    target.mkdir(parents=True, exist_ok=True)
    lod_list = [int(x) for x in lods]

    code = f"""
import bpy, json, os
vrt = bpy.context.scene.vrt
vrt.export_name = {name!r}
vrt.export_directory = {str(target)!r}
vrt.export_variant = {variant!r}
vrt.export_limit = {limit!r}
done = []
errors = []
for lod in {lod_list!r}:
    try:
        r = bpy.ops.scene.vrt_quick_export(export_lod=lod)
        done.append({{"lod": lod, "result": list(r)}})
    except Exception as exc:
        errors.append({{"lod": lod, "error": str(exc)}})
if {bool(collisions)!r}:
    try:
        r = bpy.ops.scene.vrt_quick_export_collisions()
        done.append({{"collisions": list(r)}})
    except Exception as exc:
        errors.append({{"collisions": str(exc)}})
print(json.dumps({{"exported": done, "errors": errors,
                  "directory": vrt.export_directory}}))
"""
    result = run_json(code, timeout=600)

    # Report what actually landed on disk; the operator's return value says
    # 'FINISHED' even when a variant produced nothing.
    written = []
    for sub in ("NonFractured", "Fractured", "Deformed", ""):
        d = target / sub if sub else target
        if d.is_dir():
            written += [str(p.relative_to(target)) for p in sorted(d.iterdir())
                        if p.suffix.lower() in (".fbx", ".gltf", ".bin")]
    if isinstance(result, dict):
        result["files_on_disk"] = written
        result["ok"] = bool(written) and not result.get("errors")
        if not written:
            result["hint"] = (
                "Nothing was written. With limit='SELECTED_OBJECTS' the export "
                "silently does nothing when the selection is empty — select the "
                "mesh first, or pass limit='VISIBLE_OBJECTS'."
            )
    return result


def import_material_library() -> dict[str, Any]:
    """Append SE2's shared materials so a model can use vanilla surfacing.

    Vanilla blocks do not ship per-block LOD0 textures; they reference a shared
    library (PaintedMetalColorable, MetalDull, Chrome, the AtlasDecal set...).
    Assigning those is how a mod block ends up looking like a vanilla one.
    """
    if not MATERIAL_LIBRARY.is_file():
        return {"ok": False, "error": f"Material library not found: {MATERIAL_LIBRARY}"}

    code = f"""
import bpy, json, zipfile, tempfile, os, glob
src = {str(MATERIAL_LIBRARY)!r}
tmp = os.path.join(tempfile.gettempdir(), "se2_material_library")
os.makedirs(tmp, exist_ok=True)
with zipfile.ZipFile(src) as z:
    z.extractall(tmp)
blends = glob.glob(os.path.join(tmp, "**", "*.blend"), recursive=True)
before = set(m.name for m in bpy.data.materials)
for b in blends:
    with bpy.data.libraries.load(b, link=False) as (src_data, dst_data):
        dst_data.materials = list(src_data.materials)
after = set(m.name for m in bpy.data.materials)
print(json.dumps({{"blend_files": [os.path.basename(b) for b in blends],
                  "added": sorted(after - before),
                  "total_materials": len(after)}}))
"""
    result = run_json(code, timeout=300)
    if isinstance(result, dict) and result.get("added") is not None:
        result["ok"] = True
        result["note"] = (
            "Assign these to your mesh instead of authoring LOD0 textures. Only "
            "the furthest LOD uses a baked per-block atlas (the LODMaterial "
            "folder); LOD0-3 share the library."
        )
    return result
