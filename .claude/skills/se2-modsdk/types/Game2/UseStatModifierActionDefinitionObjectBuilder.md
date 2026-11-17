# UseStatModifierActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseStatModifierActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FallbackTitle` | Title of hint used when there is no overriding name (like block name) |

## A real one

`Vanilla\Assets\System\UseActions\UseHealingDeviceDefinition.def`

```json
{
  "Guid": "7f2face5-7cac-4c07-87ad-dd6fc5def50b",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseStatModifierAction",
  "HighlightText": "MedicalRoomHealHint",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "FallbackTitle": "MedicalRoomHealTitleFallback",
  "LoopAudio": "event:/SFX/Tool/PaintTool",
  "StartAudio": "event:/UI/ColorTool_menu_appear",
  "StopAudio": "event:/UI/ColorTool_menu_disappear"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseStatModifierActionDefinitionObjectBuilder')
search_content('', type_contains='UseStatModifierActionDefinitionObjectBuilder')
```
