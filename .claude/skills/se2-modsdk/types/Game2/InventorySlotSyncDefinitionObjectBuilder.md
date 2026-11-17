# InventorySlotSyncDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Items.InventorySlotSyncDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Items`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Battery_InventorySlotSyncDefinition.def`

```json
{
  "Guid": "dbf8bb24-b864-46cd-bfa6-b219a13283ab",
  "SlotDefinition": "f095ac17-cbba-4e10-bf7f-bb9cff5db4c4",
  "SlotDummy": "0dd8466e-8e44-4ebf-93de-218954b34f43"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventorySlotSyncDefinitionObjectBuilder')
search_content('', type_contains='InventorySlotSyncDefinitionObjectBuilder')
```
