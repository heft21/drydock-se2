# GameMenuConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.GameMenuConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\GameMenuConfiguration.def`

```json
{
  "Guid": "b4ef182b-8a55-464a-abd5-62eddd641aeb",
  "Continue": "MenuContinue",
  "NewGame": "MenuNewGame",
  "Load": "MenuLoad",
  "Multiplayer": "MenuMultiplayer",
  "Workshop": "MenuWorkshop",
  "Character": "MenuCharacter",
  "Settings": "MenuSettings",
  "Credits": "MenuCredits",
  "Save": "MenuSave",
  "SaveAs": "MenuSaveAs",
  "Publish": "MenuPublish",
  "Help": "MenuHelp",
  "ExitToMainMenu": "MenuExitToMainMenu",
  "Quit": "MenuQuit"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameMenuConfigurationObjectBuilder')
search_content('', type_contains='GameMenuConfigurationObjectBuilder')
```
