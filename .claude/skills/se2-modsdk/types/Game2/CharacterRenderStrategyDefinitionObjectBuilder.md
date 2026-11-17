# CharacterRenderStrategyDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterRenderStrategyDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterPerspective` | Should this model be considered part of the first or third person character, or neither if null |
| `DefaultChanges` | Specify preset that should be always hidden for this rendered model. |
| `InitialVisibility` | Should this model be visible when first added to the scene. |
| `Model` | Model to be rendered with this component. |
| `ShadowsEnabled` | Should this model cast shadows. |

## A real one

`Vanilla\Assets\Characters\System\RenderFirstPerson.def`

```json
{
  "Guid": "8a0c4459-865f-4083-9199-0a56595c4b5a",
  "Model": "877651a4-174f-42c3-98a9-a99a059efef8",
  "DefaultChanges": [
    {
      "Key": "411fc643-df0a-411e-a159-69464474615f",
      "Value": "c3eec452-93ae-4d19-af33-c71ca4c524b1"
    }
  ],
  "InitialVisibility": false,
  "CharacterPerspective": "None",
  "ShadowsEnabled": true
}
```

Others: `RenderThirdPerson`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterRenderStrategyDefinitionObjectBuilder')
search_content('', type_contains='CharacterRenderStrategyDefinitionObjectBuilder')
```
