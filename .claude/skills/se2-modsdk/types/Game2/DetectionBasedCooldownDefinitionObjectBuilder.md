# DetectionBasedCooldownDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Cooldown.DetectionBasedCooldownDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Cooldown`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectionArgs` | Configures detection parameters for entities |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DetectionBasedCooldownDefinition.def`

```json
{
  "Guid": "f1ab544f-1717-45de-8e74-09bb2c34f1e2",
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "Frequency": 20,
    "Occlusion": false,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DetectionBasedCooldownDefinitionObjectBuilder')
search_content('', type_contains='DetectionBasedCooldownDefinitionObjectBuilder')
```
