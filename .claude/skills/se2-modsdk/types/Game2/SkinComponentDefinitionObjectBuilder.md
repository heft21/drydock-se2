# SkinComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.SkinComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultSkin` | The default skin applied to the character |

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_SkinComponentDefinition.def`

```json
{
  "Guid": "6c6bc4ae-5c0e-4515-aa74-737b7f9e9f13",
  "DefaultSkin": "2648eed6-3227-4f87-b2ea-257d7c115002",
  "PersistentSkin": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SkinComponentDefinitionObjectBuilder')
search_content('', type_contains='SkinComponentDefinitionObjectBuilder')
```
