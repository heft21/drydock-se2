# ItemRecipeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters.ItemRecipeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters`
- definitions using it: **67**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DescriptionOverride` | The localization string displayed in the production screen |
| `DisplayNameOverride` | The localization string displayed in the production screen |
| `IconOverride` | If set, it will be used instead of the icon from the first output item. |
| `Inputs` | The items needed to produce another item. All the items must be present even if partial conversion is enabled |
| `Outputs` | The items produced/yielded |
| `TimeToConvert` | The time needed for the recipe to be completed without any speed modifiers |

## A real one

`Vanilla\Assets\Components\Simple\Wire\ItemRecipeSmelterWire.def`

```json
{
  "Guid": "881a6eba-85bb-4022-80d6-95b29968d22d",
  "DisplayNameOverride": null,
  "DescriptionOverride": null,
  "TimeToConvert": 5000000,
  "IconOverride": null,
  "Inputs": [
    {
      "Key": "1e97362a-17d2-44cf-9da2-2e4eeee24b8e",
      "Value": {
        "Item": "b51dc4d7-aaeb-4116-9f82-d54a33fe4b0a",
        "Amount": 20
      }
    }
  ],
  "Outputs": [
    {
      "Key": "246e6836-db66-48a4-994d-3c31e7789098",
      "Value": {
        "Item": "e1f56096-b043-4f8e-aca0-40423c54b603",
        "Amount": 1
      }
    }
  ]
}
```

Others: `ItemRecipeSmelterGlass`, `ItemRecipeSmelterMotor`

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemRecipeDefinitionObjectBuilder')
search_content('', type_contains='ItemRecipeDefinitionObjectBuilder')
```
