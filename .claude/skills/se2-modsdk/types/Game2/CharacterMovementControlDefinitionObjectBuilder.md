# CharacterMovementControlDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterMovementControlDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RelativeDampenersDetectionArgs` | Detection settings for relative dampeners used to find the target entity whose velocity we should match |

## A real one

`Vanilla\Assets\Characters\System\CharacterMovementControlDefinition.def`

```json
{
  "Guid": "3735428b-4b42-4d12-ae09-a7b569da9d4d",
  "RelativeDampenersDetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "Frequency": 0,
    "Occlusion": false,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMovementControlDefinitionObjectBuilder')
search_content('', type_contains='CharacterMovementControlDefinitionObjectBuilder')
```
