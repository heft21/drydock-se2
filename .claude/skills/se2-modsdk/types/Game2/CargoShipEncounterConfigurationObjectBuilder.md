# CargoShipEncounterConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.CargoShips.CargoShipEncounterConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.CargoShips`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Definition` | Default definition to use in new worlds. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Encounter\CargoShipEncounterConfiguration.def`

```json
{
  "Guid": "0206a6f8-d788-4925-85b1-d3c7748cfa14",
  "Definition": "dda619d9-d9eb-430a-8eb1-62f299150a9d"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CargoShipEncounterConfigurationObjectBuilder')
search_content('', type_contains='CargoShipEncounterConfigurationObjectBuilder')
```
