# EncounterEnvironmentItemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters.EncounterEnvironmentItemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Density` | Spawn density of the item per unit area. The system will attempt to fill out every area in the containing biome so that roughly the required number of items is represented. |
| `HeightPlacementRule` | Specifies the percentage height range where the item can be placed. |
| `MaximumStage` | Maximum inclusive required sector stage for this encounter to spawn. If the encounter is outside of sectors, it is always valid. If null allows any stage at or after the . |
| `MinimumStage` | Minimum inclusive required sector stage for this encounter to spawn. If the encounter is outside of sectors, it is always valid. If null allows any stage at or before the . |
| `PreciseSlopeHeightRange` | Specifies the percentage range of the detected slope height the item is allowed to spawn in. Note: Only applicable if is enabled. |
| `Prefab` | Encounter prefab. |
| `SlopePlacementRule` | Specifies the range of slope angle where the item can be placed. Determines the allowed inclinations for item placement, with 0 representing flat ground and 90 representing vertical surfaces. |
| `SupportedVoxelMaterials` | Materials on which this item can spawn. If empty, the item will spawn regardless of the material underneath |
| `UsePreciseSlopeRange` | When enabled, the system will consider the surrounding area's slope characteristics to determine suitable locations for item placement. It is recommended to always disable this if the feature is not needed, as it will improve performance. |
| `UseWideSlope` | If this is set the is checked against a large area instead of a single point. |

## A real one

`Vanilla\Assets\Templates\Encounters\BaseDefinitions\Verdure_BiomeEncounters_EncounterEnvironmentItemDefinition.def`

```json
{
  "Guid": "82dfee90-9bec-4878-ab71-0a9c75c32466",
  "Prefab": null,
  "SupportedVoxelMaterials": [],
  "Density": {
    "Unit": "SquareKilometer",
    "ValuePerUnit": 0.0005
  },
  "SlopePlacementRule": {
    "Min": 0,
    "Max": 15
  },
  "UseWideSlope": true,
  "UsePreciseSlopeRange": false,
  "PreciseSlopeHeightRange": {
    "Min": 0,
    "Max": 1
  },
  "HeightPlacementRule": {
    "Min": 0.25,
    "Max": 1
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterEnvironmentItemDefinitionObjectBuilder')
search_content('', type_contains='EncounterEnvironmentItemDefinitionObjectBuilder')
```
