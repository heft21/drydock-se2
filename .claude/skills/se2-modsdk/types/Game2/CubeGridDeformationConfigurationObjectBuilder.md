# CubeGridDeformationConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage.CubeGridDeformationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CornerDeformationTable` | Deformation intensity for a given block corner offset relative to the corner bone position, resulting in 10 possible positions. |
| `ExplosionDeformationBoneLimitMultiplier` | Multiplier for and on explosion |
| `ExplosionDeformationMultiplier` | Final deformation multiplier after distance fall-off calculation |
| `MaxEdgeDeformationVariance` | Maximum random deformation that can occur along an edge. |
| `MaxExplosionDeformation` | Maximum distance in meters an explosion can deform armor |
| `MaxRandomDeformationAngle` | Maximum angle for random directions of the deformation |
| `MaxRandomDeformationMultiplier` | Maximum random deformation that can occur, scaled with block size |
| `MinExplosionDeformation` | Minimum distance in meters an explosion can deform armor (that is in range of the explosion) |
| `MinRandomDeformationMultiplier` | Minimum random deformation that can occur, scaled with block size |

## A real one

`Vanilla\Assets\System\Configurations\BlockGridDeformationConfiguration.def`

```json
{
  "Guid": "3d476faa-c315-410d-9a7d-6496fa7faedc",
  "CornerDeformationTable": [
    {
      "$Key": {
        "X": 0,
        "Y": 0
      },
      "$Value": {
        "CornerBoneIntensity": 0.7,
        "CloserBoneIntensity": 0.3,
        "FurtherBoneIntensity": 0.3
      }
    },
    {
      "$Key": {
        "X": 1,
        "Y": 0
      },
      "$Value": {
        "CornerBoneIntensity": 0.75,
        "CloserBoneIntensity": 0.15,
        "FurtherBoneIntensity": 0.3
      }
    },
    {
      "$Key": {
        "X": 1,
        "Y": 1
      },
      "$Value": {
        "CornerBoneIntensity": 0.75,
        "CloserBoneIntensity": 0.3,
        "FurtherBoneIntensity": 0.3
      }
    },
    {
      "$Key": {
        "X": 2,
        "Y": 0
      },
      "$Value": {
        "CornerBoneIntensity": 0.8,
        "CloserBoneIntensity": 0.3,
        "FurtherBoneIntensity": 0.375
      }
    },
    {
      "$Key": {
        "X": 2,
        "Y": 1
      },
      "$Value": {
        "CornerBoneIntensity": 0.8,
        "CloserBoneIntensity": 0.3,
        "FurtherBoneIntensity": 0.375
      }
    },
    {
      "$Key": {
        "X": 2,
        "Y": 2
      },
      "$Value": {
        "CornerBoneIntensity": 0.8,
        "CloserBoneIntensity": 0.45,
        "FurtherBoneIntensity": 0.45
      }
    },
    {
      "$Key": {
        "X": 3,
        "Y": 0
      },
      "$Value": {
        "CornerBoneIntensity": 0.9,
        "CloserBoneIntensity": 0.375,
        "FurtherBoneIntensity": 0.525
      }
    },
    {
      "$Key": {
        "X": 3,
        "Y": 1
      },
      "$Value": {
        "CornerBoneIntensity": 0.9,
        "CloserBoneIntensity": 0.375,
        "FurtherBoneIntensity": 0.6
      }
    },
    {
      "$Key": {
        "X": 3,
        "Y": 2
      },
      "$Value": {
        "CornerBoneIntensity": 0.9,
        "CloserBoneIntensity": 0.375,
        "FurtherBoneIntensity": 0.675
      }
    },
    {
      "$Key": {
        "X": 3,
        "Y": 3
      },
      "$Value": {
        "CornerBoneIntensity": 1,
        "CloserBoneIntensity": 0.77,
        "FurtherBoneIntensity": 0.77
      }
    }
  ],
  "ExplosionDeformationMultiplier": -1,
  "MinExplosionDeformation": 1,
  "MaxExplosionDeformation": 3,
  "ExplosionDeformationBoneLimitMultiplier": 0.4,
  "MinRandomDeformationMultiplier": 0.02,
  "MaxRandomDeformationMultiplier": 0.2,
  "MaxRandomDeformationAngle": 1.5708,
  "MaxEdgeDeformationVariance": 0.2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeGridDeformationConfigurationObjectBuilder')
search_content('', type_contains='CubeGridDeformationConfigurationObjectBuilder')
```
