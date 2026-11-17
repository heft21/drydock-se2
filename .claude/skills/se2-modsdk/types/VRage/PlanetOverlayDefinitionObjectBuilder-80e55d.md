# PlanetOverlayDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.PlanetOverlayDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OverlayColorMetal` | Cubemap texture containing the color and metallic properties of the planet's overlay. Define the base appearance of the planet, including its diffuse color and metallic surface qualities. |
| `OverlayNormalAO` | Cubemap texture containing the normal map and AO of the planet's overlay. Provides surface detail and ambient occlusion, ensuring realistic lighting effects for the planet when rendered at a distance. |

## A real one

`Vanilla\Assets\Procedural\VS2_2\Planets\Palatine\Data\Palatine_Overlay.def`

```json
{
  "Guid": "1717c97f-c19e-472a-8fcd-31cea5bc1f82",
  "OverlayColorMetal": "{G}3a77db64-ceb9-40e7-8e3c-870229cd4383",
  "OverlayNormalAO": "{G}ac820e85-9451-441d-a255-c90d8020b9ae"
}
```

Others: `Titan_Overlay_Overlay`, `Geomeles_Overlay_Overlay`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetOverlayDefinitionObjectBuilder')
search_content('', type_contains='PlanetOverlayDefinitionObjectBuilder')
```
