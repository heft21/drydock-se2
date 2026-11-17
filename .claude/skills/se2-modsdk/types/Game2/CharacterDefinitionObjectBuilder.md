# CharacterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterCrouchedHeight` | Height of the character while crouched |
| `CharacterHeadHeight` | Distance from character's feet to head center |
| `CharacterHeight` | Normal standing height of the character |

## A real one

`Vanilla\Assets\Characters\System\CharacterDefinition.def`

```json
{
  "Guid": "29ed7083-419b-4e67-ab49-48ebf34e8108",
  "CharacterHeight": 1.8,
  "CharacterHeadHeight": 1.65,
  "CharacterCrouchedHeight": 0.9
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDefinitionObjectBuilder')
search_content('', type_contains='CharacterDefinitionObjectBuilder')
```
