# EnvironmentResourcesConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.EnvironmentResourcesConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Skybox` | Common skybox used in all situations. It is recommended to use HDR cubemap with dark background and bright stars to achieve the best visual fidelity. |
| `SunFlare` | Flare definition for the Sun |

## A real one

`Engine\Assets\Configurations\EnvironmentResourcesConfiguration.def`

```json
{
  "Guid": "3a0d742d-3672-46aa-a34c-0d01feba09f6",
  "Skybox": null,
  "SunFlare": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EnvironmentResourcesConfigurationObjectBuilder')
search_content('', type_contains='EnvironmentResourcesConfigurationObjectBuilder')
```
