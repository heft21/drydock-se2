# LoadingWheelAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Controls.CustomControls.LoadingWheel.LoadingWheelAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Controls.CustomControls.LoadingWheel`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InnerPlanet` | Inner planet asset |
| `MiddlePlanet` | Middle planet asset |
| `OuterPlanet` | Outer planet asset |
| `SpinnerCore` | Spinner core asset |
| `SpinnerPlanet` | Spinner planet asset |
| `StarAndLines` | Asset of lines, sun and most outer planet |

## A real one

`Vanilla\Assets\MainMenuData\UI\LoadingWheel\LoadingWheelAvaloniaConfiguration.def`

```json
{
  "Guid": "404de23e-bdcb-49b7-85c0-be5705987449",
  "SpinnerCore": "{G}f83aefd6-1fe7-4904-8dca-b1b3e7291e04",
  "SpinnerPlanet": "{G}3ddd5333-6ada-48d2-bb83-908032aed62c",
  "InnerPlanet": "{G}f77fe010-0bb0-4a1c-9056-8d3bfe8519f4",
  "MiddlePlanet": "{G}9571141c-708e-45cd-ad0d-c8a07796d817",
  "OuterPlanet": "{G}be624c83-4728-4ad8-a4fb-470962c00efd",
  "StarAndLines": "{G}00645a81-51b7-47ab-b862-f453b7db62ee"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LoadingWheelAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='LoadingWheelAvaloniaConfigurationObjectBuilder')
```
