# PlanetBiomeMapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetBiomeMapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **8**

## What it is

Migration part of the planet biome map definition.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BiomeMap` | A map of the planet's surface and underground biomes, generated from a cubemap texture set. |
| `MaterialMap` | A map of the planet's materials, generated from a cubemap texture set. |
| `MinimumSurfaceLayerDepth` | Specifies the minimum surface biome depth for all materials placement rules inside the . |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\BiomeMap.def`

```json
{
  "Guid": "e3af2751-aef7-4647-8d0e-854bfbf673dc",
  "BiomeMap": "eedd617f-27ee-4ac3-b70b-fed84c3d1f1a",
  "MaterialMap": "5d93b7fc-1e7b-47b8-9454-5f4da461e1e2",
  "MinimumSurfaceLayerDepth": 5
}
```

Others: `Byblos_BiomeMap`, `Verdure_BiomeMap`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetBiomeMapDefinitionObjectBuilder')
search_content('', type_contains='PlanetBiomeMapDefinitionObjectBuilder')
```
