# ParticleEmitterSettingsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.ParticleEmitterSettingsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtlasTexture` | The default texture used for particle emitters |

## A real one

`Engine\Assets\Configurations\Setup\ParticleEmitterSettingsConfiguration.def`

```json
{
  "Guid": "808144b0-478b-4ad2-a721-79bd372c8ac7",
  "AtlasTexture": "{G}a34787eb-67b0-400e-b8b5-c9720c91caf9"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEmitterSettingsConfigurationObjectBuilder')
search_content('', type_contains='ParticleEmitterSettingsConfigurationObjectBuilder')
```
