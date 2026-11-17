# MaterialStatesPreviewConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.Previews.MaterialStatesPreviewConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Previews`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlphaBlendedBackgroundMaterial` | The material given to the background of the preview when viewing alpha blended materials |
| `PreviewCustomData` | Mapping for asset handle to the custom preview data definition. Each new > cannot be previewed unless we add the entry to this dictionary. |

## A real one

`Engine\Assets\Configurations\Preview\MaterialStatesPreviewConfiguration.def`

Too large to inline. Fields present:

`AlphaBlendedBackgroundMaterial`, `Guid`, `PreviewCustomData`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialStatesPreviewConfigurationObjectBuilder')
search_content('', type_contains='MaterialStatesPreviewConfigurationObjectBuilder')
```
