# CubeBlockDensityDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockDensityDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MassCurveModifier` | The value computed from the block volume (number of occupied cells) will be multiplied by this value to compute the final mass. |

## A real one

`Vanilla\Assets\Blocks\Shared\Density\Solid.def`

```json
{
  "Guid": "0177a842-4cd2-4318-963a-900824601d83",
  "MassCurveModifier": 35
}
```

Others: `Hollow`, `Mostly Solid`

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockDensityDefinitionObjectBuilder')
search_content('', type_contains='CubeBlockDensityDefinitionObjectBuilder')
```
