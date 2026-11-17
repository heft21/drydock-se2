# ProjectileHitScanEffectsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ProjectileSystems.ProjectileHitScanEffectsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.ProjectileSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorBlockMaterial` | Physics material representing an armor block hit. |
| `ImpactScale` | Scale of the impact particle effect. |
| `ImpactsPerFrame` | Maximum number of impact particles to spawn per frame. |
| `MaterialEffectList` | Dictionary of all hit and their corresponding . |
| `MultiEffectsPerFrame` | Maximum number of multi effects to spawn per frame |
| `PushFilter` | Entity layer filter to use when pushing entities within the path of the projectile (pushing client-side fractures/debris) |
| `TracersPerFrame` | Maximum number of impact particles to spawn per frame. |

## A real one

`Vanilla\Assets\System\Configurations\Effects\ProjectileHitScanEffectsConfiguration.def`

```json
{
  "Guid": "fb439433-3147-46be-b4d4-2d2213fffb0d",
  "ImpactScale": 0.5,
  "ImpactsPerFrame": 25,
  "TracersPerFrame": 50,
  "MultiEffectsPerFrame": 20,
  "MaterialEffectList": {
    "a6ec4448-db7e-4446-8a28-7ace385919bd": "c238629b-6a34-40c0-9706-b08a2fd6628e",
    "44ac27b1-7c39-4a2b-bc71-6a31b80db2c1": "69e94c17-4340-41a3-944d-ea60c86ad6d2",
    "cb39081f-c52d-4a0e-ae5f-106e218f76eb": "6a3e4a73-6458-4262-ac71-379596463386",
    "39c1cfce-31fa-4503-b99a-50511d73ab64": "ebb80df2-c789-4d38-9542-ea4e0eacbb70",
    "d7459919-32b7-4bb1-bcc0-9ba1a94d7bca": "4aec9f71-db1a-470e-9a3b-a959f4619c9a",
    "d14e99db-54fc-411a-91f9-3d3db7212c76": "c3590aca-572a-43ef-9e47-f5fb72f8b3b2",
    "2a32e418-fe92-43bd-9379-15e346f2d49d": "b4049324-b699-4946-8b5f-6c18540063ab",
    "e2431cdd-c4d1-4455-a303-06fde11a922c": "affdbcc7-a82d-4b4d-94e7-0bf3ee9f4890",
    "56dd2b0b-15d2-479f-a33e-f49129afe00a": "46466e17-4115-4731-a0a4-f9c7071c5438",
    "b0daa08e-c571-4d3f-bdc6-7b25dcc5baea": "239e50ef-f312-47e0-b100-9afa8509dfde",
    "a052bbc9-5465-4e12-8781-7d4105dec352": "844cafde-a916-4499-a294-df20789c7564",
    "77b8800a-2b36-4dd5-b821-578fb4dde07d": "3a19c2e6-fb2f-4b87-8abd-cb6056c38525",
    "1f56f4e9-86ca-4854-94c0-5623edb7fbba": "fb3d8f6b-662b-46d2-970e-b652bd63cdc7"
  },
  "CriticalMaterialEffectList": {
    "77b8800a-2b36-4dd5-b821-578fb4dde07d": "76cd2662-a9d1-473e-a24e-cda103d55b86"
  },
  "ArmorBlockMaterial": "cb39081f-c52d-4a0e-ae5f-106e218f76eb",
  "BackpackMaterial": "1f56f4e9-86ca-4854-94c0-5623edb7fbba",
  "PushFilter": "4d9dda78-0463-40e3-b6bc-4103367e10ce"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileHitScanEffectsConfigurationObjectBuilder')
search_content('', type_contains='ProjectileHitScanEffectsConfigurationObjectBuilder')
```
