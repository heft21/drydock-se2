# MechanicalBlockCounterpartAlignmentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockCounterpartAlignmentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignOppositeFacing` | If true, aligns the blocks so that their pivots face each other, i.e. have opposite forward (Z) vectors. If false, aligns the blocks so that their pivots face the same direction. |
| `MaxAlignmentAcceleration` | Maximum acceleration applied when aligning. |
| `MaxAlignmentSpeed` | The maximum speed at which to try to align. This is an abstract unit, not precisely equivalent to speed, but it can be thought of as being roughly in m/s. |
| `PhysicalConnectionGroup` | Connection group definition used to isolate the subgraph of physically connected entities in the grid graph. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MechanicalBlockCounterpartAlignmentDefinition.def`

```json
{
  "Guid": "1e9b1680-3982-4083-b1d1-ad15651e8ddc",
  "MaxAlignmentAcceleration": 5,
  "MaxAlignmentSpeed": 10,
  "AlignOppositeFacing": true,
  "PhysicalConnectionGroup": "262d50d2-7b5b-4939-a81b-70f731d0e252"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockCounterpartAlignmentDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockCounterpartAlignmentDefinitionObjectBuilder')
```
