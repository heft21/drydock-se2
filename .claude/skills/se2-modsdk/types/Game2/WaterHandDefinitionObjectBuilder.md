# WaterHandDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.Toolbar.WaterEdit.WaterHandDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents.Toolbar.WaterEdit`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Creative Tools\Water Hand\WaterHand.def`

```json
{
  "Guid": "28bf48c0-3171-4eb6-b918-7ad66dc88bdd",
  "InputContextDefinition": "7dee05de-97e8-4c80-95df-92df40517dbb",
  "WaterEditPrimary": "9b669c09-2fbe-4960-9914-ddf408913381",
  "WaterEditSecondary": "571669cd-d93f-4e81-b471-4a2ffc84c4be",
  "WaterEditChangeDistance": "4aaa5f97-b675-4aed-aa4d-016a9311bf69",
  "ConsumedInputKinds": [
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Utility",
    "Toolbar"
  ],
  "DefaultBrushDistance": 20,
  "WaterOperatorPrefab": "e92b9cd2-567f-4583-a178-df1a71ecd3d5"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterHandDefinitionObjectBuilder')
search_content('', type_contains='WaterHandDefinitionObjectBuilder')
```
