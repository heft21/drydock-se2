# CubeBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockKind` | Represents block type |
| `CreativeOnly` | Should this block be accessible in survival mode? |
| `DeformationResistance` | How susceptible is the block to getting deformed when damaged. Values 0-1, 1 = cannot be deformed. |
| `Density` | Settings used for computing the block's mass relative to its size in occupied cells. |
| `DestructionThreshold` | Threshold of the block health percent under which block destruction should occur |
| `DisplaySizeOverride` | Explicit block size suffix for specially shaped blocks. |
| `Fragility` | Block fragility, used for computing it's maximum HP based on it's mass. MaxHP = Fragility * Mass (calculated from and number of occupied cell) |
| `InitialBuildProgress` | BuildProgress of the block when initially spawned or materialized |
| `MountPointGeneratorSettings` | Mount point generation settings |
| `MountPointsGroupsPerDirection` | per Groups are expected to be sorted by mount point priority and will be used depending on their order. |
| `PCU` | Performance Cost Unit of the block |
| `Permeability` | If a block is permeable or hollow |
| `PlacerDefinition` | Optional settings for modifying how the block is placed |
| `Recipe` | Proportions and criticality of items from which the final recipe of the block is generated. |
| `RecipeEfficiency` | Efficiency of the block's recipe, the lower its coefficient, the less items will be required by the block's recipe. |
| `UIData` | Contains data for displaying the block in UI. |
| `WeakThreshold` | Threshold of build progress percent under which the should be applied to the block's |
| `WeaknessMultiplier` | Multiplier to apply to the block's when the block's build progress is still below . This is used to make the block have less hit points while it's still under construction. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\CubeBlockDefinition.def`

```json
{
  "Guid": "7a42329a-5745-4dd0-b423-a407347923dd",
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
  "Fragility": null,
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
describe_type('CubeBlockDefinitionObjectBuilder')
search_content('', type_contains='CubeBlockDefinitionObjectBuilder')
```
