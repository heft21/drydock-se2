# CubeGridConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.CubeGridConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ShipConnectionType` | Special connection type used to identify connections between grids that form part of a ship. Specifically, it refers to connections made by mechanical blocks like Pistons, Rotors, Hinges, Landing Gears, and Connectors, which are considered persistent connections in a ship’s structure. |

## A real one

`Vanilla\Assets\System\Configurations\GridConfiguration.def`

```json
{
  "Guid": "abe1112a-faae-45f6-ba21-14510c79d475",
  "ShipConnectionType": "2ed2d414-fedb-42a2-bc75-2b26417e1346"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeGridConfigurationObjectBuilder')
search_content('', type_contains='CubeGridConfigurationObjectBuilder')
```
