# FloraImpostorAtlasMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.FloraImpostorAtlasMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **181**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Environment\Planets\Verdure\Flora\VS2_3\Flora\Poplar\Texture\LargePoplar01_ImpostorAtlasFar.def`

```json
{
  "Guid": "31d5a663-fa19-4ba3-b177-da0cb10d2526",
  "DefaultState": "6c50a8e7-94f2-4b1d-8a36-d1e7b2c9f048",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "AlbedoTextureGuid": "c096a8dd-b4fa-4793-9be9-534e4fb5d96d",
  "LightingPositiveTextureGuid": "c096a8dc-b4fa-4793-9be9-534e4fb5d96d",
  "LightingNegativeTextureGuid": "c096a8df-b4fa-4793-9be9-534e4fb5d96d",
  "ExtensionsTextureGuid": "c096a8de-b4fa-4793-9be9-534e4fb5d96d",
  "ImpostorAtlasSize": 16,
  "Type": "FullSphere",
  "SideLightTilt": 30,
  "AlphaCutoutThreshold": 0.4,
  "ShadowBias": 1,
  "AOMultiplier": 1,
  "LightingContrast": 1.5,
  "LightingRangeMin": 0.1,
  "LightingRangeMax": 0.6
}
```

Others: `LargePoplar02_ImpostorAtlasFar`, `LargePoplar01_ImpostorAtlasNear`

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraImpostorAtlasMaterialDefinitionObjectBuilder')
search_content('', type_contains='FloraImpostorAtlasMaterialDefinitionObjectBuilder')
```
