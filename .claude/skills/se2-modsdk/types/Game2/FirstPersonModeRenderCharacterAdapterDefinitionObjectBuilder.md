# FirstPersonModeRenderCharacterAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.FirstPersonModeRenderCharacterAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ThirdPersonHidePresets` | Presets that will be hidden on third person model when in first person camera view while First Person Mode is not active. This is used only for backwards compatibility. |

## A real one

`Vanilla\Assets\Characters\System\FirstPersonModeCharacterAdapter.def`

```json
{
  "Guid": "2ceab29c-d316-4538-970a-a3a626485692",
  "ThirdPersonHidePresets": [
    {
      "Key": "62b02cc6-1a9e-43d4-b67a-d0c4acae24a0",
      "Value": "c3eec452-93ae-4d19-af33-c71ca4c524b1"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FirstPersonModeRenderCharacterAdapterDefinitionObjectBuilder')
search_content('', type_contains='FirstPersonModeRenderCharacterAdapterDefinitionObjectBuilder')
```
