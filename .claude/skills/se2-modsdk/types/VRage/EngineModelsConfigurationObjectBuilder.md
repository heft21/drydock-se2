# EngineModelsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Models.EngineModelsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Models`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RTXLightImposterSphere` | Imposter model for lights in raytracing. |

## A real one

`Engine\Assets\Configurations\Setup\EngineModelsConfiguration.def`

```json
{
  "Guid": "29c0036e-e766-465e-b235-9135994ce9be",
  "RTXLightImposterSphere": "{G}f887bbb0-3d1a-4de2-8ed5-8ec87349983a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EngineModelsConfigurationObjectBuilder')
search_content('', type_contains='EngineModelsConfigurationObjectBuilder')
```
