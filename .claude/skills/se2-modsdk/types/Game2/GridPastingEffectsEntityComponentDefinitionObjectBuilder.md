# GridPastingEffectsEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer.GridPastingEffectsEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Tools\PrefabGridPastingTool_GridPastingEffectsEntityComponentDefinition.def`

```json
{
  "Guid": "221c3e1a-15c9-4d60-bac4-446167dc54e2",
  "OnPlaceBlockAudio": null,
  "OnUnableAudio": "event:/UI/HudUnable",
  "OnRotateBlockAudio": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridPastingEffectsEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='GridPastingEffectsEntityComponentDefinitionObjectBuilder')
```
