# PlanetaryGrassWindDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.PlanetaryGrassWindDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AxisSwitchTime` | The time it takes to switch from one projection axis to another |

## A real one

`Vanilla\Assets\System\Camera\PlanetaryGrassWindDefinition.def`

```json
{
  "Guid": "6f887817-2a0b-4a00-b17e-7a7045d42c45",
  "AxisSwitchTime": 30000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetaryGrassWindDefinitionObjectBuilder')
search_content('', type_contains='PlanetaryGrassWindDefinitionObjectBuilder')
```
