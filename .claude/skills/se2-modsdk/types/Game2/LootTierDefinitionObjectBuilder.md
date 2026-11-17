# LootTierDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Loot.LootTierDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Loot`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Items` | List of actual available loot item stacks to spawn. |
| `MaxItemPicks` | Maximum times a loot item will be picked from the table specified in If the same item is picked multiple times, stacks are aggregated. |
| `MaxStage` | Maximum inclusive required sector stage for this tier to be valid. If the encounter is outside of sectors, it is always valid. If null allows any stage at or after the . |
| `MinItemPicks` | Minimum times a loot item will be picked from the table specified in If the same item is picked multiple times, stacks are aggregated. |
| `MinStage` | Minimum inclusive required sector stage for this tier to be valid. If the encounter is outside of sectors, it is always valid. If null allows any stage at or before the . |
| `NoItemProbability` | All item probabilities are relative to each other. If we want a chance of a pick resulting in nothing, we want to define a no-item probability too. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Loot\RareLootTierTemplate.def`

```json
{
  "Guid": "dc6275ae-df45-4566-ae0a-105481940acf",
  "MinProgression": 0.5,
  "MaxProgression": 1,
  "MinItemPicks": 0,
  "MaxItemPicks": 2,
  "NoItemProbability": 0.3,
  "Items": []
}
```

Others: `CommonLootTierTemplate`, `UnCommonLootTierTemplate`

---

Read it with the MCP server rather than by hand:

```
describe_type('LootTierDefinitionObjectBuilder')
search_content('', type_contains='LootTierDefinitionObjectBuilder')
```
