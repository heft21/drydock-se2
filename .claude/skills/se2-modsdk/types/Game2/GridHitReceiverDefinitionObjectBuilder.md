# GridHitReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage.GridHitReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DirectFracturesAwayFromBlockCenter` | Will ignore physical impulse direction and instead direct all broken off fractures away from block center |
| `FractureAngularImpulseRatio` | Proportion of final fracture impulse that will be randomly turned in angular impulse |
| `FractureImpulseDeviationRatio` | Proportion of final fracture impulse that will be randomly deviated away |

## A real one

`Vanilla\Assets\System\Grid\GridHitReceiverDefinition.def`

```json
{
  "Guid": "7455c2fa-1f0a-47d8-883d-581b44c6f079",
  "ReceivedDamageType": "235c92de-c788-46f2-aab0-972b2e305115",
  "DirectFracturesAwayFromBlockCenter": false,
  "FractureAngularImpulseRatio": 0.2,
  "FractureImpulseDeviationRatio": 0.3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridHitReceiverDefinitionObjectBuilder')
search_content('', type_contains='GridHitReceiverDefinitionObjectBuilder')
```
