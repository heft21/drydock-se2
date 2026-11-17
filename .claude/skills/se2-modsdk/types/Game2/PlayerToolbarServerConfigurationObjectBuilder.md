# PlayerToolbarServerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Toolbars.PlayerToolbarServerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Toolbars`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultToolbar` | The default state of a new player toolbar |

## A real one

`Vanilla\Assets\System\Configurations\PlayerToolbarServerConfiguration.def`

```json
{
  "Guid": "5dc2d2a1-e0fb-4e22-994c-8b0d37e18988",
  "DefaultToolbar": "e8d99ac4-9d4d-48b3-88df-1548cbc04c28"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlayerToolbarServerConfigurationObjectBuilder')
search_content('', type_contains='PlayerToolbarServerConfigurationObjectBuilder')
```
