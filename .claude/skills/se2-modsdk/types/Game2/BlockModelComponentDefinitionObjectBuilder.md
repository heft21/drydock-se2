# BlockModelComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Models.BlockModelComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Models`
- definitions using it: **10**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BuildProgressModels` | Model and material changes that occur during block construction to visually represent the build progress. There is an unlimited amount of construction stages, this means we are able to create great construction progression for our blocks. |
| `DamagedModel` | Model to display when the block is damaged. |
| `DamagedReplacementModels` | Maps a non-damaged model to its damaged version. This is for advanced use cases using multiple models during block construction. The mapping from and to is inferred automatically and does not need to be added here. |
| `FractureReplacementModels` | Maps a non-fractured model to its fractured version This is for advanced use cases using multiple models during block construction. The mapping between and is inferred automatically and does not need to be added here. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BlockModelDefinition.def`

```json
{
  "Guid": "f104e970-bdcc-4a09-892d-8cc96e039998",
  "Model": null,
  "Dummies": [],
  "FractureModel": null,
  "DamagedModel": null,
  "BuildProgressModels": [],
  "DamagedReplacementModels": [],
  "FractureReplacementModels": []
}
```

Others: `Piston150_S1_BlockModelComponentDefinition`, `Piston150_S2_BlockModelComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockModelComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockModelComponentDefinitionObjectBuilder')
```
