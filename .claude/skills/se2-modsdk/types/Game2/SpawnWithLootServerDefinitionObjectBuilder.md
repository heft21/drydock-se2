# SpawnWithLootServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Loot.SpawnWithLootServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Loot`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\GenericNPC\GenericNPC_SpawnWithConsumable.def`

```json
{
  "Guid": "632981b0-79cc-4390-86cf-2b44944b2cb4",
  "LootTable": "6db9434e-bbe4-4d69-b59b-1644c75ffa46",
  "InventoryTag": "ConsumableInventory"
}
```

Others: `GenericNPC_SpawnWithLootDatapads`, `GenericNPC_SpawnWithLootServerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SpawnWithLootServerDefinitionObjectBuilder')
search_content('', type_contains='SpawnWithLootServerDefinitionObjectBuilder')
```
