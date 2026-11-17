# EntityLayerConfigurationObjectBuilder

`VRage:Keen.VRage.Core.Game.Definitions.EntityLayerConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LayerPairInteraction` | Specifies the type of interaction between entities from different layers. |
| `Layers` | A distinct set of all available entity layer names. |

## A real one

`Engine\Assets\Configurations\EntityLayerConfiguration.def`

```json
{
  "Guid": "26c13b1c-1a54-4a3e-a657-0d1c193fa2bf",
  "Layers": [
    {
      "Key": "1c3171b8-2063-4f0d-a89b-9d05d2e46c0a",
      "Value": "Default"
    }
  ],
  "LayerPairInteraction": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EntityLayerConfigurationObjectBuilder')
search_content('', type_contains='EntityLayerConfigurationObjectBuilder')
```
