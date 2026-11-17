# ArmorPreviewConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Armor.Definitions.ArmorPreviewConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Armor.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorPreviewMaterials` | Default material used to preview armor block. |
| `ArmorSidePreviewMaterial` | Material used to preview armor sides. This material must be regular material for simple models. |
| `Models` | List of models that can be chosen when previewing armor skins |

## A real one

`Engine\Assets\Configurations\Preview\ArmorPreviewConfiguration.def`

```json
{
  "Guid": "da805f5f-fe54-4797-9e95-42121d56c5d8",
  "ArmorPreviewMaterials": [],
  "ArmorSidePreviewMaterial": "7ffee518-dfb0-4efc-b9c5-9794e86d90b3",
  "Models": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ArmorPreviewConfigurationObjectBuilder')
search_content('', type_contains='ArmorPreviewConfigurationObjectBuilder')
```
