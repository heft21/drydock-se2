# CargoShipEncounterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.CargoShips.CargoShipEncounterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.CargoShips`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TargetSpeed` | Target speed of the encounter. |

## A real one

`Vanilla\Assets\Templates\Encounters\BaseDefinitions\CargoShipEncounterDefinition.def`

```json
{
  "Guid": "7dc5944f-34c0-44c4-b368-da4ea826c7f9",
  "TargetSpeed": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CargoShipEncounterDefinitionObjectBuilder')
search_content('', type_contains='CargoShipEncounterDefinitionObjectBuilder')
```
