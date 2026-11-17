# ToolDamageDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage.ToolDamageDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageAdapterPrefab` | Entity that contains various implementations. |
| `DetectionArgs` | Detector settings to obtain other entities to damage |

## A real one

`Vanilla\Assets\CharacterTools\HandGrinders\Shared\HandGrinder_ToolDamageDefinition.def`

```json
{
  "Guid": "8af01a98-910e-4f89-b805-454478088ce3",
  "DamageAdapterPrefab": "ccb9f298-4d3c-420d-b9c8-29a7f3bba3d3",
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": true,
    "DetectTopMostEntities": true,
    "DetectProjections": false,
    "Frequency": 15,
    "Occlusion": false,
    "FirstHit": false,
    "AllowDuplication": true,
    "DummyOcclusionEpsilon": 0,
    "DetectionOffset": null,
    "LayerFilter": null
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolDamageDefinitionObjectBuilder')
search_content('', type_contains='ToolDamageDefinitionObjectBuilder')
```
