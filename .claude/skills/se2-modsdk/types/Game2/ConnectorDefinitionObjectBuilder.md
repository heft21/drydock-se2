# ConnectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.ConnectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ConnectorDefinition.def`

```json
{
  "Guid": "e416ff60-273e-47f2-a9fc-a0918cea821e",
  "ConnectionGroups": [
    {
      "Key": "888bb17e-9e7f-4123-a132-6e398a96d210",
      "Value": "262d50d2-7b5b-4939-a81b-70f731d0e252"
    },
    {
      "Key": "64bbba0f-d382-4de5-8fe2-f5f6b67767f4",
      "Value": "a5bd777b-b184-41c9-af22-284d7178c267"
    }
  ],
  "ConnectorSize": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConnectorDefinitionObjectBuilder')
search_content('', type_contains='ConnectorDefinitionObjectBuilder')
```
