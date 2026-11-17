# CinematicSpectatorInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.CinematicSpectatorInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\SpectatorInputAdapter\CinematicSpectatorInputHandlerDefinition.def`

```json
{
  "Guid": "88b371c0-08c2-4534-94d1-c904e5f6c15c",
  "InputContextDefinition": "ff92e525-ca85-4a9e-abe8-a51d9e3997d3",
  "RotateCameraUp": "8ba93c75-4a79-4a67-871e-1639d9afd0e6",
  "RotateCameraDown": "5ecfd301-aee3-4cb8-9946-9af7908e69ae",
  "RotateCameraLeft": "b36f7c0d-2717-4772-8b5d-a8b6aa482f59",
  "RotateCameraRight": "39fc9d23-9064-4d1f-bc84-a633a340341d",
  "RotateCameraUpLeft": "c37e077c-b114-46e7-8e98-da51aa006ea7",
  "RotateCameraUpRight": "67c16c86-88e7-454e-bd5c-a22e5b1ee6e7",
  "RotateCameraDownLeft": "dacdb3c4-d2a8-4054-8216-62d951dd57e1",
  "RotateCameraDownRight": "7c20beac-d41c-4078-b84a-688a3a0aad0d",
  "ResetCameraRotation": "51a6f3bf-5424-4c55-ba1e-a3f94322ad39",
  "AngularSpeedChange": "442733be-aea6-4676-8747-2f6563499ffd",
  "ToggleEntityLock": "8d4fa496-a399-45c6-9610-97a9e797b1d1",
  "CycleLockMode": "b10a1079-cd51-491a-afa1-fe7d706d4712",
  "CameraRotationSpeed": 1,
  "InputKind": "Movement"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CinematicSpectatorInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='CinematicSpectatorInputHandlerDefinitionObjectBuilder')
```
