# RespawnScreenAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Death.RespawnScreenAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Death`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackgroundImage` | Background Image for death screen |
| `HomeBlockLabel` | Label for showing the home block spawn point |
| `NearestBlockLabel` | Label for showing the nearest block spawn point |
| `RefreshButtonText` | Text shown on the refresh button |
| `RespawnButtonText` | Text shown on the respawn button |
| `ScreenTitle` | Title of the respawn screen |

## A real one

`Vanilla\Assets\UI\Screens\RespawnScreenAvaloniaConfiguration.def`

```json
{
  "Guid": "d1a38a77-02cc-421a-a6f9-6e778ae1051b",
  "BackgroundImage": "{G}ea616e8c-5aa6-499e-b417-d69009447294",
  "ScreenTitle": "RespawnDialogTitle",
  "HomeBlockLabel": "RespawnDialogHomeBlock",
  "NearestBlockLabel": "RespawnDialogNearestBlock",
  "RefreshButtonText": "RespawnScreenRefresh",
  "RespawnButtonText": "RespawnScreenRespawn"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RespawnScreenAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='RespawnScreenAvaloniaConfigurationObjectBuilder')
```
