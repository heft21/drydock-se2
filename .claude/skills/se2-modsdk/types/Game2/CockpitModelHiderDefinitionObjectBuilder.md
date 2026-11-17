# CockpitModelHiderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.ModelHiders.CockpitModelHiderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.ModelHiders`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Camera\CockpitFirstPersonCamera\CockpitCharacterHeadModelHider.def`

```json
{
  "Guid": "e554ee46-6ca8-425a-a903-6df0ecc9b1bc",
  "HidableRenderTag": "SkinnedThirdPersonRender",
  "ModelPartsToHide": [
    {
      "Key": "8106a077-48c7-4be9-ba7a-d744bf8b209c",
      "Value": "c3eec452-93ae-4d19-af33-c71ca4c524b1"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitModelHiderDefinitionObjectBuilder')
search_content('', type_contains='CockpitModelHiderDefinitionObjectBuilder')
```
