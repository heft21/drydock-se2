# DrillCameraShakeDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Render.Drills.DrillCameraShakeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Render.Drills`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxShakePower` | Cap the maximum contributions of drills to camera shake Drills will not try to add more camera shakes than this during a frame |
| `ShakeModifierWhileDrilling` | Shake modifier to apply while the drills are actively mining/drilling rocks |
| `ShakeModifierWhileSpinning` | Shake modifier to apply while the drills are active/spinning but not drilling/in contact with rocks |
| `ShakePower` | Amount of camera shake to deliver per active drill |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DrillCameraShakeDefinition.def`

```json
{
  "Guid": "4e40b43a-ed59-406b-bab9-9819455a2ede",
  "ShakePower": 0.25,
  "MaxShakePower": 1,
  "ShakeModifierWhileSpinning": 0.5,
  "ShakeModifierWhileDrilling": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillCameraShakeDefinitionObjectBuilder')
search_content('', type_contains='DrillCameraShakeDefinitionObjectBuilder')
```
