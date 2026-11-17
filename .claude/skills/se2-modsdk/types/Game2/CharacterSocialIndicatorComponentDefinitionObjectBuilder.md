# CharacterSocialIndicatorComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterSocialIndicatorComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\CharacterSocialIndicatorComponentDefinition.def`

```json
{
  "Guid": "5017917f-78cb-4896-a3ac-0c3102680da5",
  "BarWidth": 0.1,
  "BarFrameTexture": "{G}746e40ed-8dce-4b39-a471-cea77cd1a347",
  "BarBackgroundTexture": "{G}4f96c790-1857-4ca1-bac3-44d9bcd67466",
  "BarFillTexture": "{G}a3438b6c-1ce6-401f-9bb1-ee26001fb8e8",
  "BorderColor": {
    "PackedValue": 4294967295
  },
  "BackgroundColor": {
    "PackedValue": 4294967295
  },
  "HealthColor": {
    "PackedValue": 4294967295
  },
  "LowHealthColor": {
    "PackedValue": 4294967295
  },
  "DisplayDuration": 20000000,
  "FadeOutDuration": 5000000,
  "IconSpacing": 0.004,
  "DisconnectedIcon": "{G}3827e898-0796-458a-b246-3a2b9739993b",
  "DisconnectedIconSize": 0.03,
  "MaxDisplayDistance": 100,
  "AnchorDirection": {
    "X": 0,
    "Y": 1,
    "Z": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterSocialIndicatorComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterSocialIndicatorComponentDefinitionObjectBuilder')
```
