# SoundBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Sound.SoundBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Sound`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AvailableEvents` | List of available sounds |

## A real one

`Vanilla\Assets\Blocks\Sound\25\SoundBlock25_SoundBlockDefinition.def`

Too large to inline. Fields present:

`AvailableEvents`, `Guid`

---

Read it with the MCP server rather than by hand:

```
describe_type('SoundBlockDefinitionObjectBuilder')
search_content('', type_contains='SoundBlockDefinitionObjectBuilder')
```
