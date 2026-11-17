# CharacterLifeSupportComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterLifeSupportComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageCooldown` | The delay period after taking damage before the player starts healing. |
| `DontKillCharacter` | Characters won't die on lack of resources when this flag is set |
| `HealRate` | How much the player's health stat changes per second when emergency healing. |
| `LifeSupportStats` | Stats consumed over time. When absent, character gets damage over time |
| `MinHealth` | Target health ratio the emergency healing will progress to. If the health is greater than this value, the player will not heal. The player must have all stats to heal with life support To disable the healing, set to 0. |

## A real one

`Vanilla\Assets\Characters\System\LifeSupport.def`

```json
{
  "Guid": "00da143c-80aa-4695-ad28-a4ff7646bdbc",
  "LifeSupportStats": [
    {
      "Key": "3af865ce-de4c-4d83-9815-f2dd247b4240",
      "Value": {
        "Stat": "675206d7-7a7a-445c-946c-e0a74bbcd862",
        "Consumption": 0.095,
        "DamageWhenAbsent": 3.33,
        "ConditionalStat": null,
        "DamageSource": "d96d2397-2444-4d7e-88ff-23f24329ca94"
      }
    },
    {
      "Key": "6b794cab-047d-43d9-94e9-70c50b94fd88",
      "Value": {
        "Stat": "c162f32f-75ab-4d17-8a49-696dc6caf1ff",
        "Consumption": 0.05,
        "DamageWhenAbsent": 3.33,
        "ConditionalStat": null,
        "DamageSource": "e83fade3-02d3-4a32-a855-cbae4094b437"
      }
    }
  ],
  "DontKillCharacter": false,
  "DamageCooldown": 100000000,
  "MinHealth": 0.2,
  "HealRate": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterLifeSupportComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterLifeSupportComponentDefinitionObjectBuilder')
```
