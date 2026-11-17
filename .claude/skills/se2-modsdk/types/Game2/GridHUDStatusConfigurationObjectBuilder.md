# GridHUDStatusConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.GridHUDStatusConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EnergyResourceType` | Energy resource type |
| `HydrogenResourceType` | Hydrogen resource type |

## A real one

`Vanilla\Assets\UI\HUD\GridHUDStatusConfiguration.def`

```json
{
  "Guid": "c712f01a-ee82-40cc-ac2b-81f6c0dcd171",
  "EnergyResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "HydrogenResourceType": "a0e12811-7f81-4735-aef4-b74ef0c2d395"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridHUDStatusConfigurationObjectBuilder')
search_content('', type_contains='GridHUDStatusConfigurationObjectBuilder')
```
