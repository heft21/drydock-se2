# WorldSaveDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.RuntimeSystems.Worlds.WorldSaveDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.RuntimeSystems.Worlds`
- definitions using it: **6**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\MainMenuData\Scenarios\Scenario_CRF_WorldSaveDefinition.def`

```json
{
  "Guid": "607d033d-da07-449d-add9-44fee0b31f05",
  "World": {
    "SaveName": "CRF"
  }
}
```

Others: `Scenario_Survival_WorldSaveDefinition`, `Scenario_EmptyWorld_WorldSaveDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('WorldSaveDefinitionObjectBuilder')
search_content('', type_contains='WorldSaveDefinitionObjectBuilder')
```
