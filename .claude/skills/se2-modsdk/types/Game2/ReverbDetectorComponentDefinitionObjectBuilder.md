# ReverbDetectorComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Audio.ReverbDetectorComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Audio`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectorCollisionLayers` | Collision layers when probing for hits (grids and voxels) |
| `UseHemisphere` | When true, adds extra upper-hemisphere probe directions (y=2 layer) on top of the standard 26 sphere directions, for denser sampling above the gravity equator. Total directions: 35. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\ReverbDetectorComponentDefinition.def`

```json
{
  "Guid": "a2277c32-12f2-431c-a6e4-693b8cd86a0a",
  "DetectorCollisionLayers": "d971c9a7-41af-4c07-8560-03b3216af3cc",
  "UseHemisphere": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ReverbDetectorComponentDefinitionObjectBuilder')
search_content('', type_contains='ReverbDetectorComponentDefinitionObjectBuilder')
```
