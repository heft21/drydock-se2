# PlanetEnvironmentRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.PlanetEnvironmentRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphereDefinition` | Definition of the atmosphere to use for planet rendering |
| `CloudDefinition` | Definition of the clouds to use for planet rendering |
| `Spherization` | Settings for planet spherization |

## A real one

`Vanilla\Assets\Environment\Planets\EarthLike\EarthEnvironmentRender.def`

```json
{
  "Guid": "b4bade70-5853-4045-bfc2-a31eb8b170cd",
  "Spherization": "a808ffea-5832-4354-a971-048832ddb31c",
  "AtmosphereDefinition": "da99a0c1-d731-4ed4-bc2b-d1ad95426e27",
  "CloudDefinition": "bb8d12cf-2031-49f5-85f2-683d2da74cce"
}
```

Others: `MarsLikeAtmosphere Render`, `Testerran Atmosphere Render`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentRenderDefinitionObjectBuilder')
search_content('', type_contains='PlanetEnvironmentRenderDefinitionObjectBuilder')
```
