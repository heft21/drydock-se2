# MechanicalBlockTopTypeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockTopTypeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\MechanicalBlockTopTypes\HingeTop.def`

```json
{
  "Guid": "1a87027d-8857-4cc8-9b16-bef26d04a1fd"
}
```

Others: `RotorTop`, `PistonTop`

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockTopTypeDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockTopTypeDefinitionObjectBuilder')
```
