# DrillToolDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\DrillToolDefinition.def`

```json
{
  "Guid": "c6d62523-b264-4c89-83f7-8b8327a03154",
  "AutoConversions": [],
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "DetectProjections": false,
    "Frequency": 1,
    "Occlusion": true,
    "FirstHit": false,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0,
    "DetectionOffset": null,
    "LayerFilter": null
  },
  "PrimaryActionDummy": "8f20b1ae-4081-48fc-8b3a-8c7846af1a98",
  "PrimaryDrillingTimeModifier": 1,
  "SecondaryActionDummy": "3ecafef7-62ee-40e0-ba00-46d1d089934e",
  "SecondaryDrillingTimeModifier": 0.5,
  "PunchContactDelay": 2670000,
  "FallThroughDuration": 8000000,
  "PrimaryBrushShape": null,
  "SecondaryBrushShape": null,
  "DropOreAsFallback": true,
  "VoxelLayer": null,
  "CastColliderRadius": 0.08,
  "ProbeOffsetRight": 0,
  "ProbeOffsetUp": 0,
  "ProbeOffsetForward": 0,
  "ThirdPersonProbeOffsetRight": 0.2,
  "ThirdPersonProbeOffsetUp": -0.55,
  "ThirdPersonProbeOffsetForward": 0.2,
  "ThirdPersonProbeYaw": 0,
  "ThirdPersonProbePitch": 0.29670596,
  "ContactDummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
  "MaxCastDistance": 1.8,
  "ThirdPersonMaxCastDistance": 1.25,
  "ShoulderDummy": null,
  "CrouchedShoulderDummy": null,
  "MaxShoulderDistance": 3.5
}
```

Others: `CharacterDrillToolDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillToolDefinitionObjectBuilder')
search_content('', type_contains='DrillToolDefinitionObjectBuilder')
```
