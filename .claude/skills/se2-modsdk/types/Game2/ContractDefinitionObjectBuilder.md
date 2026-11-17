# ContractDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.ContractDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **50**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockRewards` | Block group to unlock. |
| `CompletionDescription` | Lore description shown on contract completion. |
| `CompletionImage` | Image shown on the contract completion screen. |
| `CompletionVideo` | Optional video to play when the completion screen is closed. |
| `ContractImage` | Image used by this contract |
| `CreditsReward` | Credits awarded to player on success. |
| `Description` | Contract description. |
| `GiverAvatar` | Avatar image for the contract giver. |
| `GiverName` | Name of the contract giver. |
| `ItemRewards` | Items added to contract block inventory on success. |
| `MinimumContractCompletedAmount` | Minimum number of contract completed on this block to become available. |
| `MinimumStage` | Minimum sector stage required for contract to become available. |
| `RequiredContractCompleted` | Specific contracts that must be completed to become available. |
| `StampIcon` | Stamp/seal icon for contract completion. |
| `Tags` | Tags associated with this contract. Allows contracts to be filtered when generating contract lists. |
| `Title` | Title of the contract. |
| `UpgradeColonization` | Increase on success. |

## A real one

`Vanilla\Assets\Templates\Contracts\BaseDefinitions\ContractDefinition.def`

```json
{
  "Guid": "8d7dff1f-b191-4f7c-a098-1251ee6172e6",
  "Title": "",
  "Description": "",
  "ContractImage": null,
  "Tags": [],
  "ColonizationProgress": 0,
  "ItemRewards": [],
  "CreditsReward": 0,
  "MinimumProgress": 0,
  "GiverAvatar": "{G}b4fe9adc-a214-4bd2-bae5-348d04a011bb",
  "GiverName": "ColonisationAuthority",
  "CompletionImage": "{G}0feaebbf-2e67-40db-9789-b02b80989214",
  "CompletionDescription": "ContractsCompleteDescription",
  "StampIcon": "{G}0422be47-af68-4127-982d-46e2aafdf438"
}
```

Others: `NPCDemoEncounter_ContractDefinition`, `bounty6_ContractDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractDefinitionObjectBuilder')
search_content('', type_contains='ContractDefinitionObjectBuilder')
```
