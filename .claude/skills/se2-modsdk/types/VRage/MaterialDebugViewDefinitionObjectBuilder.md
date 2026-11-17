# MaterialDebugViewDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.MaterialDebugViewDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials`
- definitions using it: **43**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Defines` | List of the shader defines altering the rendering |
| `ShowInIsolation` | If true rendering is limited only to materials with this debug view |
| `TargetOutput` | Define which view is gonna be used for the display of the material. Usually the debug value will be written into the albedo part of the GBuffer. In that case the output will be None - for lit version and Albedo - for non lit version |

## A real one

`Engine\Assets\Materials\DebugView\TriplanarLQ.def`

```json
{
  "Guid": "b5cbb8d7-5c3e-4dc4-a5ee-9d2876856038",
  "Defines": [
    {
      "Key": "7dabf884-a635-4ca5-a212-4787c234b8f4",
      "Value": {
        "Name": "LQ",
        "Value": ""
      }
    }
  ],
  "TargetOutput": "Albedo",
  "ShowInIsolation": false
}
```

Others: `TriplanarMQ`, `TriplanarCTR`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialDebugViewDefinitionObjectBuilder')
search_content('', type_contains='MaterialDebugViewDefinitionObjectBuilder')
```
