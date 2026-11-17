# BreakableModelComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Components.Models.BreakableModelComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Components.Models`
- definitions using it: **132**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FractureModel` | Model to display when the block is fractured. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\BreakableModelComponentDefinition.def`

```json
{
  "Guid": "131789f7-86ad-4c73-8c95-7cf17479cd09",
  "Model": "{G}1c9794c4-cdb1-4369-8101-1eae7923a51a",
  "Dummies": [],
  "FractureModel": "{G}695705ca-80a7-4120-94af-86170890065e"
}
```

Others: `Medium_Acacia01_ModelComponentDefinition`, `Palatine_Rock02_BreakableModelComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BreakableModelComponentDefinitionObjectBuilder')
search_content('', type_contains='BreakableModelComponentDefinitionObjectBuilder')
```
