# ArmorMesherConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Armor.Definitions.ArmorMesherConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Armor.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorMaterial` | Armor mesh material to be used in single-sided armors with no deformation - supports combining materials of different skins |
| `ArmorMaterialDoubleSided` | Armor mesh material to be used in double-sided armors with no deformation - supports combining materials of different skins |
| `DefaultArmorSkin` | Default armor skin |
| `SkinnedArmorMaterial` | Skinned Armor mesh material to be used in single-sided armors with deformations - supports combining materials of different skins |
| `SkinnedArmorMaterialDoubleSided` | Skinned Armor mesh material to be used in double-sided armors with deformations - supports combining materials of different skins |

## A real one

`Engine\Assets\Configurations\ArmorMesherConfiguration.def`

```json
{
  "Guid": "4e566aa3-fce0-459e-91c1-10f200a28382",
  "DefaultArmorSkin": "ef4ded67-bc0e-49d0-b62b-b89970f94778",
  "ArmorMaterial": "d3f3f63f-cfd3-45f5-ac52-529392655da5",
  "SkinnedArmorMaterial": "ba703c34-6b74-4a14-ae5d-0181bee024b9",
  "ArmorMaterialDoubleSided": "55cfa1d6-5c51-4692-9454-d22a896eea0e",
  "SkinnedArmorMaterialDoubleSided": "bfcdb121-3f13-4d29-a5bf-c98852900ffd"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ArmorMesherConfigurationObjectBuilder')
search_content('', type_contains='ArmorMesherConfigurationObjectBuilder')
```
