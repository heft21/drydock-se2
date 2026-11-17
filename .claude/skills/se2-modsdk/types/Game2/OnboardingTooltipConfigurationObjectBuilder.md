# OnboardingTooltipConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Shared.Mission.OnboardingTooltip.OnboardingTooltipConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Shared.Mission.OnboardingTooltip`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CloseTooltipAction` | The input action to close the tooltip This action should always be available in the tooltip input context |
| `CloseTooltipText` | The text telling the user how to close the tooltip |

## A real one

`Vanilla\Assets\UI\HUD\OnboardingTooltipConfiguration.def`

```json
{
  "Guid": "f072db2f-4f3f-45c7-aa8b-def1a5636adc",
  "CloseTooltipText": "OnboardingTooltipGenericClose",
  "CloseTooltipAction": "9cda2d89-202c-458e-bd48-32b7cf4a621f"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OnboardingTooltipConfigurationObjectBuilder')
search_content('', type_contains='OnboardingTooltipConfigurationObjectBuilder')
```
