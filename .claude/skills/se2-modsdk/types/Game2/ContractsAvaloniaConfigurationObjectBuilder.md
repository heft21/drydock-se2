# ContractsAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Contracts.ContractsAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Contracts`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AbandonContractDialog` | Dialog shown when the player wants to abandon their active contract |
| `AbandonTextKey` | Abandon text to be shown for the button when |
| `AcceptContractDialog` | Dialog shown when the player wants to accept a contract |
| `AcceptContractWarningDialog` | Dialog shown when the player wants to accept a contract, but they have an active contract that will be abandoned |
| `AcceptTextKey` | Accept text to be shown for ... |
| `CompleteTextKey` | Complete text to be shown for the button when |
| `ContractProgressRewardIcon` | Icon of a sector progress reward |
| `ContractProgressRewardText` | Loc key shown for a sector progress reward |
| `EndlessContractsAvailableText` | Text shown when the player has endless contracts available. |
| `EndlessContractsAvailableTitle` | Title shown when the player has endless contracts available. |
| `GetRewardsTextKey` | Get the Rewards text to be shown for the button when |
| `LocationTextKey` | The location text to be shown for the selected contract |
| `OnCollectRewardAudio` | Audio that is played when a contract reward is collected. One shot |
| `OnFailAudio` | Audio that is played when a contract is failed. One shot |

## A real one

`Vanilla\Assets\MainMenuData\UI\Terminal\ContractsAvaloniaConfiguration.def`

```json
{
  "Guid": "f725a612-0545-4917-90be-e829d0540499",
  "LocationTextKey": "ContractsScreenLocation",
  "AcceptTextKey": "ContractsScreenAccept",
  "AbandonTextKey": "ContractsScreenAbandon",
  "CompleteTextKey": "ContractsScreenComplete",
  "FocusTextKey": "ContractsScreenFocus",
  "UnfocusTextKey": "ContractsScreenUnfocus",
  "GetRewardsTextKey": "ContractsScreenGetRewards",
  "ContractProgressRewardText": "RewardSectorProgress",
  "EndlessContractsAvailableTitle": "EndlessContractsAvailableTitle",
  "EndlessContractsAvailableText": "EndlessContractsAvailableText",
  "ContractProgressRewardIcon": "{G}a6746f68-9bf6-4165-a5d7-6c1861e2786f",
  "AbandonContractDialog": "01d38209-b8bf-4e1c-baf0-2d5c074e7e58",
  "AcceptContractDialog": null,
  "AcceptContractWarningDialog": null,
  "OnCollectRewardAudio": "event:/UI/contract_reward_claim",
  "OnFailAudio": "event:/UI/contract_fail"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractsAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='ContractsAvaloniaConfigurationObjectBuilder')
```
