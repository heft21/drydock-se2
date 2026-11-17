# LegacyBlueprintImporterConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Blueprints.LegacyBlueprintImporterConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Blueprints`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GridImportFailureMessage` | Message shown when a grid fails to import |
| `GridImportFailureMessageContent` | Content of the message shown when a grid fails to import with a parameter for the grid name (name) |
| `GridImportMessage` | Message shown when a grid is successfully imported |
| `GridImportMessageContent` | Content of the message shown when a grid is successfully imported with a parameter for the grid name (name) |
| `NotificationTimeout` | Timeout for import notifications |

## A real one

`Vanilla\Assets\MainMenuData\UGC\Blueprints\LegacyBlueprintImporterConfiguration.def`

```json
{
  "Guid": "8d9b5006-df00-4493-ae8b-d3e07c6b617e",
  "NotificationTimeout": 50000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LegacyBlueprintImporterConfigurationObjectBuilder')
search_content('', type_contains='LegacyBlueprintImporterConfigurationObjectBuilder')
```
