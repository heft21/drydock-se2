# ItemRecipesDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters.ItemRecipesDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Recipes` | List of known recipes |

## A real one

`Vanilla\Assets\Blocks\Gearforge\250\AmmoItemRecipes.def`

```json
{
  "Guid": "22665bc0-5f58-4fbe-9ac1-493e08da4300",
  "Recipes": [
    {
      "Key": "32cc3285-5205-4710-9a7d-5ba9f9c7f5a2",
      "Value": "586926b0-425f-48e7-a61e-0d521e1a640a"
    },
    {
      "Key": "be9193e6-6ab8-46e9-9c5d-6f9b2a22c071",
      "Value": "3b7fe44f-bcb5-444d-8b1c-9da6985e1a3d"
    },
    {
      "Key": "f999bfc0-60f0-41d4-8163-7944d773a70d",
      "Value": "6a35eddc-9116-43b1-91c4-a716f083585b"
    },
    {
      "Key": "15f00960-e761-4a00-81e3-d21e3ec870e7",
      "Value": "0d9a3337-cd51-4bd0-9eb5-c0c5d3e5d651"
    },
    {
      "Key": "dc3e13d7-a262-4de4-96a7-84bdb065b782",
      "Value": "9b5f3c7e-88ac-4c76-b69f-ca520d713bde"
    }
  ]
}
```

Others: `ToolItemRecipes`, `WeaponItemRecipes`

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemRecipesDefinitionObjectBuilder')
search_content('', type_contains='ItemRecipesDefinitionObjectBuilder')
```
