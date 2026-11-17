# AreaIntegrityToolEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.Effects.AreaIntegrityToolEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DashLength` | Length of the dashes of outline of not visible parts |
| `FillOpacity` | Opacity of the highlight fill |
| `HighlightColor` | Color used for the highlight of blocks |
| `ThicknessBack` | Thickness of the outline of the not invisible sides |
| `ThicknessFront` | Thickness of the visible outline |

## A real one

`Vanilla\Assets\CharacterTools\HandWelders\AreaWelderMk1\AreaWelderMk1_Client_AreaIntegrityToolEffectDefinition.def`

```json
{
  "Guid": "6eb33921-9c7c-4355-a7af-c4b8e4218e44",
  "HighlightColor": {
    "PackedValue": 4294945280
  },
  "FillOpacity": 0.25,
  "ThicknessFront": 3,
  "ThicknessBack": 2,
  "DashLength": 0.25
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AreaIntegrityToolEffectDefinitionObjectBuilder')
search_content('', type_contains='AreaIntegrityToolEffectDefinitionObjectBuilder')
```
