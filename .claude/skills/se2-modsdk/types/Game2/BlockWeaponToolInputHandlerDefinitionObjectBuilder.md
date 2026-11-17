# BlockWeaponToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools.BlockWeaponToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultGroupName` | Default group name to use if the weapon tool doesn't have one |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\BlockWeaponInputAdapter\WeaponBlockToolInputAdapter_BlockWeaponToolInputHandlerDefinition.def`

```json
{
  "Guid": "b99ac22f-8cbf-4490-8610-de26118c0d9f",
  "InputContextDefinition": "c9a80415-b6aa-4b05-8daf-8403c2a26ac0",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": "f1789abd-986b-464a-9c2a-7ebd13c53c25",
  "ToolTertiary": null,
  "ToolPrimaryHint": "WeaponToolPrimaryHint",
  "ToolSecondaryHint": "WeaponToolReloadHint",
  "ToolTertiaryHint": "",
  "DefaultGroupName": "WeaponBlockToolDefaultName"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockWeaponToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='BlockWeaponToolInputHandlerDefinitionObjectBuilder')
```
