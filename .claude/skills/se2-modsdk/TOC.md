# Table of contents

## Read in this order for anything new

| page | when |
|---|---|
| [00-orientation.md](reference/00-orientation.md) | **always first** — how content is shaped, and the four traps that cost the most time |
| [01-file-format.md](reference/01-file-format.md) | before writing or editing any `.def` / `.partialdef` / `.meta` |
| [02-project-and-publishing.md](reference/02-project-and-publishing.md) | project setup, dependencies, building, publishing, hash errors |

## By what you are building

| page | covers |
|---|---|
| [03-planets.md](reference/03-planets.md) | generators, height encoding, biome and material maps, ColorKeys, the cube-face basis, `PlanetInfoDefinition` |
| [04-water.md](reference/04-water.md) | planetary water vs massfill domains, why massfill destroys performance, why the editor can never show water, the state of water in the shipped game |
| [05-blocks-and-models.md](reference/05-blocks-and-models.md) | block templates, size and polygon budgets, the shared material library, Blender export, armor, sound |
| [06-voxel-materials.md](reference/06-voxel-materials.md) | the PNG → comptex → triplanar → voxel material chain, and where a material spawns |

## When something is wrong

| page | covers |
|---|---|
| [08-troubleshooting.md](reference/08-troubleshooting.md) | symptom → cause, for the failures that produce no error message |
| [07-tooling.md](reference/07-tooling.md) | the MCP tools, the editor bridge, Blender, Mod HUB, and which log answers which question |

## The generated catalogue

| page | covers |
|---|---|
| [types/index.md](types/index.md) | every `$Type` SE2 content uses, sorted by how many definitions use it |
| `types/<Bundle>/<ShortName>.md` | per-type (the file is named after the type's last name part; the full name heads the page): the SDK's own field documentation, usage count, and a real vanilla file |

Regenerate after a game update:

```bash
python check_version.py       # 0 match, 2 differ
python build_reference.py     # rewrite types/ and sdk_version.txt
```

## The shortest possible summary

- Everything references everything by **bare GUID**. Resolve, do not browse.
- A mod depends on **Vanilla**, patches it with an **Override partialdef**, and
  never edits `GameData`.
- `Assets.meta` must declare a **DefinitionSetItem** or the whole mod is
  silently inert.
- Asset processors run at project **load**, not at build.
- The editor previews assets; it does not run a game session. Some things can
  only be tested in game.
