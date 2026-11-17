# WeatherModifierRenderComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Weather.WeatherModifierRenderComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CloudModifier` | How does the effect modifies clouds |
| `EffectTint` | Tint of the effect |
| `FogModifier` | How does the effect modifies fog |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\WeatherModifierRenderComponentDefinition.def`

```json
{
  "Guid": "438f7d53-d080-4ad9-b897-6d267f16be3d",
  "EffectTint": {
    "PackedValue": 0
  },
  "CloudModifier": null,
  "FogModifier": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeatherModifierRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='WeatherModifierRenderComponentDefinitionObjectBuilder')
```
