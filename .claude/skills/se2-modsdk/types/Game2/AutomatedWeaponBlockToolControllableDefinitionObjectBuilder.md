# AutomatedWeaponBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Weapons.AutomatedWeaponBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Weapons`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | InputKinds consumed by cockpit |
| `PassedInputKinds` | InputKinds forwarded to other controllers further down the stack |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\AutomatedWeaponBlockToolControllableDefinition.def`

```json
{
  "Guid": "c491b702-1d20-485b-9896-79ffb96a5b0c",
  "ConsumedInputKinds": [
    "Rotation",
    "Toolbar",
    "Utility"
  ],
  "PassedInputKinds": [
    "Movement"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AutomatedWeaponBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='AutomatedWeaponBlockToolControllableDefinitionObjectBuilder')
```
