# MagneticBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MagneticBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectionArgs` | Specifies how and what entities to detect when searching for eligible target to lock. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MagneticBlockDefinition.def`

```json
{
  "Guid": "33504930-b49b-4697-8178-b13c45b8b534",
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "DetectProjections": false,
    "Frequency": 1,
    "Occlusion": false,
    "AllowDuplication": true,
    "DummyOcclusionEpsilon": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MagneticBlockDefinitionObjectBuilder')
search_content('', type_contains='MagneticBlockDefinitionObjectBuilder')
```
