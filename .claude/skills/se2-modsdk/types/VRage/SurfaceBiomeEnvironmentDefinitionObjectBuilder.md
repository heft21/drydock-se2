# SurfaceBiomeEnvironmentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.SurfaceBiomeEnvironmentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **64**

## What it is

Object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SpawnBiome` | The surface biome within which the environment items listed below can spawn. |
| `SpawnFloraItems` | List of flora items that can be spawned. |
| `SpawnItems` | List of environment items available for spawning within the specified surface biome. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\EarthLike\Data\DesertSpawnBiome.def`

```json
{
  "Guid": "331742ae-28e3-424e-a1c3-c27c2a17a8f9",
  "SpawnBiome": "f4ce5c85-b546-42d1-8a0f-a37a1a3ab14d",
  "SpawnItems": [
    {
      "Key": "19367862-348c-427d-b4c7-e11ffa41c507",
      "Value": "67de19db-335d-464f-9e60-9f6b879d54f1"
    },
    {
      "Key": "4bc44bee-3875-41dd-8d1c-32fc7b7cf8e3",
      "Value": "4063617f-4a28-4f14-b644-33da2ffca970"
    },
    {
      "Key": "206d6bdb-7ba1-4aed-a7d8-89942f7d5ece",
      "Value": "3da6df21-1423-43cd-a014-942d8e29667f"
    },
    {
      "Key": "8cf70610-a808-43a2-b8aa-30d8cd7ebbe5",
      "Value": "99e01a92-8710-4405-a8c4-e29f085f7254"
    },
    {
      "Key": "0e647a57-7193-47fc-8b81-949baab6d589",
      "Value": "97dd43e1-63c9-4725-b994-f0f5537142ba"
    }
  ],
  "SpawnFloraItems": []
}
```

Others: `DefaultSpawnBiome`, `LakeAreasSpawnBiome`

---

Read it with the MCP server rather than by hand:

```
describe_type('SurfaceBiomeEnvironmentDefinitionObjectBuilder')
search_content('', type_contains='SurfaceBiomeEnvironmentDefinitionObjectBuilder')
```
