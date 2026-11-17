# LootTagDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Loot.LootTagDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Loot`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DebugDisplayName` | Used only while debugging encounter worlds, to display visually on tagged inventory blocks. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Encounter\Loot\Tags\RawLootTagDefinition.def`

```json
{
  "Guid": "773bc576-be19-4f32-8ebc-9cdac8083e58",
  "DebugDisplayName": "Raw"
}
```

Others: `ComponentsLootTagDefinition`, `ItemsNoDatapadLootTagDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('LootTagDefinitionObjectBuilder')
search_content('', type_contains='LootTagDefinitionObjectBuilder')
```
