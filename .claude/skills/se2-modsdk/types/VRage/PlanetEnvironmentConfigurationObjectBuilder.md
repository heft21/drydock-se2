# PlanetEnvironmentConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetEnvironmentConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FaceSize` | Helper value for easy computation of cell size |
| `PlanetSectorCutoff` | The percentage of the planet's radius after which no more depth sectors are created. |

## A real one

`Engine\Assets\Configurations\PlanetEnvironmentConfiguration.def`

```json
{
  "Guid": "013d61bc-345a-4a61-b3fe-cbf4ad4dcf0e",
  "PlanetSectorCutoff": 0.3,
  "FaceSize": 720
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentConfigurationObjectBuilder')
search_content('', type_contains='PlanetEnvironmentConfigurationObjectBuilder')
```
