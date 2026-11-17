# LoadMenuScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.LoadMenu.LoadMenuScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu.LoadMenu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OpenAdvancedSettingsDisabledTooltip` | Tooltip explaining why advanced settings screen cannot be opened |
| `OpenAdvancedSettingsTooltip` | Tooltip for opening advanced settings screen |
| `OpenModManagementDisabledTooltip` | Tooltip explaining why mod management screen cannot be opened |
| `OpenModManagementTooltip` | Tooltip for opening mod management screen |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\LoadMenuScreenConfiguration.def`

```json
{
  "Guid": "c34788d4-021c-43b9-b129-ab33ce5deb11",
  "OpenAdvancedSettingsTooltip": "LoadMenuAdvancedSettingsTooltip",
  "OpenAdvancedSettingsDisabledTooltip": "LoadMenuAdvancedSettingsDisabledTooltip",
  "OpenModManagementTooltip": "LoadMenuManageModsTooltip",
  "OpenModManagementDisabledTooltip": "LoadMenuManageModsDisabledTooltip",
  "SaveNameCollisionResolutionSuffix": "SaveNameCollisionResolutionSuffix",
  "ExternalSaveName": "ExternalSaveName",
  "NeverPlayed": "LoadGameNeverPlayed"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LoadMenuScreenConfigurationObjectBuilder')
search_content('', type_contains='LoadMenuScreenConfigurationObjectBuilder')
```
