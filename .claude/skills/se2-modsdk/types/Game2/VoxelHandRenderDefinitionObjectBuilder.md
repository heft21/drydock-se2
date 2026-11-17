# VoxelHandRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Toolbars.VoxelHand.VoxelHandRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Toolbars.VoxelHand`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AxisColorX` | Color of the line that is displayed along the X axis |
| `AxisColorY` | Color of the line that is displayed along the Y axis |
| `AxisColorZ` | Color of the line that is displayed along the Z axis |
| `AxisFalloff` | Exponent modifier that changes how quickly the axis line projection hides when it is facing the camera |
| `AxisLength` | How for the axis lines extend past the preview |
| `AxisProjectionPreview` | Enable or disable the axis projection lines |
| `AxisThickness` | How thick the axis lines are. The unit is scaled to maintain a consistent thickness |
| `BrushColor` | Color of brush when the placement is valid or not active Alpha is not used |
| `CapsuleCylinderModel` | Model of the cylinder part of the capsule voxel hand |
| `CapsuleHemisphereModel` | Model of the top and bottom parts of the capsule voxel hand |
| `CubeModel` | Model of the cube voxel hand |
| `DecalPerAxisX` | Decal that is projected along the X axis to help with spatial awareness |
| `DecalPerAxisZ` | Decal that is projected along the Z axis to help with spatial awareness |
| `DecalPerY` | Decal that is projected along the Y axis to help with spatial awareness |
| `HighlightColor` | Color of the brush highlight where the brush intersects something Alpha is not used |
| `InvalidColor` | Color of brush when the placement is invalid Alpha is not used |
| `LightColor` | Color of the light at the center of the voxel hand brush Scales with the brush size |
| `LightIntensityMultiplier` | Intensity multiplier (brightness) for the light at the center of the voxel hand brush Scales with the brush size |
| `LightNormalOffset` | Amount the light is offset from the normal by when the brush is aimed at terrain |
| `MinAxisDecalDiameter` | Minimum radius of the decals shown along the projection axis lines |
| `ProjectionAxisRadiusMultiplier` | Multiplier for how large the projection axis should be |
| `RampModel` | Model of the ramp voxel hand |
| `RotateAxis` | When true, the axis lines will rotate with the brush. When false, the axis lines will not rotate at all. |
| `SphereModel` | Model of the sphere voxel hand |
| `VoxelStorageBoundingBoxColor` | Fill color of the targeted voxels bounding box |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\VoxelHandRenderDefinition.def`

```json
{
  "Guid": "39401795-f7a8-47be-8886-4db9824008c9",
  "VoxelStorageBoundingBoxColor": {
    "PackedValue": 167837440
  },
  "BrushColor": {
    "PackedValue": 4292267703
  },
  "HighlightColor": {
    "PackedValue": 4293771945
  },
  "InvalidColor": {
    "PackedValue": 4279308720
  },
  "LightColor": {
    "X": 0.47353154,
    "Y": 0.61720663,
    "Z": 0.6724432,
    "W": 1
  },
  "LightNormalOffset": 0.1,
  "LightIntensityMultiplier": 10,
  "AxisProjectionPreview": true,
  "DecalPerAxisX": "606af65c-133b-4c43-b5c4-acf3db71e73c",
  "DecalPerY": "606af65c-133b-4c43-b5c4-acf3db71e73c",
  "DecalPerAxisZ": "606af65c-133b-4c43-b5c4-acf3db71e73c",
  "AxisLength": 15,
  "MinAxisDecalDiameter": 10,
  "AxisThickness": 1,
  "RotateAxis": false,
  "AxisColorX": {
    "PackedValue": 1188482743
  },
  "AxisColorY": {
    "PackedValue": 1188482743
  },
  "AxisColorZ": {
    "PackedValue": 1188482743
  },
  "AxisFalloff": 3,
  "ProjectionAxisRadiusMultiplier": 3,
  "SphereModel": "{G}997937d5-ef41-4b4e-a3b0-8ccc34bfaba4",
  "CubeModel": "{G}a1f81e0b-f636-4274-a61f-56329f965cb2",
  "CapsuleCylinderModel": "{G}175b3aec-cbdb-4da8-bd96-84eab0b345f0",
  "CapsuleHemisphereModel": "{G}346eab42-0f74-4c92-8779-d9d9b6b94d54",
  "RampModel": "{G}7880898d-f85a-4f57-8926-8b556d0eb09d"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelHandRenderDefinitionObjectBuilder')
search_content('', type_contains='VoxelHandRenderDefinitionObjectBuilder')
```
