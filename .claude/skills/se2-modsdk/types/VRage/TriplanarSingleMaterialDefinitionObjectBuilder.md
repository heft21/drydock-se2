# TriplanarSingleMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.TriplanarSingleMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **124**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlendingMultiplier` | Controls the size of the region where triplanar (between axis directions) blending occurs. A smaller value blends to a smaller region. For blending that factors in the heightmap more, use a large value for this and a small value for . |
| `BlendingSoftness` | Controls the softness of the influence the heightmap has on triplanar (between axis directions) blending. A smaller value blends more tightly based on the heightmap. |
| `BlendingYScale` | A scale factor that increases or decreases the blending between Y and XZ projections. Values lower than 1 will shrink transitions from Y to XZ, while values higher than 1 will enlarge them. |
| `ColorFar3` | Color (sRGB) override at FAR 3. |
| `ColorMetalBottomYFar1` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At Far1 LOD. |
| `ColorMetalBottomYFar2` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At Far2 LOD. |
| `ColorMetalBottomYNear` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At near LOD |
| `ColorMetalXZFar1` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along X and Z axis. At Far1 LOD. |
| `ColorMetalXZFar2` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along X and Z axis. At Far2 LOD. |
| `ColorMetalXZNear` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along X and Z axis. At near LOD |
| `ColorMetalYFar1` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At Far1 LOD. |
| `ColorMetalYFar2` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At Far2 LOD. |
| `ColorMetalYNear` | Texture composed of Color (RGB) and Metalness (A). Used for projection mapping along Y axis. At near LOD |
| `ExtensionsBottomYFar1` | Extension texture. Used for projection mapping along Y axis. At Far1 LOD. |
| `ExtensionsBottomYFar2` | Extension texture. Used for projection mapping along Y axis. At Far2 LOD. |
| `ExtensionsBottomYNear` | Extension texture. Used for projection mapping along Y axis. At near LOD. |
| `ExtensionsXZFar1` | Extension texture. Used for projection mapping along X and Z axis. At Far1 LOD. |
| `ExtensionsXZFar2` | Extension texture. Used for projection mapping along X and Z axis. At Far2 LOD. |
| `ExtensionsXZNear` | Extension texture. Used for projection mapping along X and Z axis. At near LOD. |
| `ExtensionsYFar1` | Extension texture. Used for projection mapping along Y axis. At Far1 LOD. |
| `ExtensionsYFar2` | Extension texture. Used for projection mapping along Y axis. At Far2 LOD. |
| `ExtensionsYNear` | Extension texture. Used for projection mapping along Y axis. At near LOD. |
| `GrassMaterial` | Grass material that should be used for this triplanar material |
| `HeightBlendingXZRange` | Blending range of the XZ height map. Lower values lead to stronger height map influence in the height blending, without affecting displacement. |
| `HeightBlendingYRange` | Blending range of the Y height map. Lower values lead to stronger height map influence in the height blending, without affecting displacement. |
| `NormalRoughnessBottomYFar1` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At Far1 LOD. |
| `NormalRoughnessBottomYFar2` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At Far2 LOD. |
| `NormalRoughnessBottomYNear` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At near LOD |
| `NormalRoughnessXZFar1` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along X and Z axis. At Far1 LOD. |
| `NormalRoughnessXZFar2` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along X and Z axis. At Far2 LOD. |
| `NormalRoughnessXZNear` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along X and Z axis. At near LOD |
| `NormalRoughnessYFar1` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At Far1 LOD. |
| `NormalRoughnessYFar2` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At Far2 LOD. |
| `NormalRoughnessYNear` | Texture composed of Normal (RGB) and Roughness (A). Used for projection mapping along Y axis. At near LOD |
| `ReflectanceMultiplier` | Reflectance multiplier, which multiplies the reflectance map or the default value. |
| `StandardTiling` | Tiling settings for Medium and High Quality |
| `WeatheringMultiplier` | Multiplier on the weathering, or voxel AO for this material. A value of 1 causes sharp voxel edges to blend towards white, as if from being exposed to the elements. |

## A real one

`Vanilla\Assets\Items\Debris\Rocks\DefaultDebrii.def`

```json
{
  "Guid": "4dbb57cd-b0f2-4002-8f09-17a7192eefb9",
  "DefaultState": "95a8abdd-7e1f-4cfc-b636-a1d73d2e7d8c",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "StandardTiling": {
    "TilingScale": 50,
    "TilingBlend": 0.6,
    "NearFarTransitionScale": 0.75,
    "BaseScale": 6,
    "Lods": {
      "_data": [
        {
          "Key": "c8157805-7345-42c0-9730-91aabb7931d0",
          "Value": {
            "Texture": "Far1",
            "Distance": 16,
            "Scale": 16
          }
        },
        {
          "Key": "f4618ccc-6c33-48a8-b485-d38fdfd99a8d",
          "Value": {
            "Texture": "Far2",
            "Distance": 50,
            "Scale": 50
          }
        },
        {
          "Key": "7214629f-c895-4a06-b73f-6ea5c12e71cd",
          "Value": {
            "Texture": "Far3",
            "Distance": 10000,
            "Scale": 1
          }
        }
      ]
    }
  },
  "BlendingMultiplier": 0.2,
  "BlendingSoftness": 0.1,
  "BlendingYScale": 1,
  "HeightBlendingXZRange": 1,
  "HeightBlendingYRange": 1,
  "ColorMetalXZNear": "{G}73092ccb-59c5-433e-99bb-9162e878b5b0",
  "ColorMetalYNear": "{G}52f68ecb-45a3-473f-8895-c44034cad763",
  "NormalRoughnessXZNear": "{G}f30b170e-bc39-40e0-8ac0-df6c36e6d5a6",
  "NormalRoughnessYNear": "{G}0d112378-bd30-4528-9e36-53a40a219835",
  "ExtensionsXZNear": "{G}eb6866b3-e612-405b-831c-d15d75b97591",
  "ExtensionsYNear": "{G}717ff163-f39c-4c57-afa9-27aec08a1d43",
  "ColorMetalXZFar1": "{G}125dda5b-54e9-42b6-8068-6518c9060951",
  "ColorMetalYFar1": "{G}ea052008-8ccb-462d-9f9d-356775ac7e23",
  "NormalRoughnessXZFar1": "{G}00993415-8608-44ec-93bf-3355d02ad935",
  "NormalRoughnessYFar1": "{G}01ce9021-7464-413e-85a6-a75b44b1438a",
  "ExtensionsXZFar1": "{G}e9bf4daf-52b1-4076-ad2f-a655d78c9ab3",
  "ExtensionsYFar1": "{G}a43c2773-5ab7-4348-8e30-76a59a0d8e0e",
  "ColorMetalXZFar2": "{G}9752f72a-2b8d-484f-a224-d2fd43ed5d0c",
  "ColorMetalYFar2": "{G}d2ccadf0-6d04-4ca1-9f52-5c5f40994602",
  "NormalRoughnessXZFar2": "{G}b43e1daa-2677-43a1-9746-bf7bdf1549b4",
  "NormalRoughnessYFar2": "{G}549d84ac-58e8-48f1-b45a-28fb9ae71851",
  "ExtensionsXZFar2": "{G}3a9c8fa5-5238-46ce-ac9c-3612f7f673d4",
  "ExtensionsYFar2": "{G}0836f106-7333-423e-9a1d-6f3d9c824669",
  "ColorFar3": {
    "PackedValue": 6184801
  },
  "GrassMaterial": null,
  "WeatheringMultiplier": 1
}
```

Others: `IceOre`, `GoldOre`

---

Read it with the MCP server rather than by hand:

```
describe_type('TriplanarSingleMaterialDefinitionObjectBuilder')
search_content('', type_contains='TriplanarSingleMaterialDefinitionObjectBuilder')
```
