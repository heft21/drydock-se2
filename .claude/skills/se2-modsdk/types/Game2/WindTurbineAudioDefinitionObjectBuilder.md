# WindTurbineAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Production.WindTurbineAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Production`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EfficiencyParameter` | Audio event parameter to transfer the efficiency of the turbine for sound modulation. |
| `EfficiencyParameterMultiplier` | Multiplier for passing value to . |
| `WindTurbineWorkingAudio` | The audio that plays and increases its volume the more effective the wind turbine is. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WindTurbine_Client_WindTurbineAudioDefinition.def`

```json
{
  "Guid": "236aef94-d6ef-4736-99a9-5a1d1444dc72",
  "WindTurbineWorkingAudio": "event:/SFX/Block/WindTurbine",
  "EffectiveVolume": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WindTurbineAudioDefinitionObjectBuilder')
search_content('', type_contains='WindTurbineAudioDefinitionObjectBuilder')
```
