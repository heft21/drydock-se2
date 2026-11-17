# ActionControlMappingDefinitionObjectBuilder

`VRage:Keen.VRage.Input.ActionControlMappingDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ControlsPerAction` | A collection of input actions and their associated input controls. |

## A real one

`Vanilla\Assets\MainMenuData\Input\ActionControlMapping.def`

---

Read it with the MCP server rather than by hand:

```
describe_type('ActionControlMappingDefinitionObjectBuilder')
search_content('', type_contains='ActionControlMappingDefinitionObjectBuilder')
```
