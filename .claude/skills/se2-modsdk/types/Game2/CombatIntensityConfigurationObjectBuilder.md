# CombatIntensityConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.CombatIntensityConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\CombatIntensityConfiguration.def`

```json
{
  "Guid": "9330b387-b6a5-4124-a806-033e95e5e03f",
  "MaxMusicDistance": 50
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CombatIntensityConfigurationObjectBuilder')
search_content('', type_contains='CombatIntensityConfigurationObjectBuilder')
```
