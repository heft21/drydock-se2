# ItemConverterRecipeCategoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters.ItemConverterRecipeCategoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters`
- definitions using it: **8**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisplayName` | The localization string displayed in the production screen |

## A real one

`Vanilla\Assets\System\ItemConverters\Ammo.def`

```json
{
  "Guid": "96f6314c-b889-42cb-95d7-c2109b57324c",
  "DisplayName": "ItemConverterAmmoCat"
}
```

Others: `Tools`, `Blocks`

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemConverterRecipeCategoryDefinitionObjectBuilder')
search_content('', type_contains='ItemConverterRecipeCategoryDefinitionObjectBuilder')
```
