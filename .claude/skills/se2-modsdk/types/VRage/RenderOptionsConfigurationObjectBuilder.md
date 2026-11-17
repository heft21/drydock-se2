# RenderOptionsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Options.RenderOptionsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Options`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorBevelMaterialOptions` | Material options for enabling/disabling armor bevels |
| `TerrainMaterialOptions` | Material options for the terrain preset. |
| `TransparentLightingMaterialOptions` | Material options for affecting lighting in the transparent pass |

## A real one

`Engine\Assets\Configurations\Setup\RenderOptionsConfiguration.def`

```json
{
  "Guid": "8828eee8-7534-4154-9ed8-5ae968d1a30b",
  "TerrainMaterialOptions": [
    {
      "Key": "5c488f6c-afd4-4dbc-980c-21b0ee788e1e",
      "Value": {
        "Options": "e31b268f-9b7c-44cd-a366-cdedf1c67814",
        "HighPresetOption": "High",
        "MediumPresetOption": "Medium",
        "LowPresetOption": "Low"
      }
    },
    {
      "Key": "a0b34ed2-fe8e-4eb9-a953-d5ef6b9e57b7",
      "Value": {
        "Options": "0795070b-6078-4704-a977-cbc1327ed6d2",
        "HighPresetOption": "On",
        "MediumPresetOption": "Off",
        "LowPresetOption": "Off"
      }
    }
  ],
  "ArmorBevelMaterialOptions": [
    {
      "Key": "f4510ea1-8477-45c8-b4e0-34ff2de9e159",
      "Value": {
        "Options": "4c271a08-e7c1-4a67-83f0-b0677504666b",
        "On": "On",
        "Off": "Off"
      }
    }
  ],
  "TransparentLightingMaterialOptions": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RenderOptionsConfigurationObjectBuilder')
search_content('', type_contains='RenderOptionsConfigurationObjectBuilder')
```
