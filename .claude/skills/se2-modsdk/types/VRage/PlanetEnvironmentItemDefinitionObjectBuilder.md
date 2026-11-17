# PlanetEnvironmentItemDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetEnvironmentItemDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **266**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Density` | Spawn density of the item per unit area. The system will attempt to fill out every area in the containing biome so that roughly the required number of items is represented. |
| `HeightPlacementRule` | Specifies the percentage height range where the item can be placed. |
| `LodPrefabs` | A list of prefabs for items that will be spawned in cells of different LODs. Example: Prefab A can spawn for this item up to LOD 1 cells, then from LOD 2 to LOD 4 cells Prefab B will spawn and so on. The first prefab that meets the requirements will always be the one that spawns. If there are no prefabs specified above a certain LOD, nothing will be spawned in those cells. |
| `LodSpawnPruning` | A list of pruning rules for the item in case a lower percentage of items is desirable at different LODs. Example: 100% of items will be spawned up to LOD 1 cells, then 75% from LOD 2 to LOD 4 cells and so on. In case there are multiple values applicable at the current LOD only the first one will be used. No items will be spawned above the highest LOD specified in this list. |
| `PreciseSlopeHeightRange` | Specifies the percentage range of the detected slope height the item is allowed to spawn in. Note: Only applicable if is enabled. |
| `RollThreshold` | Specifies the maximum tilt angle allowed for the item during placement. |
| `SlopePlacementRule` | Specifies the range of slope angle where the item can be placed. Determines the allowed inclinations for item placement, with 0 representing flat ground and 90 representing vertical surfaces. |
| `UsePreciseSlopeRange` | When enabled, the system will consider the surrounding area's slope characteristics to determine suitable locations for item placement. It is recommended to always disable this if the feature is not needed, as it will improve performance. |
| `UseWideSlope` | If this is set the is checked against a large area instead of a single point. |
| `ZOffsetRange` | Offset that can be applied when placing the item. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\EarthLike\Voxels\RoundCave.def`

```json
{
  "Guid": "3e40745a-c8dd-4641-998b-c444ad981c2b",
  "LodPrefabs": [
    {
      "Key": "1253c9db-d446-4544-91ae-2fa4aca4dcd3",
      "Value": {
        "LodItemServer": "252ab3ec-8096-4ad3-ad4b-34fd05ed2d77",
        "VariantPrefabs": {
          "ZRotatedVariantServer": "474e76e1-a8e7-4fcb-8e52-db7a352c60b7",
          "ZXRotatedVariantServer": "0a5a47e6-ad28-44ab-b5d6-355dfcd90358"
        },
        "MaxLod": 5
      }
    }
  ],
  "LodSpawnPruning": [],
  "Density": {
    "Unit": "SquareKilometer",
    "ValuePerUnit": 0.2
  },
  "SupportedVoxelMaterials": [],
  "SlopePlacementRule": {
    "Min": 50,
    "Max": 85
  },
  "UseWideSlope": false,
  "UsePreciseSlopeRange": false,
  "PreciseSlopeHeightRange": {
    "Min": 0,
    "Max": 1
  },
  "HeightPlacementRule": {
    "Min": 0,
    "Max": 0.9
  },
  "RollThreshold": 80.38461,
  "ZOffsetRange": {
    "Min": 0,
    "Max": 0
  }
}
```

Others: `CaveSystem`, `FunnelCave`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentItemDefinitionObjectBuilder')
search_content('', type_contains='PlanetEnvironmentItemDefinitionObjectBuilder')
```
