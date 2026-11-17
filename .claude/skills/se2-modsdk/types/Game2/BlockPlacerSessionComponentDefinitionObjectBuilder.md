# BlockPlacerSessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlockPlacerSessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignmentMode` | The default value of when starting the game. |
| `InitialGridVelocity` | The default value of when starting the game. |
| `SubgridProjectionsNotification` | Notification shown when the player is attemping to load a grid that contains subgrids in survival |

## A real one

`Vanilla\Assets\System\BlockPlacer\DefaultBlockPlacerSession.def`

```json
{
  "Guid": "1d1b914a-c610-41d3-a40d-718de5230d96",
  "InitialGridVelocity": 0,
  "AlignmentMode": "FreeAlign",
  "SubgridProjectionsNotification": "d151e9b4-88b5-49ce-ac1b-838235a16c06"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacerSessionComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockPlacerSessionComponentDefinitionObjectBuilder')
```
