# FloraDebugMenuConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Client.DebugControls.FloraDebugMenuConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.DebugControls`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FloraItems` | Flora item definitions to use. |
| `FloraModels` | Flora models to use. |

## A real one

`Vanilla\Assets\System\Configurations\FloraDebugMenuConfiguration.def`

Too large to inline. Fields present:

`FloraItems`, `FloraModels`, `Guid`

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraDebugMenuConfigurationObjectBuilder')
search_content('', type_contains='FloraDebugMenuConfigurationObjectBuilder')
```
