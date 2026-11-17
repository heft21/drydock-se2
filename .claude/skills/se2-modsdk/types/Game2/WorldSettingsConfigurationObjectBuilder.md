# WorldSettingsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.RuntimeSystems.WorldSettings.WorldSettingsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.RuntimeSystems.WorldSettings`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackRemovalTimeout` | Time after which backpack dropped from death character will despawn unless interacted with. |
| `DeadCharacterRemovalTimeout` | Time after which dead character will despawn. |

## A real one

`Vanilla\Assets\System\Configurations\WorldSettingsConfiguration.def`

```json
{
  "Guid": "845734d0-e779-47b3-93aa-9d8e3ed49549",
  "DeadCharacterRemovalTimeout": 3600000000,
  "BackpackRemovalTimeout": 9000000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WorldSettingsConfigurationObjectBuilder')
search_content('', type_contains='WorldSettingsConfigurationObjectBuilder')
```
