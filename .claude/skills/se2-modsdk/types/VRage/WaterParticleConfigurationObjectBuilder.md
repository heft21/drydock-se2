# WaterParticleConfigurationObjectBuilder

`VRage:Keen.VRage.Water.Client.WaterParticleConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Client`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DebugParticleEffect` | Debug particle effect used for development. |
| `DefaultGPUParticleEffect` | Default particle settings used by particles produced by gpu effects. |

## A real one

`Vanilla\Assets\System\Water\WaterParticleConfiguration.def`

```json
{
  "Guid": "049592fd-bdfa-4f26-b791-77910da959d0",
  "DebugParticleEffect": "2f633b0c-b381-48fb-81e9-9fd73b7c2aa3",
  "DefaultGPUParticleEffect": "6d2fa91b-39cf-4be2-a12c-3924d08f7551"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterParticleConfigurationObjectBuilder')
search_content('', type_contains='WaterParticleConfigurationObjectBuilder')
```
