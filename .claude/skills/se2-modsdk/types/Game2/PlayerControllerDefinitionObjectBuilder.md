# PlayerControllerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerControllerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InputHandlers` | Defines what InputHandler prefab should be spawned for a combination of specific Controllable component and optionally SpecificKey provided by some implementations. Example: Controllable for Character and Welder require different InputHandlers, so based on the type of the Controllable, the correct prefab is selected. But there can for example be 2 different versions of the cockpit, where both use the same Controllable, but different InputHandler is expected. In this case it needs to be differentiated by SpecificKey which ties to SpecificKey provided by the Controllable. |

## A real one

`Vanilla\Assets\System\Controller\PlayerController.def`

Too large to inline. Fields present:

`Guid`, `InputHandlers`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlayerControllerDefinitionObjectBuilder')
search_content('', type_contains='PlayerControllerDefinitionObjectBuilder')
```
