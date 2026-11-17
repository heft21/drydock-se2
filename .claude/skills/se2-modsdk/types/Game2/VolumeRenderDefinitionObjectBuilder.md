# VolumeRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProceduralGeneration.VolumeRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProceduralGeneration`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\AsteroidRings\TestRing\AsteroidRing.def`

```json
{
  "Guid": "d1b96362-f71f-4eb9-961d-f3168fa71887",
  "ModelAsset": "{G}0afc4d21-5b58-4eef-80e1-3a835bd2c6ba",
  "MapMaterial": "1882398b-2fc4-49ed-94ae-46d602ac13f3",
  "MapVisualPrefab": "b9f6ad3f-e103-4b47-84ec-67da3627ed18"
}
```

Others: `AsteroidField`

---

Read it with the MCP server rather than by hand:

```
describe_type('VolumeRenderDefinitionObjectBuilder')
search_content('', type_contains='VolumeRenderDefinitionObjectBuilder')
```
