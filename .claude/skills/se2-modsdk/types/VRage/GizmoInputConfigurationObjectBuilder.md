# GizmoInputConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Gizmos.GizmoInputConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Gizmos`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EditButton` | Pointer input to "click" and edit gizmos. |
| `InputContext` | Context for the inputs. |
| `PointerPosition` | Input of the pointer position. |
| `TransformRotate` | Input to set the . |
| `TransformScale` | Input to set the . |
| `TransformSnapping` | Input to enable . |
| `TransformTranslate` | Input to set the . |

## A real one

`Engine\Assets\Configurations\Input\GizmoInputConfiguration.def`

```json
{
  "Guid": "0976bc62-7319-49af-b8e0-49d46ae58128",
  "InputContext": "7b4da8a3-9ddf-49c2-812b-babf5fdcbc23",
  "EditButton": "7866c6f7-9b4a-4e19-ab7b-4ebf445ead8a",
  "PointerPosition": "daeab155-fd20-45c7-80c1-fa404e0b1259",
  "TransformTranslate": "1cc0496e-c4b3-4f1c-935d-6bd962d373b4",
  "TransformRotate": "9d780839-5d38-412f-a2d8-af3b84bc39dd",
  "TransformScale": "af33ab41-eae5-4b2c-91c6-ebf68d6a143a",
  "TransformSnapping": "480bf8db-6543-4e3c-974a-ed49066a2401"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GizmoInputConfigurationObjectBuilder')
search_content('', type_contains='GizmoInputConfigurationObjectBuilder')
```
