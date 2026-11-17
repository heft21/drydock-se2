# UseActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DepositNonEssentialItems` | Optionally provided depending on . Tries to transfer all non essential items to available inventory of interacted Entity from interactor. |
| `HighlightEffect` | Optional highlight effect to apply on the affected block parts |
| `HighlightText` | Localization id of text to display when the player is targeting the dummy associated to this action |
| `Inflation` | Size offset applied to each dimension of the dummy. Used by conveyors to reduce the number of false-positive hits on conveyors along their edges. |
| `InputContextDefinition` | Input context settings |
| `InteractPrimary` | Input for primary interaction action |
| `InteractSecondary` | Input for secondary interaction action |
| `RequireFacingPlayer` | When true, interaction hits that are facing away from dummy's forward will be ignored. Used to reduce the number of false-positive hits on conveyors. |
| `UseActionType` | The class type of the action to create |
| `WorkWhenDisabled` | If a dummy of this type is on a block that is disabled (powered off, nonfunctional, missing power, etc), the use action won't be created when targeted. Note that this does not affect nonfunctional/destroyed fracture filtering. |

## A real one

`Vanilla\Assets\System\UseActions\UseAction.def`

```json
{
  "Guid": "f49a9b10-fe13-42f5-8bd8-dc32f98c4333",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseAction",
  "HighlightText": "BlankUseActionHighlightText",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657"
}
```

Others: `UseSkinColorChangeAction`

---

Read it with the MCP server rather than by hand:

```
describe_type('UseActionDefinitionObjectBuilder')
search_content('', type_contains='UseActionDefinitionObjectBuilder')
```
