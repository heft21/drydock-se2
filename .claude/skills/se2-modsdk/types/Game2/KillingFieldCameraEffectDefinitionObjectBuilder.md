# KillingFieldCameraEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraSpaceEffects.KillingFieldCameraEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.CameraSpaceEffects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EffectParticles` | particle effect for damaging zone, when damage is applied |
| `TransitionRegion` | transition zone where both particles are played. 0 - no transition zone 1 - start playing together with warning particles 0.5 - start playing at half of the warning zone |
| `WarningParticles` | particle effect for warning zone, before the damage is actually applied. if null - no warning particles are played |

## A real one

`Vanilla\Assets\System\Camera\KillingFieldCameraEffectDefinition.def`

```json
{
  "Guid": "8c3e3fa3-3c92-4493-a3b1-64185f151237",
  "WarningParticles": "0104c712-5ccc-4b3b-b74e-7c6aea10de43",
  "EffectParticles": "f48b10e7-b29b-4e17-9134-1b9304c5b9fb",
  "TransitionRegion": 0.1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('KillingFieldCameraEffectDefinitionObjectBuilder')
search_content('', type_contains='KillingFieldCameraEffectDefinitionObjectBuilder')
```
