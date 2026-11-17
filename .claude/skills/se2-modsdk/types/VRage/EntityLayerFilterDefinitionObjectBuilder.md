# EntityLayerFilterDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.Definitions.EntityLayerFilterDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.Definitions`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExcludeLayers` | All layers that should be excluded. When used, the filter will includes all layers EXCEPT for the ones listed here |
| `IncludeLayers` | All layers that should be included. When used, the filter will only include the layers listed here |

## A real one

`Vanilla\Assets\System\Grid\CarSafeFromLayers.def`

```json
{
  "Guid": "6bf68baf-0537-4dab-bed3-79e6599d2d42",
  "IncludeLayers": [],
  "ExcludeLayers": [
    {
      "Key": "c6494f7f-0559-4fe0-8d49-31d12a9038e9",
      "Value": "Grids"
    },
    {
      "Key": "5b77dc18-0636-4391-ad8f-cf6d36edcd4e",
      "Value": "HeavyGrids"
    }
  ]
}
```

Others: `SafeFromCarLayers`, `InteractorEntityLayerFilter`

---

Read it with the MCP server rather than by hand:

```
describe_type('EntityLayerFilterDefinitionObjectBuilder')
search_content('', type_contains='EntityLayerFilterDefinitionObjectBuilder')
```
