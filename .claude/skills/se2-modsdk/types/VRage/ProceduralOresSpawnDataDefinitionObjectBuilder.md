# ProceduralOresSpawnDataDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.ProceduralOresSpawnDataDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **13**

## What it is

Defines procedural generation of ore deposits in a voxel storage.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxDeposits` | Specifies the maximum number of ore deposits to generate inside the voxel storage. |
| `MinDeposits` | Specifies the minimum desired number of ore deposits to generate inside the voxel storage, if conditions allow. If the conditions for spawning are insufficient, fewer deposits may be created. |
| `OreRules` | A collection of rules defining the spawning behavior and properties of ore deposits. If the probabilities of the listed ores do not add up to 1, they are automatically rescaled to ensure consistent distribution. NOTE:If initialized, this will override boulder ore rules from the . |

## A real one

`Vanilla\Assets\Procedural\VS2_0\Planets\Common\GeneratedDetailPrefabs\SpawnEntities\LeedahBoulder_500Deposits.def`

```json
{
  "Guid": "e673e1e4-333d-4448-8bca-bab52f05dc68",
  "OreRules": [
    {
      "Probability": 0.7,
      "Ore": {
        "Material": "30ca48a2-d182-4892-8629-60433c18883f",
        "MinSize": 8,
        "MaxSize": 32,
        "MinBiomeDepth": 0,
        "MaxBiomeDepth": 1
      }
    },
    {
      "Probability": 0.3,
      "Ore": {
        "Material": "99252318-6504-471b-a0ed-1dbc3ed4cf74",
        "MinSize": 8,
        "MaxSize": 32,
        "MinBiomeDepth": 0,
        "MaxBiomeDepth": 1
      }
    }
  ],
  "MinDeposits": 0,
  "MaxDeposits": 32
}
```

Others: `EarthLike_DefaultBiome_Boulder30Deposits`, `EarthLike_DefaultBiome_LeedahBoulder_500Deposits`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProceduralOresSpawnDataDefinitionObjectBuilder')
search_content('', type_contains='ProceduralOresSpawnDataDefinitionObjectBuilder')
```
