# MapPlanetCloudsMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.MapPlanetCloudsMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisplacementTexture` | Texture composed of Height (R) |
| `Lacunarity` | How quickly the frequency increases between layers |
| `Octaves` | How many layers of noise are used |
| `Persistence` | How quickly the contribution (amplitude) of each layer shrinks |

## A real one

`Vanilla\Assets\System\ColonizationMap\Models\Planets\EmptyCloudsColonization.def`

```json
{
  "Guid": "d7f2e11f-f10e-4772-9284-06a7aacb63c4",
  "DefaultState": "170ac8e4-4f37-453b-a7a7-40a38de2076c",
  "PinTextures": false,
  "DisplacementTexture": "{G}f2e6b973-ff87-41b7-b790-b81de2d3cfb3",
  "Octaves": 0,
  "Persistence": 0.3,
  "Lacunarity": 3
}
```

Others: `KemikCloudsColonization`, `VerdureCloudsColonization`

---

Read it with the MCP server rather than by hand:

```
describe_type('MapPlanetCloudsMaterialDefinitionObjectBuilder')
search_content('', type_contains='MapPlanetCloudsMaterialDefinitionObjectBuilder')
```
