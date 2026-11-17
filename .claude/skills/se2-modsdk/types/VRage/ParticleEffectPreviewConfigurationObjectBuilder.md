# ParticleEffectPreviewConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.Previews.ParticleEffectPreviewConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Previews`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Models` | List of models that can be chosen when previewing decals |

## A real one

`Engine\Assets\Configurations\Preview\ParticleEffectPreviewConfiguration.def`

```json
{
  "Guid": "32cf6d3d-4e43-4932-a2f4-46f3865c33e4",
  "Models": [
    {
      "Key": "e021162d-9f48-4982-83da-451e3a4b01a6",
      "Value": "{G}e7e12ca9-ff5c-4a3f-af78-eac18813484b"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectPreviewConfigurationObjectBuilder')
search_content('', type_contains='ParticleEffectPreviewConfigurationObjectBuilder')
```
