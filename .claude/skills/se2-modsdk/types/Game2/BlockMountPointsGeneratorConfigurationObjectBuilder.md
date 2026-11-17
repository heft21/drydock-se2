# BlockMountPointsGeneratorConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.BlockDataGenerators.BlockMountPointsGeneratorConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.BlockDataGenerators`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PrimaryMountPointDummies` | List of dummy types that should generate primary mount points |

## A real one

`Vanilla\Assets\System\Configurations\BlockMountPointsGeneratorConfiguration.def`

```json
{
  "Guid": "47300da3-7924-4951-a53f-9335ed81e767",
  "PrimaryMountPointDummies": [
    "29d45e5b-2ddf-4ba5-9031-885260550947",
    "e4203734-4c68-4490-a77e-7e299ad6839d",
    "fbb1ee8a-ffef-4093-9bf3-23dbb03ae7d1"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockMountPointsGeneratorConfigurationObjectBuilder')
search_content('', type_contains='BlockMountPointsGeneratorConfigurationObjectBuilder')
```
