# FlareDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.FlareDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **8**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Intensity` | Multiplier on the strength of the flare brightness |
| `Size` | Multiplier of the size of all glares within the flare |
| `SubGlares` | All the individual glare elements that make up the lens flare |

## A real one

`Vanilla\Assets\Environment\Flares\Flare\WelderFlare.def`

Too large to inline. Fields present:

`Guid`, `Intensity`, `Size`, `SubGlares`

Others: `SunFlareDefinition`, `LargeFlareDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('FlareDefinitionObjectBuilder')
search_content('', type_contains='FlareDefinitionObjectBuilder')
```
