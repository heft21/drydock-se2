# CharacterControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | InputKinds that character controller is allowed to consume |
| `PassedInputKinds` | InputKinds that character controller is allowed to forward to other controllers further down the stack |

## A real one

`Vanilla\Assets\Characters\System\ComponentCharacterClient.def`

```json
{
  "Guid": "7bc703f4-d03c-4940-86b4-43321a8602de",
  "ConsumedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Tools",
    "Utility",
    "Toolbar"
  ],
  "PassedInputKinds": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterControllableDefinitionObjectBuilder')
search_content('', type_contains='CharacterControllableDefinitionObjectBuilder')
```
