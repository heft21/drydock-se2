# CreditsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.CreditsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CreditsMusic` | Music to play during credits |
| `CreditsToolTip` | Represents the localization key for the credits |
| `CreditsVideo` | Represents credits video |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\CreditsConfiguration.def`

```json
{
  "Guid": "a8570447-68d6-409e-af95-84b51fad0f69",
  "CreditsVideo": "{G}39bacc68-ee6f-4d0e-92e4-3a7251982b11",
  "CreditsToolTip": "CreditsButtonTooltip",
  "CreditsMusic": "event:/Music/Credits/CreditsAstronautsUnite"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CreditsConfigurationObjectBuilder')
search_content('', type_contains='CreditsConfigurationObjectBuilder')
```
