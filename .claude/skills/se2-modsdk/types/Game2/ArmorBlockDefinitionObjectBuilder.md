# ArmorBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Armors.ArmorBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Armors`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BuildProgressSkins` | Skins to display for each build stage of the block (shows visual build progress to the player) |
| `Model` | Model used to render this armor block |
| `Skin` | Skin used to render this armor block - can be used to differentiate between different armor types like heavy/light |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\HeavyArmorBlockDefinition.def`

```json
{
  "Guid": "d04f8368-c3f4-4dae-a5d2-68f7760a01c3",
  "Model": null,
  "Skin": "738a1c90-5523-49b2-a79b-6cf4ea9e6ccc",
  "BuildProgressSkins": []
}
```

Others: `LightArmorBlockDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ArmorBlockDefinitionObjectBuilder')
search_content('', type_contains='ArmorBlockDefinitionObjectBuilder')
```
