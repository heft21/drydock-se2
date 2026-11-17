# SafeZoneFieldMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.SafeZoneFieldMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnimationSpeed` | The speed and direction that the UVs will be scrolled over time. X is horizontal and Y is vertical. |
| `AnimationSpeedFar` | Same as but for a far view |
| `CollisionHighlightDistance` | The distance (in a multiple of the safe zone radius) of the highlight effect near where the safe zone intersects world geometry. |
| `EdgeSmoothness` | How smooth is the safe zone - solid intersection |
| `EmissivityStrength` | Strength of the emissivity for the color emitted according to . Controls regions where the highlight isn't active. |
| `HighlightFalloffPower` | The falloff power of the highlight (both the rim-light and collision highlight). Larger values fall off faster. |
| `HighlightStrength` | The strength of the highlight (both the rim-light and collision highlight) |
| `NormalRoughnessTexture` | Normal and roughness map. Determines the normal and roughness of the environment reflection, as well as the normal of the refraction |
| `NormalRoughnessTextureFar` | Same as but for a far view. If not assigned - is used |
| `OpacityTexture` | Opacity texture to use, grayscale. Determines the emissive color pattern for both the highlight and emissive output. The color is determined by entity data. |
| `OpacityTextureFar` | Same as but for a far view. If not assigned - is used |
| `RefractiveIndex` | The index of refraction. 1.0 is no refraction. Higher values refract inwards and lower values refract outwards. |
| `TransitionCloseDistance` | if distance to safe zone is smaller than this value, closer preset is selected. if the distance is between this and two presets are interpolated |
| `TransitionFarDistance` | if distance to safe zone is bigger than this value, farthest preset is selected if the distance is between and this two presets are interpolated |
| `UVScale` | The speed and direction that the UVs will be scrolled over time. X is horizontal and Y is vertical. |
| `UVScaleFar` | Same as but for a far view |

## A real one

`Vanilla\Assets\System\SafeZones\Materials\SafeZoneMaterial_Lines\SafeZoneMaterial.def`

```json
{
  "Guid": "a57fc048-daca-4dfc-8209-2d64c4f7499a",
  "DefaultState": "6566e25c-7571-4f2b-b74b-3298226a80e6",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "OpacityTexture": "{G}6ce42f1a-636e-4224-8535-4f95c02257ca",
  "NormalRoughnessTexture": "{G}2db4f00a-c2ab-44bc-ba74-69d98286925b",
  "OpacityTextureFar": null,
  "NormalRoughnessTextureFar": null,
  "RefractiveIndex": 1.02,
  "EmissivityStrength": 0.25,
  "CollisionHighlightDistance": 0.099609375,
  "HighlightStrength": 10,
  "HighlightFalloffPower": 8.286655,
  "AnimationSpeed": {
    "X": 0.025,
    "Y": 0.00025
  },
  "AnimationSpeedFar": {
    "X": 0.08,
    "Y": 0.0008
  },
  "UVScale": {
    "X": 4,
    "Y": 4
  },
  "UVScaleFar": {
    "X": 1.25,
    "Y": 1.25
  },
  "EdgeSmoothness": 0.05,
  "TransitionCloseDistance": 250,
  "TransitionFarDistance": 400
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SafeZoneFieldMaterialDefinitionObjectBuilder')
search_content('', type_contains='SafeZoneFieldMaterialDefinitionObjectBuilder')
```
