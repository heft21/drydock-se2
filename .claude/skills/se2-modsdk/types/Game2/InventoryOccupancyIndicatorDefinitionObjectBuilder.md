# InventoryOccupancyIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Items.InventoryOccupancyIndicatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Items`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Blocks\Contracts\ContractsTerminal\250\ContractBlock250_InventoryOccupancyIndicatorDefinition.def`

```json
{
  "Guid": "00b15be7-3adc-4454-8383-1512cb06ffbd",
  "Highlight": null,
  "Dummy": "18ebca70-b1ac-46e0-9965-a3dc257a21b4",
  "ParticleEffect": "5f4cad6b-8e1a-4b3d-8f9c-4a5b6c7d8e9f",
  "ParticleEffectScale": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryOccupancyIndicatorDefinitionObjectBuilder')
search_content('', type_contains='InventoryOccupancyIndicatorDefinitionObjectBuilder')
```
