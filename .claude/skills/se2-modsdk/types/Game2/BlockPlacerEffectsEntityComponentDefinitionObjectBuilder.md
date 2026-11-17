# BlockPlacerEffectsEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer.BlockPlacerEffectsEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Tools\BlockPlacerEffectsEntityComponentDefinition.def`

```json
{
  "Guid": "007e6299-351a-4a5f-89a5-eb1ba16b3fee",
  "OnPlaceBlockAudio": "event:/UI/Block/PlaceBlock",
  "OnUnableAudio": "event:/UI/HudUnable",
  "OnRotateBlockAudio": "event:/UI/Block/RotateBlock"
}
```

Others: `PrefabBlockPlacerTool_BlockPlacerEffectsEntityComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacerEffectsEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockPlacerEffectsEntityComponentDefinitionObjectBuilder')
```
