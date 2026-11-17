# ArmorSkinDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Armor.Definitions.ArmorSkinDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Armor.Definitions`
- definitions using it: **17**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultMaterial` | Default material which is used whenever the armor block side doesn't specify a special or it is not found in |
| `SideMaterials` | Side specific material variants to be used together with |

## A real one

`Vanilla\Assets\ArmorSkins\HeavyArmorSkin.def`

```json
{
  "Guid": "738a1c90-5523-49b2-a79b-6cf4ea9e6ccc",
  "DefaultMaterial": "114061d3-5857-4a50-870e-15a4d3f206f8",
  "SideMaterials": {}
}
```

Others: `LigthArmorSkin`, `DefaultArmorSkin`

---

Read it with the MCP server rather than by hand:

```
describe_type('ArmorSkinDefinitionObjectBuilder')
search_content('', type_contains='ArmorSkinDefinitionObjectBuilder')
```
