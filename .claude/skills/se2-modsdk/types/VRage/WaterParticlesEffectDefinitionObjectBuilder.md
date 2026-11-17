# WaterParticlesEffectDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.WaterParticlesEffectDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxSplashesPerFrame` | Maximum amount of splash particles created per frame |
| `MaxSpraysPerFrame` | Maximum amount of spray particles created per frame |
| `SplashParticles` | particles created as singular splashes. Activated mostly on waterfalls and falling water |
| `SprayParticles` | particles created as sprays. Activated mostly on interactions with solids |

## A real one

`Vanilla\Assets\System\Water\WaterParticlesEffectDefinition.def`

```json
{
  "Guid": "b2b0f1e1-0f4f-4492-a2ea-ac3812b79ad8",
  "SplashParticles": [
    {
      "Key": "bc066bc7-f5f1-46b4-9ac9-1a1698afe1ca",
      "Value": {
        "Emitter": "afe6d0cd-1576-433d-81b4-54511237ede3",
        "FoamFactor": 0.3,
        "Weight": 1,
        "LiftCoefficient": 0,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.2,
        "VolumeSpeedVariance": 0
      }
    },
    {
      "Key": "5ee75300-ce03-4aaf-bf71-b7180f23f291",
      "Value": {
        "Emitter": "6d2fa91b-39cf-4be2-a12c-3924d08f7551",
        "FoamFactor": 0.3,
        "Weight": 1,
        "LiftCoefficient": 0,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.2,
        "VolumeSpeedVariance": 0
      }
    },
    {
      "Key": "0ee5cb7c-49ba-4707-ab39-e1a162da33fc",
      "Value": {
        "Emitter": "351f2a95-58b9-4d64-8dd6-3c6d124f5ef0",
        "FoamFactor": 0.3,
        "Weight": 1,
        "LiftCoefficient": 0,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.2,
        "VolumeSpeedVariance": 0
      }
    }
  ],
  "MaxSplashesPerFrame": 400,
  "SprayParticles": [
    {
      "Key": "19872799-1853-4062-bedb-792fff05af63",
      "Value": {
        "Emitter": "da607367-9042-418b-91e0-94627634a2bf",
        "FoamFactor": 1,
        "Weight": 1,
        "LiftCoefficient": 0.2,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.5,
        "VolumeSpeedVariance": 0
      }
    },
    {
      "Key": "cda07642-61ca-40e4-8a22-5ba1a852e049",
      "Value": {
        "Emitter": "065bdc4a-02aa-4981-baa9-3b138b516eb4",
        "FoamFactor": 1,
        "Weight": 1,
        "LiftCoefficient": 0.2,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.5,
        "VolumeSpeedVariance": 0
      }
    },
    {
      "Key": "a759b998-84df-4ef1-8777-d79f1321f5bb",
      "Value": {
        "Emitter": "f0d0884b-f9f9-4ee0-afba-ad5bc18764e4",
        "FoamFactor": 1,
        "Weight": 0.5,
        "LiftCoefficient": 0.2,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.5,
        "VolumeSpeedVariance": 0
      }
    }
  ],
  "MaxSpraysPerFrame": 600,
  "VolumeParticles": [
    {
      "Key": "8ecefc79-13c3-4260-a945-e34a7c7b8ee2",
      "Value": {
        "Emitter": "28a27a52-3ac0-4e05-93d8-a16b8f4c1538",
        "FoamFactor": 1,
        "Weight": 0.5,
        "LiftCoefficient": 0.2,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.5,
        "VolumeSpeedVariance": 0.1
      }
    },
    {
      "Key": "cfde9b37-8381-40d1-b91d-1a8660842ae7",
      "Value": {
        "Emitter": "c89a741e-1179-4c45-a697-bc28923d555b",
        "FoamFactor": 1,
        "Weight": 1,
        "LiftCoefficient": 0.2,
        "LiftVariance": 0.3,
        "SideToSideVariance": 0.5,
        "VolumeSpeedVariance": 0.1
      }
    }
  ],
  "MaxVolumeParticlesPerFrame": 5000,
  "VolumeLoopedEffect": "330e415e-fd8b-48e4-a7dc-470bf18f1f1d"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterParticlesEffectDefinitionObjectBuilder')
search_content('', type_contains='WaterParticlesEffectDefinitionObjectBuilder')
```
