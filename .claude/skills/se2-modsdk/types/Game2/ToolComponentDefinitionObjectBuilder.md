# ToolComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterOnly` | When true, only characters can equip the tool (spectator will not be able to equip the tool) |
| `CreativeOnly` | When true, the tool can only be equipped in creative mode |
| `DequipTime` | Amount of time it takes for the tool to be dequipped/stowed away. The tool will stop working immediately, but will be deleted only after the given time has elapsed. |
| `DisplayName` | Display name of the tool that is shown to the user. |
| `EquipTime` | Amount of time it takes for the tool to be equipped. The tool will be spawned immediately, but will only work after the given time has elapsed. |
| `Name` | Identifier of the tool, used i.e. for animation controller blackboard value |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\ToolComponentDefinition.def`

```json
{
  "Guid": "eda01aee-d53e-4de9-abdb-1cb2b96040aa",
  "Name": "HandWelder",
  "EquipTime": 2500000,
  "DequipTime": 2500000,
  "CharacterOnly": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolComponentDefinitionObjectBuilder')
search_content('', type_contains='ToolComponentDefinitionObjectBuilder')
```
