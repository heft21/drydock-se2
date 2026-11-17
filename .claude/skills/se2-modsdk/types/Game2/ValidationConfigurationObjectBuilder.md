# ValidationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Common.ValidationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Common`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InvalidInputKey` | Represents the localization key for invalid input scenarios. |
| `InvalidRangeKey` | Represents the localization key used to identify and handle invalid range validation scenarios. |

## A real one

`Vanilla\Assets\MainMenuData\UI\ValidationConfiguration.def`

```json
{
  "Guid": "a9077c4d-2b71-437b-8f0e-2e536cbc07c0",
  "InvalidInputKey": "ValidationInvalidInput",
  "InvalidRangeKey": "ValidationInvalidRange"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ValidationConfigurationObjectBuilder')
search_content('', type_contains='ValidationConfigurationObjectBuilder')
```
