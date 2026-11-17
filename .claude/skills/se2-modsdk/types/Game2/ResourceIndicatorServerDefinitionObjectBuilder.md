# ResourceIndicatorServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources.ResourceIndicatorServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Resources` | The resources that will be tracked |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\OxygenHydrdogen_ResourceIndicatorServerDefinition.def`

```json
{
  "Guid": "90cbfce6-ed99-43bc-b914-c7e75f6300d7",
  "Resources": [
    {
      "Key": "d16df869-84dc-4483-9906-e41dd4a4d322",
      "Value": "a0e12811-7f81-4735-aef4-b74ef0c2d395"
    },
    {
      "Key": "d955f40e-6dd2-4fed-b162-63640ee68285",
      "Value": "d129d38e-116d-4424-a1a8-bbb298ac9dba"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceIndicatorServerDefinitionObjectBuilder')
search_content('', type_contains='ResourceIndicatorServerDefinitionObjectBuilder')
```
