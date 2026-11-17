# TutorialOverlayConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Tutorial.TutorialOverlayConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Tutorial`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ContinueInputAction` | They key to press to continue to next step |
| `ContinueText` | Default text to display as continue instruction |
| `DefaultConnectorStyle` | Default style applied to connectors with no per-step style override |
| `DefaultSpotlightDimLayerColor` | Default color of the dim layer drawn around spotlights when a step does not override it |
| `DefaultSpotlightStyle` | Default style applied to spotlights with no per-step style override |
| `InputLayer` | Input layer of tutorial overlay |
| `PassthroughActions` | List of input actions this layer won't block |

## A real one

`Vanilla\Assets\UI\Tutorials\TutorialOverlayConfiguration.def`

```json
{
  "Guid": "839de52b-d092-49ba-94ee-43f636cffae9",
  "DefaultSpotlightStyle": "b8f9a111-b269-4d07-a949-47145c264138",
  "DefaultConnectorStyle": "b1628341-0419-4bef-8bd6-af6a1af3a3c8",
  "DefaultSpotlightDimLayerColor": {
    "PackedValue": 4026531840
  },
  "InputLayer": "Tutorial",
  "PassthroughActions": [],
  "ContinueInputAction": "1d872e88-12fc-4d50-8a12-121b18ba4498",
  "ContinueText": "TutorialPressKeyToContinue",
  "SkipHoldTime": 7500000,
  "SkipText": "TutorialSkipping",
  "SkipHintText": "TutorialHoldKeyToSkip"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TutorialOverlayConfigurationObjectBuilder')
search_content('', type_contains='TutorialOverlayConfigurationObjectBuilder')
```
