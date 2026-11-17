# EncounterPCULimitConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Validations.EncounterPCULimitConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Validations`
- definitions using it: **1**

## What it is

's object builder.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AddStandardDeviation` | Each procedural sector have a probability to spawn an encounter meaning that many sector near each other may spawn encounters. The probability of area with higher density is low but possible. This add the standard deviation X times to get closer to worse case scenario. |
| `Estimate` | Non serialized estimation of the PCU the different system will use. |
| `MaxCargoShipPCU` | Maximum PCU of a single . |
| `MaxContractPCU` | Maximum PCU of a single . |
| `MaxEncounterPCU` | Maximum PCU of a single . |
| `MaxPlanetEncountersPCU` | Maximum PCU of planet encounters spawning around the player. |
| `MaxSpaceEncountersPCU` | Maximum PCU of space encounters spawning around the player. |
| `MaxSpawnerPCU` | Maximum PCU of a single . |
| `MaxTotalCargoShipPCU` | Maximum PCU of cargo ship encounters spawning around the player. |

## A real one

`Vanilla\Assets\System\Configurations\EncounterPCULimitConfiguration.def`

```json
{
  "Guid": "be5c2e6b-68cd-4a37-9833-494da062cdfe",
  "MaxSpawnerPCU": 100000,
  "MaxEncounterPCU": 20000,
  "MaxContractPCU": 50000,
  "MaxCargoShipPCU": 25000,
  "MaxPlanetEncountersPCU": 70000,
  "MaxSpaceEncountersPCU": 70000,
  "MaxTotalCargoShipPCU": 30000,
  "AddStandardDeviation": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterPCULimitConfigurationObjectBuilder')
search_content('', type_contains='EncounterPCULimitConfigurationObjectBuilder')
```
