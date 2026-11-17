# UseRespawnPointDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseRespawnPointDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivateHomeText` | Localization id of hint text to display when the block is owned but not the current home. Used for setting the home base |
| `ActivatingHomeText` | Localization id of hint text to display when the block is owned, not the current home, and is being activated. |
| `ClaimText` | Localization id of hint text to display when the block is not owned and is not claimed. Used for activating unknown respawn points |
| `ClaimingText` | Localization id of hint text to display when the block is not owned, not claimed, and is being activated. |
| `DeactivateHomeText` | Localization id of hint text to display when the block is owned and is the current home. Used for clearing the home base |
| `DeactivatingHomeText` | Localization id of hint text to display when the block is owned, is the current home, and is being activated. |
| `HoldTime` | Amount of time the interaction must be held for it to complete |
| `UnclaimText` | Localization id of hint text to display when the block is not owned and is claimed. Used for deactivating known respawn points |
| `UnclaimingText` | Localization id of hint text to display when the block is not owned, claimed, and is being activated. |

## A real one

`Vanilla\Assets\System\UseActions\UseRespawnPointDefinition.def`

```json
{
  "Guid": "58383da5-f2ca-499c-a11d-b6d2809ae6fc",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseRespawnPointAction",
  "HighlightText": "BlankUseActionHighlightText",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "ActivateHomeText": "RespawnPointSetHome",
  "DeactivateHomeText": "RespawnPointUnsetHome",
  "ClaimText": "RespawnPointClaim",
  "UnclaimText": "RespawnPointUnclaim",
  "ActivatingHomeText": "RespawnPointSettingHome",
  "DeactivatingHomeText": "RespawnPointUnsettingHome",
  "ClaimingText": "RespawnPointClaiming",
  "UnclaimingText": "RespawnPointUnclaiming",
  "HoldTime": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseRespawnPointDefinitionObjectBuilder')
search_content('', type_contains='UseRespawnPointDefinitionObjectBuilder')
```
