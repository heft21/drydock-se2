# LootTableDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Loot.LootTableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Loot`
- definitions using it: **8**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LootTiers` | Represents all available loot tiers for this table. Each tier is rolled for separatelly and aggregated with other tiers. |

## A real one

`Vanilla\Assets\Characters\Shared\NPC\Loot\LootTables\NPC_InventoryLootTableDatapads.def`

```json
{
  "Guid": "1ac14927-e3e2-4e53-96aa-cc68856eaa89",
  "LootTiers": [
    {
      "Key": "0257a668-d20a-4f17-a94d-a671e8d1ce92",
      "Value": "366881b2-acbc-42d8-b6c1-2c730dd71831"
    }
  ]
}
```

Others: `NPC_InventoryLootTableConsumable`, `NPC_InventoryLootTableDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('LootTableDefinitionObjectBuilder')
search_content('', type_contains='LootTableDefinitionObjectBuilder')
```
