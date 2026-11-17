# TimerBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar.TimerBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DurationMax` | Maximum duration length |
| `DurationMin` | Minimum duration length |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\TimerBlockDefinition.def`

```json
{
  "Guid": "e633db51-59de-4229-903c-1bf7e712b487",
  "DurationMin": 0,
  "DurationMax": 36000000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TimerBlockDefinitionObjectBuilder')
search_content('', type_contains='TimerBlockDefinitionObjectBuilder')
```
