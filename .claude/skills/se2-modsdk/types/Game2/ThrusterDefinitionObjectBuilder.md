# ThrusterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Movement.ThrusterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Movement`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ResourcesRequiredToThrust` | Additional resources of the type of the block's that are required for the thruster to thrust. Is null, or there is no , this is ignored. |
| `ThrustClass` | The thruster class ID that is defined in |
| `ThrustDirection` | The relative direction in which the block will be moved by the thrust |
| `ThrustPower` | Maximum thrust that the block can deliver |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\IonThrusterDefinition.def`

```json
{
  "Guid": "fb85a823-f1d5-402e-a1e6-fec53125585c",
  "ThrustPower": 10000,
  "ThrustDirection": "Forward",
  "ThrustClass": "Ion"
}
```

Others: `HydrogenThrusterDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ThrusterDefinitionObjectBuilder')
search_content('', type_contains='ThrusterDefinitionObjectBuilder')
```
