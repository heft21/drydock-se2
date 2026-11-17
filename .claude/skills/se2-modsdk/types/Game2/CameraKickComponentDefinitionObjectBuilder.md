# CameraKickComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraKickComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\RenderCameraKickComponentDefinition.def`

```json
{
  "Guid": "75892917-9b3e-4bb4-8138-df27e28f5db2",
  "KickPeakTime": 0.08,
  "MaxKickAngle": 0.02182,
  "CriticalKickMultiplier": 1.2,
  "MaxTotalKickAngle": 0.04363
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraKickComponentDefinitionObjectBuilder')
search_content('', type_contains='CameraKickComponentDefinitionObjectBuilder')
```
