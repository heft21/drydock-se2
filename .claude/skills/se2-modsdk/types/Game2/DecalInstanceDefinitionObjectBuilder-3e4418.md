# DecalInstanceDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalInstanceDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **50**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Budget` | Decal Budget. If the number of decals in the budget becomes greater than the limit, previously added decals are faded out |
| `Decal` | Decal material used for the decal, when is false |
| `Decals` | List of decal materials to be randomly selected from, when is true |
| `FadeInTime` | If not null the decal will fade in instead of appearing instantly. |
| `Falloff` | falloff settings of the decal |
| `Flags` | Decal flags |
| `LifeTime` | If null the decal will persist indefinitely (until the budget allows). If not null the lifetime of the decal will be controlled |
| `NormalAlignment` | How aligned is the decal with the surface normal. 0 - decal will face in the same direction it is projected from (shot direction for buillets, etc.) 1 - decal will face in the direction of surface normal |
| `RandomRotation` | If true the rotation around decal Z-Axis will be randomized |
| `RandomizedMaterial` | Whether the decal instance should be randomized or not |
| `Size` | Size of the orthographic projection of a decal, in the XY size of the projected image and the Z size of the projection length. |
| `SizeRandomization` | If not null the decal size will be randomized |

## A real one

`Vanilla\Assets\System\Projectiles\Voxels\Decal_Drill_Voxel_Ice.def`

```json
{
  "Guid": "d6e7bb0e-424e-4edc-bc47-972404be0900",
  "Size": {
    "X": 0.5,
    "Y": 0.5,
    "Z": 0.5
  },
  "SizeRandomization": null,
  "RandomRotation": true,
  "Flags": "Voxels",
  "Falloff": {
    "FalloffZ": 0.1,
    "FalloffX": 0,
    "FalloffY": 0,
    "FalloffAngle": 0.157
  },
  "Budget": "ab82c309-3e7c-4a2b-bfe8-920c7402f18b",
  "FadeInTime": 2500000,
  "LifeTime": {
    "LifeTime": 3000000000,
    "FadeOutTime": 300000000
  },
  "NormalAlignment": 0.75,
  "RandomizedMaterial": false,
  "Decals": [
    {
      "Key": "2265aff0-9fb7-4f38-a428-533559685fe8",
      "Value": "f2e75a9e-504f-47ea-8553-1ff360f23525"
    }
  ],
  "Decal": "a47e76fd-e63e-4cb6-8eb7-356fe3beac6e"
}
```

Others: `Decal_Drill_Voxel_Ores`, `Decal_Drill_Voxel_Rock`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalInstanceDefinitionObjectBuilder')
search_content('', type_contains='DecalInstanceDefinitionObjectBuilder')
```
