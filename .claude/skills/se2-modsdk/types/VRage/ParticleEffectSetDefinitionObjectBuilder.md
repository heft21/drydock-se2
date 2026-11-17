# ParticleEffectSetDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.ParticleEffectSetDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **15**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Effects` | List of particle effects with their occurrence weights. |

## A real one

`Vanilla\Assets\System\Particles\Generic\Fire\FireLarge_ParticleSet.def`

```json
{
  "Guid": "3ccf2891-968b-47c2-998d-fb60ea82b514",
  "Effects": [
    {
      "Key": "ded98e6b-4604-4220-a072-c750630a8717",
      "Value": {
        "Effect": "e30e4526-24a5-4962-938e-f763040d9b1d",
        "Weight": 0.33
      }
    },
    {
      "Key": "4f3b261e-5c53-4b59-a772-7bb145831db3",
      "Value": {
        "Effect": "bac64b36-44d2-456e-96c5-8ac89228cb5b",
        "Weight": 0.33
      }
    },
    {
      "Key": "f068feee-566b-463e-93c2-c0594467f5ee",
      "Value": {
        "Effect": "21202bf6-7c7e-4e2f-b6f0-a687a6234a26",
        "Weight": 0.33
      }
    }
  ]
}
```

Others: `FireSmall_ParticleSet`, `FireMedium_ParticleSet`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectSetDefinitionObjectBuilder')
search_content('', type_contains='ParticleEffectSetDefinitionObjectBuilder')
```
