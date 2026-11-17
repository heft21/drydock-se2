# SpotLightRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Render.Lights.SpotLightRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Render.Lights`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CookieTexture` | Optional texture projected by the spotlight |
| `LensFlare` | Optional artistic lens flare produced by the spotlight |
| `TryForceAllocateShadowMap` | Gives higher priority for this light when it comes to shadow map allocation, as a result the renderer will try to always keep a shadow map for this light. |

## A real one

`Vanilla\Assets\Blocks\Lights\SpotLightRenderDefinition.def`

```json
{
  "Guid": "2a0baaa7-1166-499b-a019-1fee6d2611e2",
  "LightDummyType": "eb314b59-e80c-4554-a092-8b031d1aa8c4",
  "FlareDummyType": "136c1d0b-1e0a-4440-9f25-7fb47e4d491b",
  "CookieTexture": null,
  "LensFlare": "171b328f-95de-4d9b-bcf4-a9e35cef5dd0",
  "TryForceAllocateShadowMap": false
}
```

Others: `PlayerSpotlightRenderComponent`, `SpectatorSpotlightRenderComponent`

---

Read it with the MCP server rather than by hand:

```
describe_type('SpotLightRenderDefinitionObjectBuilder')
search_content('', type_contains='SpotLightRenderDefinitionObjectBuilder')
```
