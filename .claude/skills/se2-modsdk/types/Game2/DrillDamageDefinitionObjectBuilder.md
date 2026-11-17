# DrillDamageDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage.DrillDamageDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DrillDamageDefinition.def`

```json
{
  "Guid": "b5e43e13-b829-4976-b892-97655b55aaf4",
  "DamageAdapterPrefab": null,
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": true,
    "DetectTopMostEntities": true,
    "DetectProjections": false,
    "Frequency": 30,
    "Occlusion": false,
    "FirstHit": false,
    "AllowDuplication": true,
    "DummyOcclusionEpsilon": 0,
    "LayerFilter": "1ef9d72d-527e-44b2-bfc1-0d708d8229a1"
  }
}
```

Others: `IntegrityToolDamageDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillDamageDefinitionObjectBuilder')
search_content('', type_contains='DrillDamageDefinitionObjectBuilder')
```
