# TargetingGridClientDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeGrids.TargetingGridClientDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Grid\Grid_Client_TargetingGridClientDefinition.def`

```json
{
  "Guid": "071b15af-07cd-483a-b865-c2119fbe0690",
  "DetectionRange": 1000,
  "TargetReticle": "{G}945a77c1-fb87-42b7-a637-81f03bb52c4d"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TargetingGridClientDefinitionObjectBuilder')
search_content('', type_contains='TargetingGridClientDefinitionObjectBuilder')
```
