# TileCoverageMapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.Surface.TileCoverageMapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet.Surface`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PlanetTexture` | Texture containing the tilemap information. |
| `Texture` | Texture containing the tilemap information. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\Planets\DefaultTileCoverageMap.def`

```json
{
  "Guid": "4faac13d-2621-48ff-9440-8de67824d248",
  "Texture": "{G}ba51ef4c-313d-485c-aa0e-3a3d2da18406",
  "PlanetTexture": "{G}3c885957-b81e-4356-a695-c6f08af95822"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TileCoverageMapDefinitionObjectBuilder')
search_content('', type_contains='TileCoverageMapDefinitionObjectBuilder')
```
