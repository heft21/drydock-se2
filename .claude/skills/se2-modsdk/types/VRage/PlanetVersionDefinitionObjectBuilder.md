# PlanetVersionDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetVersionDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `UseItemGeneratorHeightRangeFix` | Set to true for any planet newer than VS2.0 to fix heigh calculations when checking |
| `UseVS22Fixes` | Set to true for any planet newer than VS2.0 to apply additional generation fixes |
| `UseVS23Fixes` | Set to true for any planet newer than VS2.3 to apply ore surface-clearance fixes: configurable and a slope-correction cap via . |

## A real one

`Vanilla\Assets\Procedural\VS2_2\Planets\Common\PlanetVersionDefinition_VS2-2.def`

```json
{
  "Guid": "f36276b0-3b93-44b3-9391-38a0cb8f4099",
  "UseItemGeneratorHeightRangeFix": true,
  "UseVS22Fixes": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetVersionDefinitionObjectBuilder')
search_content('', type_contains='PlanetVersionDefinitionObjectBuilder')
```
