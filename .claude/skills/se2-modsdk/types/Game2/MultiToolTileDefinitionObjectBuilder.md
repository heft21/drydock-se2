# MultiToolTileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.MultiToolTileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\Screens\GScreen\CharacterTools\Drills\DrillsMultiToolTileDefinition.def`

```json
{
  "Guid": "47d08ec0-bf78-4ca4-8ed8-83a49839f612",
  "Name": "ToolDrillGroup",
  "Order": 1,
  "Subcategories": [
    {
      "Key": "9bc1b5f7-7399-4b47-9a9a-8cc404232b31",
      "Value": "947ff8fd-c76f-4ea6-b839-d920e6c7c797"
    }
  ],
  "Icon": "{G}0a10550c-7e23-4863-aee3-5d3d803a5f1a",
  "Description": "ToolDrillGroupDesc",
  "Tools": [
    {
      "Key": "0c0da26e-1355-41df-b54c-8a17d0fb1eee",
      "Value": "7569b116-034d-4e1c-8445-fd3e6252ebb4"
    },
    {
      "Key": "be7541e1-3080-4eac-9861-46cb577a550b",
      "Value": "2f57501e-ab56-47ae-8889-b7a809dd6f9f"
    },
    {
      "Key": "db3eb941-d1ef-47dd-bd4b-89f1a37deeb9",
      "Value": "63d99ab7-4079-41c4-ac23-39e6f848c035"
    },
    {
      "Key": "22356fe7-5bb7-4a9a-babd-104aefd352e4",
      "Value": "13bef13e-8601-40c4-99f9-99bc7029d2a7"
    }
  ]
}
```

Others: `WeldersMultiToolTileDefinition`, `GrindersMultiToolTileDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MultiToolTileDefinitionObjectBuilder')
search_content('', type_contains='MultiToolTileDefinitionObjectBuilder')
```
