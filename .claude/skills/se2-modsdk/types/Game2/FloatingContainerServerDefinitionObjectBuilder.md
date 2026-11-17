# FloatingContainerServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FloatingContainerServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TimeToDespawn` | Default time to despawn the container without any player interacting with it |

## A real one

`Vanilla\Assets\Items\System\Floating Objects\FloatingContainers\BackpackServerDefinition.def`

```json
{
  "Guid": "ad97864e-19e0-4df8-a8c2-cc1ef80046fd",
  "TimeToDespawn": 300000000,
  "GpsOffset": {
    "X": 0,
    "Y": 1.2,
    "Z": 0.25
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloatingContainerServerDefinitionObjectBuilder')
search_content('', type_contains='FloatingContainerServerDefinitionObjectBuilder')
```
