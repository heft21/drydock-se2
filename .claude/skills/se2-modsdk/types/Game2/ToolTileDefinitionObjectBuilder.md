# ToolTileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.ToolTileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **18**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Description` | Tool description |
| `Icon` | The icon for the tool |
| `ToolPrefab` | The tool in this group |

## A real one

`Vanilla\Assets\CharacterTools\Rifle\Rifle_ToolTileDefinition.def`

```json
{
  "Guid": "6cd26304-7e61-4529-a072-e970bda99d55",
  "Name": "WeaponRifle",
  "Order": 0,
  "Subcategories": [
    {
      "Key": "550a764d-146a-4d97-85a3-9645e743e7b1",
      "Value": "2728efb4-4fc8-47f3-bf90-d371184c6d02"
    }
  ],
  "ToolPrefab": "eb2e3c27-2542-4274-adfc-a1c82dab9b47",
  "Icon": "{G}77974e4a-1627-4829-bf62-579f788c502e",
  "Description": "WeaponRifleDesc"
}
```

Others: `Pistol_ToolTileDefinition`, `DebugGunToolTileDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolTileDefinitionObjectBuilder')
search_content('', type_contains='ToolTileDefinitionObjectBuilder')
```
