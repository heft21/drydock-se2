---
name: se2-modsdk
description: Handbook for modding Space Engineers 2 with the VRAGE3 Mod SDK. Covers the GUID-addressed definition format, partialdefs, project layout and publishing, planets and their maps, planetary water, blocks and models, voxel materials, the editor/Blender/Mod HUB tooling, and a generated catalogue of every $Type SE2 content uses. Use for any question about authoring, debugging or publishing SE2 (version 2) content — .def/.partialdef files, .vrgproj projects, Mod HUB, VRage.Editor, planet cubemaps, ColorKeys, or the "dependencies hashes do not match" error.
license: MIT
allowed-tools: Read, Bash, Grep, Glob
---

# Space Engineers 2 Mod SDK

Space Engineers 2 content is **GUID-addressed JSON**. Every `.def` and
`.partialdef` carries a `$Type` and a `$Value`, and refers to every other asset
by a bare GUID with no name attached. A folder listing tells you almost nothing,
and most of what matters is documented nowhere.

This handbook is what fills that gap. Read the page for what you are doing
before you start; the mistakes in SE2 modding are almost all convention
mistakes, and they are cheap to avoid and expensive to find.

- [Table of contents](TOC.md)

## Read this first

**[reference/00-orientation.md](reference/00-orientation.md)** — how the content
is shaped, what to look at first, and the four traps that cost the most time.

## Check the version before trusting anything

This handbook was generated against a specific SDK build, recorded in
`sdk_version.txt`. Steam updates the SDK silently.

```bash
python check_version.py
```

Exit codes: `0` match, `2` differ, `1` error.

- **MATCH** — proceed.
- **DIFFER** — the hand-written pages under `reference/` are measured facts and
  age slowly; they are usually still right. The generated `types/` catalogue
  ages with every update and should be rebuilt: `python build_reference.py`.
  Until then, treat a type page as a hint and confirm against the live files.

## The two halves

**`reference/`** is hand-written and measured. Each fact in it came from reading
the shipped data, or from decompiling the content pipeline, or from watching
something fail — not from documentation, which does not exist for most of it.

**`types/`** is generated from the installed SDK: one page per `$Type` that
really occurs in content, with the SDK's own XML field documentation, how many
definitions use it, and a real vanilla file to look at. Start at
[types/index.md](types/index.md), which is sorted by usage — a type used by
9,000 definitions is load-bearing, one used by a single file is a curiosity.

## Working with the MCP server

This skill lives inside the **se2-modsdk MCP server** repository, and the two
are meant to be used together: the handbook explains the shape of things, the
server answers questions about *this* install. When the server is connected,
prefer it over reading files by hand — it resolves GUIDs, which is the whole
problem.

```
sdk_info                       what is installed, is the index ready
search_content('thruster')     find how vanilla does something
resolve_guid('<guid>')         the single most useful operation
read_definition(<guid>)        read it, with every GUID it references named
describe_type('Placement')     what the fields mean
find_references('<guid>')      what breaks if I change this
write_definition(...)          author one, with a correct .meta sidecar
audit_project(<dir>)           the offline check that works on real mods
```

Without the server, everything here still works: the reference pages are plain
Markdown and the type pages name real file paths you can open directly.

## Never

- **Never edit anything inside the SDK's `GameData`.** It is reference material.
  A mod changes vanilla content with an `Override` partialdef instead.
- **Never re-serialise a definition with a generic JSON writer.** Key order is
  significant to the game-side Newtonsoft reader.
- **Never resample an index map (biome, material) with anything but
  nearest-neighbour.** Any smooth filter invents values that map to no material.
- **Never ship the editor bridge plugin inside a mod.** Run `uninstall_bridge`
  before publishing.
