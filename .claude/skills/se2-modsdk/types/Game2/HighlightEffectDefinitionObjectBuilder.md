# HighlightEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.HighlightEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Color` | Color of the highlight effect |
| `StrobePeriod` | Period of the strobe effect. If 0 the effect is constant. |

## A real one

`Vanilla\Assets\System\UseActions\DefaultHighlight.def`

```json
{
  "Guid": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "Color": {
    "PackedValue": 218169343
  },
  "StrobePeriod": 3
}
```

Others: `DefaultHighlight_V2`

---

Read it with the MCP server rather than by hand:

```
describe_type('HighlightEffectDefinitionObjectBuilder')
search_content('', type_contains='HighlightEffectDefinitionObjectBuilder')
```
