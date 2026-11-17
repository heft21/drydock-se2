# CharacterLifeComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterLifeComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HealthStat` | Character stat to use for tracking health points |
| `RespawnDamageSource` | Damage source applied when the player requests respawn |

## A real one

`Vanilla\Assets\Characters\System\CharacterLifeComponentDefinition.def`

```json
{
  "Guid": "625e33d2-6a4e-406a-926b-81ca7821b110",
  "HealthStat": "3a40976e-7f57-46ea-a1a3-4d8124722e04",
  "RespawnDamageSource": "d64ff48e-b20b-40c9-a45d-b1db2cc952dd"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterLifeComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterLifeComponentDefinitionObjectBuilder')
```
