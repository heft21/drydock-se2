# GridDecalsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeGrids.GridDecalsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockFixDecalFadeOutTime` | How much time it takes for decals to fade out once a block is fixed |

## A real one

`Vanilla\Assets\System\Decals\GridDecalsConfiguration.def`

```json
{
  "Guid": "be9a3a65-c591-431e-85b4-01e3dae81914",
  "BlockFixDecalFadeOutTime": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridDecalsConfigurationObjectBuilder')
search_content('', type_contains='GridDecalsConfigurationObjectBuilder')
```
