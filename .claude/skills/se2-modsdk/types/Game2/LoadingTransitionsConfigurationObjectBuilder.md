# LoadingTransitionsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Overlays.LoadingTransitionsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Overlays`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Backgrounds` | Backgrounds to use for loading screens |
| `Texts` | Smart texts to show on loading screens |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\LoadingTransitionsConfiguration.def`

Too large to inline. Fields present:

`Backgrounds`, `Guid`, `Texts`

---

Read it with the MCP server rather than by hand:

```
describe_type('LoadingTransitionsConfigurationObjectBuilder')
search_content('', type_contains='LoadingTransitionsConfigurationObjectBuilder')
```
