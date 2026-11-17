# ControlPanelConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Terminal.ControlPanel.ControlPanelConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Terminal.ControlPanel`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultGroupName` | Default name used as a suffix for the block name. |
| `DefaultPriority` | Used for detail types that have no priority associated with them. Lower priority means higher order in the list. |
| `DetailModelComponentToPriority` | Mapping of detail (view)model of components to their priority. Influences the order in which the detail views of components are displayed in the control panel. Lower priority means higher order in the list. |
| `NpcName` | Localization string of the NPC |

## A real one

`Vanilla\Assets\System\Configurations\ControlPanelConfiguration.def`

```json
{
  "Guid": "1beb8d4b-3131-4b95-96ae-b8ba85d653a7",
  "DetailModelComponentToPriority": {
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.FunctionalBlockComponent": 0,
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar.TimerBlockServerComponent": 0,
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar.EventControllerServerComponent": 0
  },
  "DefaultPriority": 4294967295,
  "DefaultGroupName": "TerminalScreenDefaultGroupName"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ControlPanelConfigurationObjectBuilder')
search_content('', type_contains='ControlPanelConfigurationObjectBuilder')
```
