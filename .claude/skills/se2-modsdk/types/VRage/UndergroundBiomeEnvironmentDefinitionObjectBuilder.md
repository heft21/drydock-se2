# UndergroundBiomeEnvironmentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.UndergroundBiomeEnvironmentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **1**

## What it is

Object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SpawnBiome` | The underground biome within which the environment items listed below can spawn. |
| `SpawnItems` | List of environment items available for spawning within the specified underground biome. |

## A real one

`Vanilla\Assets\Procedural\VS2_2\Planets\Palatine\Biomes\Underground\Palatine_UndergroundBiomeEnvironmentDefinition.def`

```json
{
  "Guid": "4f68f911-1aff-4e95-8263-8535bfa3a8c5",
  "SpawnBiome": "7afdbc45-9da3-4bc2-977c-a47d287e5a7e",
  "SpawnItems": [
    {
      "Key": "c4bcb72e-7169-4a9f-b441-af1e9e517b14",
      "Value": "5e3eaf6c-e3ba-4a19-9bce-bba4b1b12c1b"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UndergroundBiomeEnvironmentDefinitionObjectBuilder')
search_content('', type_contains='UndergroundBiomeEnvironmentDefinitionObjectBuilder')
```
