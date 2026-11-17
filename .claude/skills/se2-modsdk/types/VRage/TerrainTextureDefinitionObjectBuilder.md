# TerrainTextureDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.Surface.TerrainTextureDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet.Surface`
- definitions using it: **84**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HeightMap` | Bitmap containing height information. |
| `MaterialMap` | Bitmap containing material assignments. |
| `PlanetHeightmap` | Bitmap containing height information. |
| `PlanetMaterialMap` | Bitmap containing material assignments. |

## A real one

`Vanilla\Assets\Environment\Planets\EarthLike\Dunes.def`

```json
{
  "Guid": "b8645f7c-b32f-4c5d-b367-d063c0c7c524",
  "HeightMap": "{G}ea6e2b80-c505-4758-866d-dd0f401dd2a1",
  "MaterialMap": null,
  "PlanetHeightmap": "{G}85cf28ac-f0c1-4215-9610-6f870b906be7",
  "PlanetMaterialMap": null
}
```

Others: `Waves`, `MarsLikeDunes`

---

Read it with the MCP server rather than by hand:

```
describe_type('TerrainTextureDefinitionObjectBuilder')
search_content('', type_contains='TerrainTextureDefinitionObjectBuilder')
```
