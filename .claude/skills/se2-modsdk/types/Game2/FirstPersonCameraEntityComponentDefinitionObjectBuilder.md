# FirstPersonCameraEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Modes.FirstPersonCameraEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Modes`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LookOffsetResetSpringStiffnessLag` | Spring stiffness value representing camera look offset reset rotation lag. Values from 0 to 1, 1 means no lag. |
| `RotationSpringStiffnessLag` | Spring stiffness value representing camera rotation lag. Values from 0 to 1, 1 means no lag. |

## A real one

`Vanilla\Assets\System\Camera\CharacterFirstPersonCamera\FirstPersonCamera.def`

```json
{
  "Guid": "24821479-9af7-460d-ac40-17d32aee7c7c",
  "RotationSpringStiffnessLag": 1,
  "LookOffsetResetSpringStiffnessLag": 0.12
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FirstPersonCameraEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='FirstPersonCameraEntityComponentDefinitionObjectBuilder')
```
