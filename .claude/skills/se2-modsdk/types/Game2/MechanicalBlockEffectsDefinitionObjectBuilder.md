# MechanicalBlockEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AudioStateAligning` | Parameter value to send to when aligning |
| `AudioStateConnect` | Parameter value to send to when connected |
| `AudioStateDisconnect` | Parameter value to send to when disconnected |
| `AudioStateParameter` | Parameter to send to to change audio state |
| `AudioStateReadyToConnect` | Parameter value to send to when ready to connect |
| `BlockAudio` | Audio event to play on mechanical block state change |
| `OnDisconnectParticleEffect` | Particle effect to spawn when the mechanical block disconnects from a counterpart. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Connectors_MechanicalBlockEffectsDefinition.def`

```json
{
  "Guid": "4ceecd10-bf39-4437-891d-78ff48445bf1",
  "OnDisconnectParticleEffect": {
    "ParticleEffect": "cf82bb19-55be-4fb8-b251-888f57ded7fd",
    "Dummy": "b80cb7d1-126f-406e-a1c7-6410109f3c1d",
    "Scale": 1
  },
  "BlockAudio": "event:/SFX/Block/Connector",
  "AudioStateParameter": "Connector",
  "AudioStateAligning": "available",
  "AudioStateReadyToConnect": "alligned",
  "AudioStateConnect": "lock",
  "AudioStateDisconnect": "unlock"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockEffectsDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockEffectsDefinitionObjectBuilder')
```
