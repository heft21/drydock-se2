# BackpackItemConverterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.BackpackItemConverterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RecipeDefinitions` | Collection of recipe definitions the backpack item converter can produce |
| `SpeedMultiplier` | Modifier that alters the speed items are converted |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\BackpackItemConverterDefinition.def`

```json
{
  "Guid": "f97a23f2-735a-4550-b830-23f2f0e5ed5c",
  "SpeedMultiplier": 0,
  "RecipeDefinitions": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BackpackItemConverterDefinitionObjectBuilder')
search_content('', type_contains='BackpackItemConverterDefinitionObjectBuilder')
```
