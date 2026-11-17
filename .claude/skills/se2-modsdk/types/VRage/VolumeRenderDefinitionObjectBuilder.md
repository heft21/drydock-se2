# VolumeRenderDefinitionObjectBuilder

`VRage:Keen.VRage.Game.ProceduralGeneration.VolumeRenderDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.ProceduralGeneration`
- definitions using it: **2**

## What it is

Migration for the object builder.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ModelAsset` | Model used for the representation of the volume |

## A real one

`Vanilla\Assets\System\AsteroidRings\KemikRing\KemikRing.def`

```json
{
  "Guid": "b9e5192a-228f-44d2-83c4-d9d104b32754",
  "ModelAsset": "{G}cbb8d116-7359-43a9-b79a-6ea6de8a307f",
  "MapMaterial": "3c0e3194-f675-4aef-9b88-41cb25c7fe61",
  "MapVisualPrefab": "b9f6ad3f-e103-4b47-84ec-67da3627ed18"
}
```

Others: `VerdureRing`

---

Read it with the MCP server rather than by hand:

```
describe_type('VolumeRenderDefinitionObjectBuilder')
search_content('', type_contains='VolumeRenderDefinitionObjectBuilder')
```
