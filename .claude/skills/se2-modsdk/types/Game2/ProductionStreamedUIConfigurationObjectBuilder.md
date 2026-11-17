# ProductionStreamedUIConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Terminal.Production.ProductionStreamedUIConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Terminal.Production`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\ProductionStreamedUIConfiguration.def`

```json
{
  "Guid": "e20edcab-e8da-4816-b22d-0200bd2e1448",
  "AutomaticRecipeParentNote": "ProductionScreenAutomaticRecipeParentNote",
  "AutomaticRecipeChildrenNote": "ProductionScreenAutomaticRecipeChildrenNote"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProductionStreamedUIConfigurationObjectBuilder')
search_content('', type_contains='ProductionStreamedUIConfigurationObjectBuilder')
```
