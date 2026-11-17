# FunctionalBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.FunctionalBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\FunctionalBlockDefinition.def`

```json
{
  "Guid": "ea3505ef-f162-4e25-8af3-eba6e68a186a",
  "UIData": {
    "Name": "",
    "Icon": "{G}f07eda89-27f7-4d23-8073-00b72b3e7397"
  },
  "PlacerDefinition": null,
  "MountPointGeneratorSettings": {
    "Enabled": true,
    "Sampler": "Circular8",
    "Directions": "All"
  },
  "MountPointsGroupsPerDirection": {},
  "Density": null,
  "Fragility": "eaaa3a8d-d04c-461f-a7f5-00e8cabd27bd",
  "DisplaySizeOverride": null,
  "Permeability": false,
  "DeformationResistance": 0.9,
  "DestructionThreshold": 0.3,
  "WeakThreshold": 0.8,
  "WeaknessMultiplier": 0.8,
  "Recipe": null,
  "RecipeEfficiency": null,
  "BlockKind": null,
  "PCU": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FunctionalBlockDefinitionObjectBuilder')
search_content('', type_contains='FunctionalBlockDefinitionObjectBuilder')
```
