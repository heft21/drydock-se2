# GridControlConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.GridControlConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LightToggleTag` | Tag of components used for toggling Lights on and off. |

## A real one

`Vanilla\Assets\System\Configurations\GridControlConfiguration.def`

```json
{
  "Guid": "19218fd2-9043-4ac8-b566-039e8a161890",
  "LightToggleTag": "TOGGLE_LIGHTS"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridControlConfigurationObjectBuilder')
search_content('', type_contains='GridControlConfigurationObjectBuilder')
```
