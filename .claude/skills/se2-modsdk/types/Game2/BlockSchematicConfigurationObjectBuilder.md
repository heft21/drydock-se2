# BlockSchematicConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.BlockSchematics.BlockSchematicConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.BlockSchematics`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Items\BlockSchematics\System\BlockSchematicConfiguration.def`

```json
{
  "Guid": "9a591302-8779-43c7-af38-7d8143cf6a13",
  "NonConsumable": [
    "bb0a1acc-12fe-497b-864e-af9ba24d269c"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockSchematicConfigurationObjectBuilder')
search_content('', type_contains='BlockSchematicConfigurationObjectBuilder')
```
