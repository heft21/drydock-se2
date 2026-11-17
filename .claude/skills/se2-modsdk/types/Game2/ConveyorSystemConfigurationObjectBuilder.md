# ConveyorSystemConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.ResourceDistribution.Conveyors.ConveyorSystemConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.ResourceDistribution.Conveyors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConveyorConnectionTypes` | List of connection groups that can establish valid connections to conveyor nodes |
| `InteractableDummies` | List of dummies that can be used to access the conveyor nodes (e.g. inventory) |
| `PipeableDummies` | List of dummies that can be used to connect conveyor tubes |
| `UniversalAccessDummies` | List of dummies that can be used to access the conveyor nodes despite not being part of ConveyorSystem (Terminal) |

## A real one

`Vanilla\Assets\System\GridConveyorSystem.def`

```json
{
  "Guid": "0493bcd4-feec-4a8e-a4f8-d10dd86e1582",
  "PipeableDummies": [
    "e4203734-4c68-4490-a77e-7e299ad6839d",
    "29d45e5b-2ddf-4ba5-9031-885260550947"
  ],
  "InteractableDummies": [
    "29d45e5b-2ddf-4ba5-9031-885260550947",
    "18ebca70-b1ac-46e0-9965-a3dc257a21b4",
    "51c3b94d-e1fa-4d52-8dd9-2acd162f2c9c"
  ],
  "UniversalAccessDummies": [
    "b15d441f-88d0-4722-a377-7adfd75579e7",
    "c39b2ab3-7191-4279-82f8-d9dcd5271b84",
    "25e5525b-ad06-487f-b585-96c7a550c64e"
  ],
  "ConveyorConnectionTypes": [
    "a5bd777b-b184-41c9-af22-284d7178c267"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConveyorSystemConfigurationObjectBuilder')
search_content('', type_contains='ConveyorSystemConfigurationObjectBuilder')
```
