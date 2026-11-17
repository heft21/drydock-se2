# WeaponBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Tools.WeaponBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\BlockTools\Weapons\WeaponBlockTool_Client_WeaponBlockToolControllableDefinition.def`

```json
{
  "Guid": "4951d3a1-65a8-4438-bd9d-c9fbbab668d2",
  "ConsumedInputKinds": [
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Utility",
    "Toolbar"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeaponBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='WeaponBlockToolControllableDefinitionObjectBuilder')
```
