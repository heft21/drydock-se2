# FmodTemplateConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.FmodTemplateConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MusicBankPath` | File path to the FMOD bank metadata xml relative to root |
| `MusicTemplate` | Should be a zip file with a .fstemplate extension, imported into the project. Should be prepared for music modding |
| `SfxBankPath` | File path to the FMOD bank metadata xml relative to root |
| `Template` | Should be a zip file with a .fstemplate extension, imported into the project |

## A real one

`Engine\Assets\Core\Audio\FmodTemplateConfiguration.def`

```json
{
  "Guid": "271663ec-d9c7-4504-8377-6bc2f574325d",
  "Template": "{G}5e3f8de0-35ac-4d3e-ac2c-678ccaeb6033",
  "MusicTemplate": "{G}e8d75c28-cf2e-4c45-af43-332a0cbc1069",
  "SfxBankPath": "Metadata/Bank/{a0564dcf-f494-40b2-a991-049a147d1866}.xml",
  "MusicBankPath": "Metadata/Bank/{802bfccc-6325-42b0-85e9-b5674933820d}.xml"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FmodTemplateConfigurationObjectBuilder')
search_content('', type_contains='FmodTemplateConfigurationObjectBuilder')
```
