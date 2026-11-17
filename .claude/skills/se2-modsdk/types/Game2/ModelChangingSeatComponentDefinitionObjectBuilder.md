# ModelChangingSeatComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit.ModelChangingSeatComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HidableRenderTag` | Tag of the component on pilot's entity implementing that this component will use to hide the preset on. |
| `PilotPresetToHide` | Defines what model part preset should be hidden for pilot. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ModelChangingSeatComponentDefinition.def`

```json
{
  "Guid": "1ea19763-d44a-43ee-b099-1414cfde8446",
  "SeatType": {
    "Id": "0"
  },
  "PilotDummy": "a28b206d-33f2-46f5-b018-2445b1d6ae4b",
  "SeatDummy": "8e581544-8c74-4c85-be9f-5e175f2792c1",
  "PilotPresetToHide": "cc221cf4-a2ef-4b26-98ba-8c3d81646e08",
  "HidableRenderTag": "SkinnedThirdPersonRender"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ModelChangingSeatComponentDefinitionObjectBuilder')
search_content('', type_contains='ModelChangingSeatComponentDefinitionObjectBuilder')
```
