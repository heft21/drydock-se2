# GameInputConfigurationObjectBuilder

`VRage:Keen.VRage.Input.GameInputConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AliasGroups` | The alias groups for input controls. Used for resolving potential conflicts and overlaps between input controls. |
| `Layers` | Defines the structure and order of input layers in the input stack. Specifies how input is prioritized and processed across layers. |
| `Mapping` | The control mapping for the inputs. Defines how user actions are associated with specific controls. |

## A real one

`Vanilla\Assets\MainMenuData\Input\GameInputConfiguration.def`

```json
{
  "Guid": "a2a7ee6e-a77a-4312-a8f7-14a2f30d9a25",
  "Layers": "eb814602-f074-4664-b3bb-2345f62d4ce8",
  "Mapping": "6d13577c-a162-4429-a7b9-11338da0e99e",
  "AliasGroups": "8077dd92-4d77-4f6a-97a0-a3c12db87f76"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameInputConfigurationObjectBuilder')
search_content('', type_contains='GameInputConfigurationObjectBuilder')
```
