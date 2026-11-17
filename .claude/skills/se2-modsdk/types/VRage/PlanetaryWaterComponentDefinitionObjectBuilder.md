# PlanetaryWaterComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.PlanetaryWaterComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WaterBiomes` | Define water biomes |
| `WaterLayers` | Define how water looks like at different locations |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\EarthLike\Data\EarthLikePlanetaryWaterComponentDefinition.def`

```json
{
  "Guid": "4160daa7-658c-41b8-8abf-03dfd86994c7",
  "WaterLayers": "2389ca31-dcd2-4acc-b419-fd1f398164e3",
  "WaterBiomes": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetaryWaterComponentDefinitionObjectBuilder')
search_content('', type_contains='PlanetaryWaterComponentDefinitionObjectBuilder')
```
