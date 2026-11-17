# PointLightRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Render.Lights.PointLightRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Render.Lights`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LensFlare` | Optional artistic lens flare produced by the point light |

## A real one

`Vanilla\Assets\Blocks\Lights\PointLightRenderDefinition.def`

```json
{
  "Guid": "13368fb5-87b5-4441-9c11-ffb99e0834d9",
  "LightDummyType": "eb314b59-e80c-4554-a092-8b031d1aa8c4",
  "FlareDummyType": "136c1d0b-1e0a-4440-9f25-7fb47e4d491b",
  "LensFlare": "171b328f-95de-4d9b-bcf4-a9e35cef5dd0"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PointLightRenderDefinitionObjectBuilder')
search_content('', type_contains='PointLightRenderDefinitionObjectBuilder')
```
