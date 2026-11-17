# PlanetBiomeDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetBiomeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **62**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoulderOreRules` | List of ore spawn rules for the surface boulders. |
| `ColorKey` | The red channel color value that corresponds to this biome in the biome texture. Used to identify areas of the planet's surface where the biome will occur. |
| `OreRules` | List of ore spawn rules for the biome. |
| `OresPerCubicKilometer` | The density of ore deposits in this biome, measured in deposits per cubic kilometer. Determines the frequency of ore spawns in areas where this surface biome is present. |
| `SnowAmount` | The snow amount to be applied on flora in this biome. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\MarsLike\Biomes\MarsLikeRock.def`

```json
{
  "Guid": "d5b2960d-243f-4b18-9ca8-a8bfb6321879",
  "OreRules": [
    {
      "Probability": 1,
      "Ore": {
        "Material": "1f5d7d9b-9fe5-4fbc-8b88-42794e005137",
        "MinSize": 10,
        "MaxSize": 20,
        "MinBiomeDepth": 0,
        "MaxBiomeDepth": 1
      }
    },
    {
      "Probability": 1,
      "Ore": {
        "Material": "30ca48a2-d182-4892-8629-60433c18883f",
        "MinSize": 10,
        "MaxSize": 20,
        "MinBiomeDepth": 0,
        "MaxBiomeDepth": 1
      }
    }
  ],
  "BoulderOreRules": [],
  "ColorKey": 0,
  "OresPerCubicKilometer": 2
}
```

Others: `Grass_Biome`, `Desert_Biome`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetBiomeDefinitionObjectBuilder')
search_content('', type_contains='PlanetBiomeDefinitionObjectBuilder')
```
