# CombatMusicConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.AI.CombatMusicConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.AI`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\CombatMusicConfiguration.def`

```json
{
  "Guid": "e2a283cd-7836-4a60-8ea1-d62ef5cc78d5",
  "Playlist": "ab68bd9f-3578-4604-a7af-21154a4e1ee9",
  "IntensityToAmount": {
    "None": 0,
    "Anonymous": 0.25,
    "Identified": 0.5,
    "Engaging": 1
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CombatMusicConfigurationObjectBuilder')
search_content('', type_contains='CombatMusicConfigurationObjectBuilder')
```
