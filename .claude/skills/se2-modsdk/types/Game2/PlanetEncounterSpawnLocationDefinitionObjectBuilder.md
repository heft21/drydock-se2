# PlanetEncounterSpawnLocationDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounterSpawnLocationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnchorAlignmentAngle` | This affect where the planet can spawn relative to the encounter generation origin, reducing the angle between the spawn direction and the origin direction. |
| `Biomes` | The encounter will spawn on the planet's biome or anywhere if empty. |
| `HeightPlacementRule` | Specifies the percentage height range where the item can be placed. |
| `MaxDistance` | Maximum spawn distance from the origin. |
| `MinDistance` | Minimum spawn distance from the origin. |
| `Planet` | The encounter will spawn on the planet using this generator. |
| `PreciseSlopeHeightRange` | Specifies the percentage range of the detected slope height the item is allowed to spawn in. Note: Only applicable if is enabled. |
| `SlopePlacementRule` | Specifies the range of slope angle where the item can be placed. Determines the allowed inclinations for item placement, with 0 representing flat ground and 90 representing vertical surfaces. |
| `SupportedVoxelMaterials` | Materials on which this item can spawn. If empty, the item will spawn regardless of the material underneath |
| `UsePreciseSlopeRange` | When enabled, the system will consider the surrounding area's slope characteristics to determine suitable locations for item placement. It is recommended to always disable this if the feature is not needed, as it will improve performance. |
| `UseWideSlope` | If this is set the is checked against a large area instead of a single point. |

## A real one

`Vanilla\Assets\Templates\Contracts\BaseDefinitions\PlanetEncounterSpawnLocationDefinition.def`

```json
{
  "Guid": "1bcb2c63-b039-42fb-9453-9ad550a6f67d",
  "Locations": [],
  "Planet": null,
  "AnchorAlignmentAngle": 45,
  "Biomes": [],
  "SupportedVoxelMaterials": [],
  "SlopePlacementRule": {
    "Min": 0,
    "Max": 30
  },
  "UseWideSlope": true,
  "UsePreciseSlopeRange": false,
  "PreciseSlopeHeightRange": {
    "Min": 0,
    "Max": 1
  },
  "HeightPlacementRule": {
    "Min": 0,
    "Max": 0.6
  }
}
```

Others: `SpaceKemikCommStationUpgradeContractVS2-3_PlanetEncounterSpawnLocationDefinition`, `KemikHydrogenFacilityContractVS2-3_PlanetEncounterSpawnLocationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEncounterSpawnLocationDefinitionObjectBuilder')
search_content('', type_contains='PlanetEncounterSpawnLocationDefinitionObjectBuilder')
```
