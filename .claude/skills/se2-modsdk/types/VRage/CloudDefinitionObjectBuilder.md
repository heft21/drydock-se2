# CloudDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.CloudDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmbientPlanetAlbedo` | How much light should be reflected by the planet surface. Used to approximate the lighting of the dark side of clouds during day, facing away from the sun. Value of earth, without clouds, is 0.15 |
| `BeerCoefficient` | Coefficient affecting how much light clouds absorb. Higher values means thick clouds darken more aggressively from self-occluding sunlight. |
| `BiomeCoverageMult` | Sets the contribution of the biome to coverage |
| `BiomeDensityInfluence` | Sets the contribution of the biome to density |
| `BiomeTexture` | Biome cubemap texture; should be mapped to the biomes on the planet itself. Adds coverage (r) and multiplies density (g) Generally advisable to use a low resolution texture for performance purposes |
| `CloudTint` | Color multiplier on the clouds. Used for clouds with impurities that might cause them to not be exactly white to sunlight. White is preferred for earth-like clouds. |
| `CoverageMax` | The max value of coverage (usually best set above 1, so combined coverage can reach full, or 1, more often) |
| `CoverageMin` | The min value of coverage (usually best set below 0, so combined coverage can reach none, or 0, more often) |
| `DensityVariation` | Density variation. Higher values allow the "minimum density" of the clouds to be lower. |
| `HenyeyGreensteinEccentricity` | Coefficient affecting the eccentricity of the cloud scattering. Higher values allow the sun to shine brighter through low density clouds. Combine high values of this with high values of for a "silver lining" effect. High values are generally preferred. 0.99 is preferred for earth-like clouds. |
| `HenyeyGreensteinScattering` | Controls the factor at which front and back scattering evens out as density increases. Higher values create a strong "silver lining" effect. 1.0 looks good for earth-like clouds. |
| `MaxDensity` | Maximum density of the clouds. Higher density clouds are "bolder" looking and lower density clouds are "softer". |
| `NightAddedLight` | Unused... made more sense to move to frame settings since it is calibrated along side the skybox brightness. |
| `SampleGradientNoiseFrequency` | Increases the frequency of the gradient noise. This wide scale noise is responsible for making clouds be present or not present depending on probability. |
| `SampleMicroNoiseBalance` | Sets the balance of different levels in the small scale noise. This noise is responsible for the smaller details of the clouds. Values X, Y, and Z control the influence of large, medium and small noise. Values should be more than 0 and will be normalized to add up to 1. |
| `SampleMicroNoiseFrequency` | Increases the frequency of the small scale noise. This noise is responsible for the smaller details of the clouds. Higher values make smaller noise. |
| `SampleMicroNoiseInfluence` | Sets the overall influence of micro noise on the clouds |
| `SampleVoronoiNoiseBalance` | Sets the balance of different levels in the large scale voronoi noise. This noise is responsible for the "bubbly" aspect of cloud shape. Values X, Y, and Z control the influence of large, medium and small noise. Values should be more than 0 and will be normalized to add up to 1. |
| `SampleVoronoiNoiseFrequency` | Increases the frequency of the large scale voronoi noise. This noise is responsible for the "bubbly" aspect of cloud shape. Higher values make smaller noise. |
| `SampleVoronoiNoiseInfluence` | Sets the overall influence of voronoi noise on the clouds |
| `ShapeLUT` | Cloud shape lookup texture. Input X-> is coverage (from weather/biome), input Y^ is height. Output is cloud probability (r) and cloud density (g). Please use a low resolution texture for this to avoid performance issues (32x32 is recommended). Probability should go to 0 towards the left side of the texture so a coverage value of 0 results in no clouds rendered. |
| `ShellStartHeight` | Height, as a multiple of planet radius, above or below sea level where the clouds start |
| `ShellThickness` | Thickness, as a multiple of planet radius, of the cloud shell |
| `WeatherOverlays` | Weather overlays that are composited into the weather map |

## A real one

`Vanilla\Assets\Environment\Planets\Verdure\Clouds\VerdureClouds.def`

```json
{
  "Guid": "bb8d12cf-2031-49f5-85f2-683d2da74cce",
  "CloudTint": {
    "PackedValue": 4294967295
  },
  "HenyeyGreensteinEccentricity": 0.99,
  "HenyeyGreensteinScattering": 1,
  "BeerCoefficient": 0.1,
  "AmbientPlanetAlbedo": 0.1,
  "NightAddedLight": 0.1,
  "MaxDensity": 20000,
  "DensityVariation": 6,
  "ShellStartHeight": 0.04,
  "ShellThickness": 0.04,
  "CoverageMin": -0.25,
  "CoverageMax": 1.25,
  "BiomeTexture": "{G}433f364f-0250-4400-8832-6fcf29d2316c",
  "BiomeCoverageMult": 1,
  "BiomeDensityInfluence": 1,
  "WeatherOverlays": [
    {
      "Key": "6d2aa9a8-3065-4427-a3fc-f6b945ee6432",
      "Value": {
        "OverlayTexture": "{G}7b4e7665-ddb7-45b9-a8d7-7f4520688d22",
        "RotationAxis": {
          "X": 1,
          "Y": 0,
          "Z": 0
        },
        "RotationSpeed": 0.0004,
        "CoverageInfluence": 1,
        "DensityInfluence": 0.2
      }
    }
  ],
  "ShapeLUT": "{G}b7efdb23-2047-4cf2-a6ba-a862f7b006e0",
  "SampleGradientNoiseFrequency": 5,
  "SampleVoronoiNoiseFrequency": 5,
  "SampleVoronoiNoiseBalance": {
    "X": 1,
    "Y": 0.5,
    "Z": 0.25
  },
  "SampleVoronoiNoiseInfluence": 1,
  "SampleMicroNoiseFrequency": 80,
  "SampleMicroNoiseBalance": {
    "X": 1,
    "Y": 0.5,
    "Z": 0.25
  },
  "SampleMicroNoiseInfluence": 0.6
}
```

Others: `Titan_CloudDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CloudDefinitionObjectBuilder')
search_content('', type_contains='CloudDefinitionObjectBuilder')
```
