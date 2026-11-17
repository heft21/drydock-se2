# CharacterDeathClientComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterDeathClientComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackCharacterPreset` | Preset on character model to hide when backpack is detached |
| `GravityAfterDeath` | The gravity types that will affect character entity after death. |
| `StatsToDisable` | Stats on the entity that will be set to minimum value when the character dies. |

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_CharacterDeathClientComponentDefinition.def`

```json
{
  "Guid": "822edf24-b386-43f9-81c3-89e11754145e",
  "BackpackCharacterPreset": "cc221cf4-a2ef-4b26-98ba-8c3d81646e08",
  "StatsToDisable": [
    {
      "Key": "a711d81d-52f0-4b1c-80de-fe0d07b5f8d0",
      "Value": "b4de981d-1ed7-4603-95c8-e76f6281a928"
    }
  ],
  "GravityAfterDeath": "41493979-f3d6-4b5c-b8b7-970adad7b42c"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDeathClientComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterDeathClientComponentDefinitionObjectBuilder')
```
