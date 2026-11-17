# ModelHiderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.ModelHiders.ModelHiderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.ModelHiders`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HidableRenderTag` | Tag of the render component this component will hide model parts on. If empty, a first viable component will be used. |
| `ModelPartsToHide` | Model parts that should be hidden so that they do not obscure the view of the camera. |

## A real one

`Vanilla\Assets\System\Camera\CharacterHeadModelHider.def`

```json
{
  "Guid": "673315cf-4606-4514-a38f-838d7b59d922",
  "HidableRenderTag": "SkinnedThirdPersonRender",
  "ModelPartsToHide": [
    {
      "Key": "a16dcb9c-1b57-4168-ac12-582879d33f20",
      "Value": "c3eec452-93ae-4d19-af33-c71ca4c524b1"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ModelHiderDefinitionObjectBuilder')
search_content('', type_contains='ModelHiderDefinitionObjectBuilder')
```
