# UndergroundBiomeDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.UndergroundBiomeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **22**

## What it is

Migrations part of the underground biome definition.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Material` | Voxel material that defines the biome composition. |
| `MaxDepth` | Specifies the maximum depth percentage at which this biome occurs. Biomes are assigned in ascending order of depth percentages, starting at 0 for the planet's surface and ending at 1 for its center. Within any overlapping ranges, the biome with the lowest `MaxDepth` takes precedence up to its limit. Example: - Biome A (`MaxDepth: 0.3`) occurs from the surface to 30% depth. - Biome B (`MaxDepth: 0.7`) occurs from 30% to 70% depth. - Biome C (`MaxDepth: 1.0`) occurs from 70% depth to the planet's center. |
| `OreRules` | List of ore spawn rules. |
| `OresPerCubicKilometer` | The density of ore deposits in this biome, measured in deposits per cubic kilometer. Determines the frequency of ore spawns at depths where this underground biome occurs. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\EarthLike\Biomes\UndergroundOne.def`

```json
{
  "Guid": "9abecf28-8447-4285-a3d6-fe1e07082c10",
  "OreRules": [
    {
      "Probability": 1,
      "Ore": {
        "Material": "1f5d7d9b-9fe5-4fbc-8b88-42794e005137",
        "MinSize": 20,
        "MaxSize": 50,
        "MinBiomeDepth": 0,
        "MaxBiomeDepth": 1
      }
    }
  ],
  "Material": "dd82e401-023d-4fa2-9865-69d9ddb8bb26",
  "MaxDepth": 0.15,
  "OresPerCubicKilometer": 2
}
```

Others: `UndergroundTwo`, `UndergroundThree`

---

Read it with the MCP server rather than by hand:

```
describe_type('UndergroundBiomeDefinitionObjectBuilder')
search_content('', type_contains='UndergroundBiomeDefinitionObjectBuilder')
```
