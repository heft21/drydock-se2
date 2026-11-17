# ContextualHintDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.UI.ContextualHints.ContextualHintDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.UI.ContextualHints`
- definitions using it: **17**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\ContextualHints\ToggleJetpackContextualHintDefinition.def`

```json
{
  "Guid": "bfbf19e3-94f9-4dca-898d-01e05ea242cb",
  "Text": "JetpackTooltip",
  "Icon": "{G}0ff0d22e-fe98-4404-93d4-fd8f8e0b8091"
}
```

Others: `GrindContextualHintDefinition`, `CrouchContextualHintDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ContextualHintDefinitionObjectBuilder')
search_content('', type_contains='ContextualHintDefinitionObjectBuilder')
```
