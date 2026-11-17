# DeathScreenAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Death.DeathScreenAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Death`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackgroundImage` | Background Image for death screen |
| `DeathFanfare` | Fanfare to show on the death screen |

## A real one

`Vanilla\Assets\UI\Screens\DeathScreenAvaloniaConfiguration.def`

```json
{
  "Guid": "e9100c78-889c-41e1-a3f3-4cc467ef4bf9",
  "BackgroundImage": "{G}ea616e8c-5aa6-499e-b417-d69009447294",
  "DeathFanfare": "8ceaa088-f2b5-4e64-9e7b-8ac6c4295f78"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DeathScreenAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='DeathScreenAvaloniaConfigurationObjectBuilder')
```
