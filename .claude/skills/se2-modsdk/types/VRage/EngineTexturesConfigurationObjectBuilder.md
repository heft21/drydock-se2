# EngineTexturesConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.EngineTexturesConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultAlphaMaskTexture` | Backup texture used in case there is a missing resource passed into UI rendering |

## A real one

`Engine\Assets\Configurations\Setup\EngineTexturesConfiguration.def`

```json
{
  "Guid": "fa4edcfa-51b2-47d5-a68f-0807c13bfd9f",
  "DefaultAlphaMaskTexture": "{G}602fc120-05ca-4b85-bdc9-ec2eea43c6ed"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EngineTexturesConfigurationObjectBuilder')
search_content('', type_contains='EngineTexturesConfigurationObjectBuilder')
```
