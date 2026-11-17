# InventorySlotsServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.InventorySlotsServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SlotDefinition` | Definition of slots that will be synced. Must use |
| `SlotDummy` | Definition of dummy that the slots are attached to |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Battery_InventorySlotsServerDefinition.def`

```json
{
  "Guid": "bfe587b2-2b38-479d-b818-34d5113fb69f",
  "SlotDefinition": "f095ac17-cbba-4e10-bf7f-bb9cff5db4c4",
  "SlotDummy": "0dd8466e-8e44-4ebf-93de-218954b34f43"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventorySlotsServerDefinitionObjectBuilder')
search_content('', type_contains='InventorySlotsServerDefinitionObjectBuilder')
```
