# DetectedBlockProviderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.DetectedBlockProviderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\ToolProvider.def`

```json
{
  "Guid": "3c54906d-61ec-47ac-97a7-ea3efcda806c",
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": true,
    "DetectTopMostEntities": true,
    "Frequency": 1,
    "Occlusion": true,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0
  },
  "UseSelfAsSource": true
}
```

Others: `ToolProvider`

---

Read it with the MCP server rather than by hand:

```
describe_type('DetectedBlockProviderDefinitionObjectBuilder')
search_content('', type_contains='DetectedBlockProviderDefinitionObjectBuilder')
```
