# InventoryEffectsSessionComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Inventory.InventoryEffectsSessionComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Inventory`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterInventory` | Inventory definition to know if we are transferring to character or other inventory |
| `OnBackpackProductionStartAudio` | Audio event to play on a backpack production started One-shot sound |
| `OnChangeToolbarAudio` | Audio event to play when toolbar is switched One-shot sound |
| `OnChangeToolbarTileAudio` | Audio event to play when toolbar a toolbar tile is changed One-shot sound |
| `OnCharacterInventoryFullAudio` | Audio event to play when inventory is full One-shot sound |
| `OnInventoryFullAudio` | Audio event to play when inventory is full One-shot sound |
| `OnObjectClickAudio` | Audio event to play on picking up or transfering an item One-shot sound |
| `OnObjectDropAudio` | Audio event to play on dropping a block One-shot sound |
| `OnOpenRareLootContainerAudio` | Audio event to play when player opens a container with rare generated loot One-shot sound |
| `OnProductionErrorAudio` | Audio event to play on a production error One-shot sound |
| `OnProductionItemAddedAudio` | Audio event to play on adding a production item to the queue One-shot sound |
| `OnQuickMenuClosedAudio` | Audio event to play when quick menu is closed One-shot sound |
| `OnQuickMenuOpenAudio` | Audio event to play when quick menu is opened One-shot sound |
| `OnRemoveToolbarTileAudio` | Audio event to play when toolbar a toolbar tile is removed One-shot sound |
| `OnSearchGScreenAddAudio` | Audio event to play when a character is added to the GScreen search query One-shot sound |
| `OnSearchGScreenRemoveAudio` | Audio event to play when a character is removed from the GScreen search query One-shot sound |
| `OnSelectGScreenTileAudio` | Audio event to play when a tile is selected in GScreen One-shot sound |
| `OnTerminalScreenToggleAudio` | Audio event to play upon opening/closing the terminal screen. One-shot sound |
| `OnToolbarLoadUnloadAudio` | Audio event to play when toolbar is changing One-shot sound |
| `OnToolbarLoadUnloadParameter` | Parameter to use for toggling on/off |
| `OnToolbarLoadUnloadParameterOffValue` | Off value to send to |
| `OnToolbarLoadUnloadParameterOnValue` | Off value to send to |
| `OnToolbarTileActivatedAudio` | Audio event to play when player activates a toolbar tile action One-shot sound |
| `OnToolbarTileDeselectedAudio` | Audio event to play when player selects One-shot sound |
| `OnToolbarTileSelectedAudio` | Audio event to play when tile is selected One-shot sound |
| `TerminalScreenToggleParameter` | Parameter to use for toggling on/off |
| `TerminalScreenToggleParameterOffValue` | Off value to send to |

## A real one

`Vanilla\Assets\System\Configurations\InventoryEffectsSessionComponentConfiguration.def`

```json
{
  "Guid": "8bdd72bf-b54d-4a6d-99c4-70f3f5e5a328",
  "OnTerminalScreenToggleAudio": "event:/UI/ui_Terminal",
  "TerminalScreenToggleParameter": "OnOff",
  "TerminalScreenToggleParameterOffValue": "Off",
  "OnObjectClickAudio": "event:/SFX/Character/TakeItem",
  "OnChangeToolbarAudio": "event:/UI/Gscreen_toolbar_swap",
  "OnToolbarTileSelectedAudio": "event:/UI/toolbar_select",
  "OnToolbarTileActivatedAudio": "event:/SFX/Block/Button",
  "OnToolbarTileDeselectedAudio": "event:/UI/toolbar_unselect",
  "OnChangeToolbarTileAudio": "event:/UI/Gscreen_insert",
  "OnRemoveToolbarTileAudio": "event:/UI/toolbar_remove",
  "OnSelectGScreenTileAudio": "event:/UI/Gscreen_drag",
  "OnSearchGScreenAddAudio": "event:/UI/Gscreen_type",
  "OnSearchGScreenRemoveAudio": "event:/UI/Gscreen_type_delete",
  "OnQuickMenuOpenAudio": "event:/UI/ColorTool_menu_appear",
  "OnQuickMenuClosedAudio": "event:/UI/ColorTool_menu_disappear",
  "OnObjectDropAudio": "event:/SFX/Character/DropItem",
  "OnProductionItemAddedAudio": "event:/UI/AddItemToCue",
  "OnProductionErrorAudio": "event:/UI/ComponentMissing",
  "OnInventoryFullAudio": "event:/UI/HudUnable",
  "OnCharacterInventoryFullAudio": "event:/UI/SuitInventoryFull",
  "CharacterInventory": "fe9df47f-5673-4253-b797-54635d4f3f42",
  "OnOpenRareLootContainerAudio": "event:/UI/Loot_box_reward",
  "OnBackpackProductionStartAudio": "event:/UI/ui_backpack_build",
  "OnToolbarLoadUnloadAudio": "event:/UI/toolbar_load_unload",
  "OnToolbarLoadUnloadParameter": "OnOff",
  "OnToolbarLoadUnloadParameterOnValue": "On",
  "OnToolbarLoadUnloadParameterOffValue": "Off"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryEffectsSessionComponentConfigurationObjectBuilder')
search_content('', type_contains='InventoryEffectsSessionComponentConfigurationObjectBuilder')
```
