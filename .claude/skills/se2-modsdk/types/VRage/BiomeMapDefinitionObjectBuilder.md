# BiomeMapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.BiomeMapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **12**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Cubemap` | The main biome cubemap for the planet. Provides the texture data used to map biomes across the planet's surface based on color values. Supports and . Requires a square texture. |
| `PlanetCubemap` | Main biome cubemap for the planet. |
| `SurfaceBiomes` | A list of surface biomes for this planet. Make sure that each biome in this set has a unique color key. This will map the value in the texture red channel to a specific defined biome. Processing the definition will assert if there are non-unique keys. |
| `SurfaceOresDepth` | Specifies the maximum depth at which surface ores can spawn. NOTE: The maximum allowed depth for each individual ore can be lowered by adjusting the ore rules inside the . |
| `UndergroundBiomes` | A list of underground biomes for this planet. Make sure to have at least 1 biome set to the depth of 1 - that will represent the nucleus of the planet. If there are no other biomes besides the nucleus, it will occur right under the surface. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\Planets\Kemik\Biomes\Kemik_Biomes.def`

```json
{
  "Guid": "c8e10a5b-9b75-494f-95c9-ba40e1bc7adc",
  "Cubemap": {
    "Right": "{G}378ea2e9-23ab-4503-9ef3-9a6927e9f03e",
    "Left": "{G}d5dadeb3-9320-41a9-8e9c-26e84c9a9f38",
    "Up": "{G}f2d1d352-a40d-423a-bb8f-2b38333aedb4",
    "Down": "{G}0aceb142-338a-43ad-9c2e-d0f2f4146cea",
    "Backward": "{G}d1ad0d29-f2c5-4f64-a84d-9f8b15c657c7",
    "Forward": "{G}43b6e5f7-73ff-4460-b59b-1bc7557104fd"
  },
  "PlanetCubemap": "{G}c59f0960-b1cc-45e8-9aa5-0171d3652117",
  "SurfaceBiomes": [
    {
      "Key": "bb3f7ee6-282c-4367-a12f-f4aae620cf79",
      "Value": "0d054173-fabc-492b-91a4-d50a7a1a0636"
    },
    {
      "Key": "a05fc07e-59b7-4bbc-a0a2-8799578ef648",
      "Value": "f8c3bfbf-62d7-43b0-8290-cd45586e809a"
    },
    {
      "Key": "e75f825f-088c-42cb-b12d-24a1398b98b6",
      "Value": "f1c8f1aa-f7b1-4c95-b124-f6be135e267e"
    },
    {
      "Key": "7f02b679-6eee-4619-9287-ce114487e3eb",
      "Value": "4b299b83-10ac-4536-aa4d-3753716c4c21"
    }
  ],
  "SurfaceOresDepth": 20,
  "UndergroundBiomes": [
    "3310a12b-a89b-4e01-8cad-9596108f3638",
    "94a3020a-f05a-4eeb-bd60-2ca0e549e89e",
    "bc9cf2e2-61c4-45bb-b3a2-fc9d41599218"
  ]
}
```

Others: `Byblos_Biomes`, `Verdure_Biomes`

---

Read it with the MCP server rather than by hand:

```
describe_type('BiomeMapDefinitionObjectBuilder')
search_content('', type_contains='BiomeMapDefinitionObjectBuilder')
```
