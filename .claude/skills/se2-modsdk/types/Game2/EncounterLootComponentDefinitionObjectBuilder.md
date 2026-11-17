# EncounterLootComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Loot.EncounterLootComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Loot`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LootTables` | Represents an association between a loot tag and a specific loot table. Inventories associated by this tag in the encounter will have their loot generated from the associated table. |

## A real one

`Vanilla\Assets\Templates\Encounters\BaseDefinitions\EncounterLootComponentBaseDefinition.def`

```json
{
  "Guid": "4ae73ed6-a0ad-4a1b-b390-1ca2d3019808",
  "LootTables": {}
}
```

Others: `EncounterLootComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterLootComponentDefinitionObjectBuilder')
search_content('', type_contains='EncounterLootComponentDefinitionObjectBuilder')
```
