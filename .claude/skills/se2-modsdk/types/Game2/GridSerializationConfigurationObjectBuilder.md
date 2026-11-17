# GridSerializationConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.GridSerializationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConnectionTypes` | Defines how connected grids will be handled when creating a blueprint See the connection groups of mechanical blocks |
| `GridPrefab` | Server prefab of a grid entity |

## A real one

`Vanilla\Assets\System\Configurations\GridSerializationConfiguration.def`

```json
{
  "Guid": "2e77e93b-4cea-4fec-af4b-811dc018362d",
  "ConnectionTypes": [
    "262d50d2-7b5b-4939-a81b-70f731d0e252"
  ],
  "GridPrefab": "672d6382-207a-498f-a51c-58b370aa96cb"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridSerializationConfigurationObjectBuilder')
search_content('', type_contains='GridSerializationConfigurationObjectBuilder')
```
