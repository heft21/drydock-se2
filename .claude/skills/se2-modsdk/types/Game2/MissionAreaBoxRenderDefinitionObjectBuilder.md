# MissionAreaBoxRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Missions.MissionAreaBoxRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Missions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BehindOpacity` | Opacity of the highlight hidden behind objects |
| `DashLength` | Length of the dashes of outline of not visible parts |
| `HighlightColor` | Color used for the highlight area |
| `ThicknessBack` | Thickness of the outline of the not invisible sides |
| `ThicknessFront` | Thickness of the visible outline |

## A real one

`Vanilla\Assets\System\Mission\Triggers\Areas\MissionAreaBoxRenderDefinition.def`

```json
{
  "Guid": "5620d239-2fab-466b-aee1-046c2e24cd62",
  "HighlightColor": {
    "PackedValue": 4278235457
  },
  "BehindOpacity": 0.25,
  "ThicknessFront": 3,
  "ThicknessBack": 1,
  "DashLength": 0.15
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MissionAreaBoxRenderDefinitionObjectBuilder')
search_content('', type_contains='MissionAreaBoxRenderDefinitionObjectBuilder')
```
