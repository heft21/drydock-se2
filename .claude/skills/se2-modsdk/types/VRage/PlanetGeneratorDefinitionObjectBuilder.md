# PlanetGeneratorDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetGeneratorDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackMap` | The BACK map asset for the height cubemap. |
| `DefaultMaterial` | The default voxel material used for the planet's terrain. Serves as the base for the planet, applied to areas without specific biome or material definitions. |
| `Detail` | Planet detail texture used to shape sloped terrain. Enhances the visual quality of slopes by providing finer surface details. |
| `DetailCubemap` | Optional detail cubemap. Provides extra surface detail, complementing the heightmap for more realistic terrain generation. |
| `DownMap` | The DOWN map asset for the height cubemap. |
| `FrontMap` | The FRONT map asset for the height cubemap. |
| `GravityFalloffPower` | TODO: Remove after stable deploy |
| `Heightmap` | Main sliced height cubemap for the planet. |
| `HillParams` | Controls the overall variation in terrain height for the planet based on the heightmap. The range is relative to the planet's radius. Example: - A minimum value of -0.03 means the lowest terrain will be 3% lower than the planet's radius. For a planet with a radius of 60,000 meters, this translates to the lowest terrain being 1,800 meters below sea level. - A maximum value of 0.12 means the highest terrain will be 12% higher than the planet's radius. For the same planet, this translates to the highest terrain being 7,200 meters above sea level. |
| `IsMoon` | Whether this body is a moon (orbits a planet rather than a star). Used by the colonization map to bias the moon's position outward from its parent planet. |
| `LeftMap` | The LEFT map asset for the height cubemap. |
| `MaterialGroups` | TODO: Remove after stable deploy |
| `MaterialsMaxDepth` | TODO: Remove after stable deploy |
| `MaterialsMinDepth` | TODO: Remove after stable deploy |
| `MaxAltimeter` | Controls the max value for the altimeter. The value is relative to the |
| `Name` | Name used for the planet. Note: Will be replaced with filename once the functionality is available. |
| `OreMappings` | TODO: Remove after stable deploy |
| `RightMap` | The RIGHT map asset for the height cubemap. |
| `SurfaceGravity` | TODO: Remove after stable deploy |
| `SurfaceMaterialTable` | TODO: Remove after stable deploy |
| `UpMap` | The UP map asset for the height cubemap. |
| `Version` | Optional definition to apply versionned fixed to planet generation. Should be specified for any planet created after VS2.0 |
| `ZeroGround` | Controls the baseline elevation of the planet's terrain relative to its radius that is used by the altimeter. The value is relative to the |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\PlanetGenerator.def`

```json
{
  "Guid": "3f9e5617-541e-43e5-ae01-e3392b19fcdb",
  "Name": "EarthLike",
  "Heightmap": "{G}2272dcb3-7f22-4c19-ae40-3400d980ceb9",
  "UpMap": "{G}9ccdb519-5dfd-451f-993f-c30e443e5c27",
  "DownMap": "{G}70057d58-9e21-44fc-bca6-a9e31e8db578",
  "LeftMap": "{G}03ac1c9b-91e5-45f5-be10-c854586d8422",
  "RightMap": "{G}2a268ae0-ae0f-4d2f-8e91-465485b873a9",
  "FrontMap": "{G}a080f33b-3e33-4ace-b6c9-72dcff17ea94",
  "BackMap": "{G}ff7c9a3d-4a25-43b9-a4d6-fa70f2a63575",
  "HillParams": {
    "Min": -0.01,
    "Max": 0.12
  },
  "ZeroGround": 0,
  "MaxAltimeter": 0.12,
  "DefaultMaterial": "2be020a3-440f-48ed-a62b-05274d52bcf4",
  "Detail": null,
  "DetailCubemap": "22ae874a-f601-4990-af20-987f57cf92a4",
  "Version": null,
  "IsMoon": false
}
```

Others: `ByblosGenerator `, `VerdureGenerator`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetGeneratorDefinitionObjectBuilder')
search_content('', type_contains='PlanetGeneratorDefinitionObjectBuilder')
```
