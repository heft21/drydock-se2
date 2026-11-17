# CameraDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## What it is

Builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FOV` | Camera field of view |
| `FarFarPlane` | Very far camera plane for culling very far objects |
| `FarPlane` | Far camera plane distance, in meters. Used to cull render entities. |
| `FieldOfViewMaximum` | Max FOV angle |
| `FieldOfViewMinimum` | Min FOV angle |
| `NearPlane` | Near camera plane (should be something very small, like 0.05m or less) |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\RenderCamera.def`

```json
{
  "Guid": "6a60df5a-bd6b-452d-bb0c-bb824090ee1d",
  "NearPlane": 0.025
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraDefinitionObjectBuilder')
search_content('', type_contains='CameraDefinitionObjectBuilder')
```
