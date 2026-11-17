# CharacterLookOffsetDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterLookOffsetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxVerticalLookAngle` | Maximum vertical angle that the character can look to in degrees |
| `MinVerticalLookAngle` | Minimum vertical angle that the character can look to in degrees |

## A real one

`Vanilla\Assets\Characters\System\CharacterLookOffsetDefinition.def`

```json
{
  "Guid": "58e15cbe-2e39-4fa0-bc30-a4dc2317809b",
  "HorizontalAimClipAngle": 1.2217305,
  "MaxVerticalLookAngle": 1.3962634,
  "MinVerticalLookAngle": -1.5707964
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterLookOffsetDefinitionObjectBuilder')
search_content('', type_contains='CharacterLookOffsetDefinitionObjectBuilder')
```
