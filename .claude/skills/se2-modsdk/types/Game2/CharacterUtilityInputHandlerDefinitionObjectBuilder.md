# CharacterUtilityInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.CharacterUtilityInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\CharacterUtilityInputAdapter.def`

```json
{
  "Guid": "726d0601-7a72-47ad-9557-2e0e484e8041",
  "InputContextDefinition": "cbbb6e6f-0c25-4d14-a824-75f77b5a1e41",
  "RespawnScreen": "c593bad2-40e6-432e-b61d-4bd5373cc009",
  "ToggleLightInput": "35eee78d-5fa0-4f15-b3f6-8b25a4db01f9",
  "HeadlightOnStat": "b4de981d-1ed7-4603-95c8-e76f6281a928",
  "HeadlightAutomaticModeStat": "73b66f23-d596-474c-b481-2ca6a1458990",
  "StatToggles": {}
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterUtilityInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='CharacterUtilityInputHandlerDefinitionObjectBuilder')
```
