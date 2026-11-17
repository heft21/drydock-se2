# AudioListenerComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Audio.Components.AudioListenerComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraTag` | Tag we should use to get camera world transform |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\AudioListenerComponentDefinition.def`

```json
{
  "Guid": "4c3752f4-bf94-49dd-8194-d6369c03f900",
  "CameraTag": "PhysicsObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioListenerComponentDefinitionObjectBuilder')
search_content('', type_contains='AudioListenerComponentDefinitionObjectBuilder')
```
