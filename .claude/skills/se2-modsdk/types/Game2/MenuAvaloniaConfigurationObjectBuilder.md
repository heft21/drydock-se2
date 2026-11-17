# MenuAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.MenuAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlphaBadge` | Alpha badge for the whole game |
| `BackIcon` | Left arrow icon for the back button |
| `CampaignBackground` | Background for Campaign on |
| `CreativeBackground` | Background for Creative on |
| `LineOrnamentBottomLeftTopRight` | A line ornament that goes from bottom left to top right |
| `LineOrnamentTopLeftBottomRight` | A line ornament that goes from top left to bottom right |
| `MenuBackground` | Background Image for Menu and others In-Menu screens |
| `MenuButtonBackground` | Background for Menu Button |
| `MenuButtonBackgroundDisabled` | Background for Menu Button when disabled |
| `MenuButtonsPanelBackground` | Buttons Panel Background for Main Menu |
| `MenuButtonsPanelOrnaments` | Buttons Panel Ornaments for Main Menu |
| `MenuHighlight` | Highlight image for the Main Menu |
| `MenuSortAscendingIcon` | Icon for ascending sort order |
| `MenuSortDescendingIcon` | Icon for descending sort order |
| `NewGameButtonBackground` | Background of the New-Game button |
| `NewGameButtonBackgroundDisabled` | Background of the New-Game button when Disabled |
| `OptionsScreenOrnament` | Ornament for the top part of a screen, with specific details for the Option Screen |
| `QuickStartBackground` | Background for Quick Start on |
| `SavePreviewFallback` | Fallback for unreadable save preview |
| `ScenarioBackground` | Background for Scenario on |
| `ScreenOrnament` | Ornament for the top part of a screen |
| `SmallMenuButtonBackground` | Background of the Small Button on Menu Screens |
| `SurvivalBackground` | Background for Survival on |
| `TabOrnamentB` | Tab Ornament Bottom |
| `TabOrnamentBBackground` | Tab Ornament Bottom Background |
| `TabOrnamentL` | Tab Ornament Left |
| `TabOrnamentR` | Tab Ornament Right |
| `TabOrnamentT` | Tab Ornament Top |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\MenuAvaloniaConfiguration.def`

```json
{
  "Guid": "55236e69-6fe5-4f32-a3ac-991d811a552c",
  "MenuBackground": "{G}0feaebbf-2e67-40db-9789-b02b80989214",
  "MenuHighlight": "{G}c47b34e6-4d6e-4829-838d-75ceb8ced62d",
  "QuickStartBackground": "{G}9c9077d5-c222-4543-a516-6c478adba9d6",
  "CampaignBackground": "{G}8e80d5c7-0d70-4f15-93f7-b58bd8aa51d5",
  "SurvivalBackground": "{G}43b8eda8-6f3a-4b6a-909f-b3b0029aee01",
  "CreativeBackground": "{G}2fe80f7d-3f23-4ca4-8358-f9b114fb33be",
  "ScenarioBackground": "{G}379be61e-0ec4-4905-b49f-f41f97af9b74",
  "MenuButtonsPanelBackground": "{G}8b221692-58d3-4abe-b3f5-358fdbf7c27e",
  "MenuButtonsPanelOrnaments": "{G}a56b9805-d12b-4725-bb46-ea5d5ec22068",
  "MenuButtonBackground": "{G}ce449419-4243-4cac-894e-686b61f43214",
  "MenuButtonBackgroundDisabled": "{G}65cb356e-a32a-40e7-8d0e-20efddd32144",
  "ScreenOrnament": "{G}48d23edc-83e5-4862-bf0a-37c0b7e47b92",
  "OptionsScreenOrnament": "{G}d9178459-8614-4710-9c89-b6f6f6dc915a",
  "TabOrnamentB": "{G}f3f4e3eb-cb70-4d7d-b40e-49ae6e0d4a11",
  "SavePreviewFallback": "{G}623808bc-3889-4d74-a78d-0553878b05ed",
  "AlphaBadge": "{G}4fec6c35-123d-49f5-995b-dbea39c35010",
  "MenuSortAscendingIcon": "{G}939e9bc0-cbb9-4a40-9b6f-de9434ffe297",
  "MenuSortDescendingIcon": "{G}a5118303-cf29-4afb-84cf-a260400fd1a0",
  "BackIcon": "{G}1b5bf214-72c5-4393-ad0b-1feeac63c2ab"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MenuAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='MenuAvaloniaConfigurationObjectBuilder')
```
