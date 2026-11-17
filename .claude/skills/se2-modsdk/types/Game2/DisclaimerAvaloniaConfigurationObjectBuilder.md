# DisclaimerAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Disclaimer.DisclaimerAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Disclaimer`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisclaimerImage` | Disclaimer Image |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\DisclaimerAvaloniaConfiguration.def`

```json
{
  "Guid": "9ae47d3d-5a86-437c-80a9-94dd021625df",
  "DisclaimerImage": "{G}d0221b01-83f3-4a47-ac32-be150d97ac14",
  "PatchNotesUrl": "https://kswh.link/se2-hostile-encounters",
  "PatchNotesText": "WhatsNew"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DisclaimerAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='DisclaimerAvaloniaConfigurationObjectBuilder')
```
