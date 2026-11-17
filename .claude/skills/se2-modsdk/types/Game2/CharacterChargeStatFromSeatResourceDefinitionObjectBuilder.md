# CharacterChargeStatFromSeatResourceDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterChargeStatFromSeatResourceDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **3**

## What it is

Object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ChargingStat` | Stat that is recharged |
| `ConsumedResourceType` | What resource to recharge with |
| `ConsumptionPriority` | Priority of resource consumption from the resource distribution system. |
| `MaxChargingRate` | Max rate at which stat can be filled |

## A real one

`Vanilla\Assets\Characters\System\CharacterEnergy.def`

```json
{
  "Guid": "477b915f-48a7-4c93-8039-ffc5130f0793",
  "ChargingStat": "675206d7-7a7a-445c-946c-e0a74bbcd862",
  "ConsumedResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "MaxChargingRate": 50,
  "ConsumptionPriority": {
    "Priority": 7
  }
}
```

Others: `CharacterOxygenRecharging`, `CharacterHydrogenRecharging`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterChargeStatFromSeatResourceDefinitionObjectBuilder')
search_content('', type_contains='CharacterChargeStatFromSeatResourceDefinitionObjectBuilder')
```
