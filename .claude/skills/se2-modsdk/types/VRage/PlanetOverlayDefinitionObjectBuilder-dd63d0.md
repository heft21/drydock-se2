# PlanetOverlayDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.PlanetOverlayDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **8**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Engine\Assets\Preview\Voxels\PlanetOverlayDefinition.def`

```json
{
  "Guid": "f02c5807-fa1d-45e8-9d43-933d7be08f3e",
  "OverlayColorMetal": "{G}65981052-c392-4ed2-843c-a2c62b770453",
  "OverlayNormalAO": "{G}65981052-c392-4ed2-843c-a2c62b770453"
}
```

Others: `Kemik_Overlay`, `ByblosOverlay`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetOverlayDefinitionObjectBuilder')
search_content('', type_contains='PlanetOverlayDefinitionObjectBuilder')
```
