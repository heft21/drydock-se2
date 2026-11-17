# GameInputLayersDefinitionObjectBuilder

`VRage:Keen.VRage.Input.GameInputLayersDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `NamedLayers` | An ordered collection of named input layers. The layers are processed in sequence, starting from the last one in the collection (highest index) to the first one (index 0). |

## A real one

`Vanilla\Assets\MainMenuData\Input\GameInputLayers.def`

Too large to inline. Fields present:

`Guid`, `NamedLayers`

---

Read it with the MCP server rather than by hand:

```
describe_type('GameInputLayersDefinitionObjectBuilder')
search_content('', type_contains='GameInputLayersDefinitionObjectBuilder')
```
