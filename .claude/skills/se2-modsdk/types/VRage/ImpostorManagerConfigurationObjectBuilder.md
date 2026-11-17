# ImpostorManagerConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.ImpostorManagerConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ImpostorRenderingMaterial` | Common material to assigned to all impostors |

## A real one

`Engine\Assets\Configurations\Setup\ImpostorManagerConfiguration.def`

```json
{
  "Guid": "4e4933ff-5af3-4a34-8aff-a656aff2b00b",
  "ImpostorRenderingMaterial": "7a17c07a-c0b6-4236-ac63-bf869cdea7da"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ImpostorManagerConfigurationObjectBuilder')
search_content('', type_contains='ImpostorManagerConfigurationObjectBuilder')
```
