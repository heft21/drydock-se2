# OnboardingTooltipDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Missions.Onboarding.OnboardingTooltipDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Missions.Onboarding`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\OnboardingTooltipDefinition.def`

```json
{
  "Guid": "a1511c2e-13c6-49e3-9fc8-1ef0445061f3",
  "InputContext": null,
  "CompleteAction": null,
  "Icon": "{G}68f029d7-b90a-4655-884e-c9a70374c016",
  "Banner": null,
  "Name": "",
  "Description": "",
  "CallToAction": ""
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OnboardingTooltipDefinitionObjectBuilder')
search_content('', type_contains='OnboardingTooltipDefinitionObjectBuilder')
```
