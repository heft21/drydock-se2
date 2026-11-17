# ModConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Shared.UGC.Mods.ModConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Shared.UGC.Mods`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultThumbnail` | Default thumbnail to display on worlds without or with invalid thumbnails |
| `LoadGameText` | Action button text when the manage mod screen opened from the load game screen |
| `StartGameText` | Action button text when the manage mod screen opened from the details screen |

## A real one

`Vanilla\Assets\MainMenuData\UGC\Mods\ModConfiguration.def`

```json
{
  "Guid": "d126b6e0-1aea-4a38-bc3f-73e3735322c5",
  "DefaultThumbnail": "{G}2e5795a7-8c1d-4014-8bf8-01c0dc019bd3",
  "LoadGameText": "ManageModsScreenLoadGame",
  "StartGameText": "ManageModsScreenStartGame"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ModConfigurationObjectBuilder')
search_content('', type_contains='ModConfigurationObjectBuilder')
```
