# AnimationPreviewModelConfigurationObjectBuilder

`VRage:Keen.VRage.Animation.Client.Preview.AnimationPreviewModelConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Client.Preview`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Model` | The model asset to be used for animation previews. |

## A real one

`Engine\Assets\Configurations\Preview\AnimationPreviewModelConfiguration.def`

```json
{
  "Guid": "328d335a-519d-41b8-92c7-349e2d52368c",
  "Model": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AnimationPreviewModelConfigurationObjectBuilder')
search_content('', type_contains='AnimationPreviewModelConfigurationObjectBuilder')
```
