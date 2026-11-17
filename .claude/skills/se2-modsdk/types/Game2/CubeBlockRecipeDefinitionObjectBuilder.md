# CubeBlockRecipeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockRecipeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **18**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BuildTimePerItem` | Will be further scaled by tools that open on the block |
| `CriticalItems` | List of critical items to build the CubeBlockComponent |
| `OptionalItems` | List of optional items to build the CubeBlockComponent |

## A real one

`Vanilla\Assets\Blocks\Timer\50\Timer50RecipeDefinition.def`

```json
{
  "Guid": "6e3ac5b6-0b6a-41c8-b7c0-8743ae3aded8",
  "CriticalItems": [
    {
      "Key": "2f8191e3-56ce-494a-b60b-8fac9a01b8fc",
      "Value": {
        "Item": "824e331b-a798-479e-9276-5d35dc02df35",
        "Amount": 1
      }
    },
    {
      "Key": "e2e3f4cd-d573-438d-8507-83c0bb7da681",
      "Value": {
        "Item": "828c2c1e-25e0-44c7-870a-a20810725726",
        "Amount": 1
      }
    },
    {
      "Key": "6574489f-36d8-4074-ac3f-c4949f9bb1e9",
      "Value": {
        "Item": "616013e6-bbe2-44df-b762-9bcb79771238",
        "Amount": 5
      }
    }
  ],
  "OptionalItems": [
    {
      "Key": "e87bcdf7-6116-4148-ac0c-4deea6d31c84",
      "Value": {
        "Item": "824e331b-a798-479e-9276-5d35dc02df35",
        "Amount": 3
      }
    }
  ],
  "BuildTimePerItem": 3250000
}
```

Others: `RecipePlaceholder`, `SensorRecipeDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockRecipeDefinitionObjectBuilder')
search_content('', type_contains='CubeBlockRecipeDefinitionObjectBuilder')
```
