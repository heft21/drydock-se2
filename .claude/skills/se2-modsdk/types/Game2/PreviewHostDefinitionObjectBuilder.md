# PreviewHostDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.PreviewHostDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorPreviewPrefab` | Armor block prefab to use as base when previewing armor blocks |
| `BlockPreviewPrefab` | Block prefab to use as base when previewing regular blocks |
| `BreakableBlockPreviewPrefab` | Breakable block prefab to use as base when previewing breakable blocks |
| `GridPreviewPrefab` | The grid prefab to use as the base when previewing blocks |
| `Projection` | Specify projection settings affecting how the previewed block is displayed |

## A real one

`Vanilla\Assets\System\BlockPlacer\Projections\ProjectionHost.def`

```json
{
  "Guid": "7173bda9-536d-4369-a8e8-831e6a1c3d23",
  "GridPreviewPrefab": "6bbfc03c-fb12-414c-853b-bb8ecda3738d",
  "ArmorPreviewPrefab": "5a70d0d2-49b4-42d2-b71e-d05ddb5a87f3",
  "BreakableBlockPreviewPrefab": "0827588b-a59f-4cd8-8bf2-9d42cd33498e",
  "BlockPreviewPrefab": "9ea34004-3b3b-44b5-ae71-e02104ae3a8e",
  "Projection": "f8c3151f-0cc8-4ab4-b449-74b3fc2560ef"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PreviewHostDefinitionObjectBuilder')
search_content('', type_contains='PreviewHostDefinitionObjectBuilder')
```
