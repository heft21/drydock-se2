# ParticleEffectDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.ParticleEffectDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **245**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EffectDuration` | Duration of the effect |
| `EffectDurationVariation` | Variation of the effect duration |
| `EffectMaxDistance` | Max viewing distance of the effect |
| `IsLooping` | Enable looping of the effect |
| `ParticleAudio` | Optional audio event when particle plays. Should loop depending on |
| `ParticleEmitters` | List of particle emitters along with their modifiers |
| `ParticleLight` | List of particle lights |

## A real one

`Vanilla\Assets\System\Particles\Generic\Debug\ParticleEffect_Debug.def`

```json
{
  "Guid": "a4ecba57-d0fd-4784-a71d-f9688537e18c",
  "EffectDuration": 5,
  "EffectDurationVariation": 0,
  "EffectMaxDistance": 200,
  "IsLooping": true,
  "ParticleEmitters": [
    {
      "Key": "efaf777f-ae48-47b1-aca7-146f726eccc9",
      "Value": {
        "Definition": "9bcd1355-ff92-4ab0-b792-0239def4962e",
        "Parameters": {
          "GlobalScaleFactor": 1,
          "EmitterLifeTime": 5,
          "EmitterStartTime": 0,
          "GravityMultiplier": 0
        }
      }
    },
    {
      "Key": "1d8569eb-d991-4ada-8f2f-d33711fac393",
      "Value": {
        "Definition": "84144293-91c2-4c66-b139-e16c9b6cca36",
        "Parameters": {
          "GlobalScaleFactor": 1,
          "EmitterLifeTime": 5,
          "EmitterStartTime": 0,
          "GravityMultiplier": 0
        }
      }
    },
    {
      "Key": "f754341f-34ab-4876-a684-6266e81514f5",
      "Value": {
        "Definition": "58572144-b5a3-47a2-a96d-84d2085296b1",
        "Parameters": {
          "GlobalScaleFactor": 1,
          "EmitterLifeTime": 5,
          "EmitterStartTime": 0,
          "GravityMultiplier": 0
        }
      }
    }
  ],
  "ParticleAudio": null,
  "ParticleLight": []
}
```

Others: `Delfos_ParticleEffect`, `Snow_ParticleEffect`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectDefinitionObjectBuilder')
search_content('', type_contains='ParticleEffectDefinitionObjectBuilder')
```
