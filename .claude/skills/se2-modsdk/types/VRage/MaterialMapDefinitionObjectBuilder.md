# MaterialMapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.MaterialMapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **10**

## What it is

Object builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Cubemap` | The main material cubemap for the planet. Provides the texture data used to map materials across the planet's surface based on color values. Supports and . Requires a square texture. |
| `MaterialBlending` | Settings for the blending texture. |
| `MaterialMappings` | Defines a list of material mappings for the planet. Each mapping associates a specific set of material rules with a color key. Ensures distinct materials can be assigned to different regions of the planet based on their characteristics. |
| `PlanetCubemap` | Main material cubemap for the planet. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\Planets\Kemik\Biomes\MaterialMaps\Kemik_Materials.def`

```json
{
  "Guid": "4e65dc57-34ec-4623-a91e-aa17f2424657",
  "Cubemap": {
    "Right": "{G}1f5f063b-4911-432a-a424-271b847b66fb",
    "Left": "{G}f324ee5a-5a55-48bd-b687-b5fd8fa1a500",
    "Up": "{G}65540bd5-bf55-48a9-9bd3-4b12ee2b1a37",
    "Down": "{G}d6fb1ecb-ba34-4f99-b1bc-660c03f4694a",
    "Backward": "{G}b6ef2fcd-7e14-4dbf-8e8c-843757d89818",
    "Forward": "{G}8d7ea9d1-e969-47a1-9b14-80451c3fdab2"
  },
  "PlanetCubemap": "{G}1dcee6bb-5986-45f3-946e-06bbed625e69",
  "MaterialBlending": {
    "Texture": "{G}ba51ef4c-313d-485c-aa0e-3a3d2da18406",
    "PlanetTexture": "{G}3c885957-b81e-4356-a695-c6f08af95822",
    "CellSize": 64
  },
  "MaterialMappings": [
    {
      "Key": "174127af-4e1e-48b4-9bdb-5abd10e0f6fd",
      "Value": "67d17f59-cfb1-46d2-b802-65552d28a490"
    },
    {
      "Key": "d8166047-95d5-45ba-ace4-5fa69c803089",
      "Value": "74b562f3-2749-4560-a644-ed713809577a"
    },
    {
      "Key": "23150bdf-de78-477e-b031-a30e801202e2",
      "Value": "56ee4383-8972-4cb0-b93c-25278002a31f"
    },
    {
      "Key": "7c798bd7-098d-4f6c-afc4-c7c2d8dd0b3b",
      "Value": "a9eb1cc9-1699-424d-aca5-7d729badbf49"
    },
    {
      "Key": "4b0da91c-5d36-4558-b404-c8ef65999a0b",
      "Value": "aa26f8d9-9e75-42ae-a48f-bfdd6afb2067"
    },
    {
      "Key": "14ab4faf-802a-41f6-a236-d549159b7d21",
      "Value": "28d038e5-fee2-45eb-90a9-5f67c5c29491"
    },
    {
      "Key": "2bfd682e-5b32-439a-9e85-9344fa1dc5a4",
      "Value": "a2ac65bc-f0c5-4b29-a062-8308d6071f1e"
    },
    {
      "Key": "d1c5fcc7-8d5d-44d7-ad12-82f112c9750c",
      "Value": "d42d6ce2-161a-48a9-b212-63d29f944781"
    },
    {
      "Key": "2e74c34f-7ea3-4826-b0c1-d833b8a8537b",
      "Value": "ca7c3d93-a9e6-492b-9116-f43ac5ad526d"
    },
    {
      "Key": "821ec7a2-df58-4ec8-b649-a4bf9705201d",
      "Value": "b7dc9f18-eb20-4c72-9fb3-4352ed1fbcc9"
    },
    {
      "Key": "becafc75-98aa-4f17-9a40-1c341abce6b4",
      "Value": "935e9527-7583-486f-a036-9f45cfa32131"
    },
    {
      "Key": "5fc685c0-2c16-446c-8d5a-014f2a8c991e",
      "Value": "459bbff0-e867-47f5-bc1c-0bee8feddbbe"
    },
    {
      "Key": "49ccfbe3-d233-49dd-b9df-363b7a6e29f6",
      "Value": "ee34f582-1e06-4005-a946-a6ff925a81b1"
    }
  ]
}
```

Others: `Byblos_Materials`, `Verdure_Materials`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialMapDefinitionObjectBuilder')
search_content('', type_contains='MaterialMapDefinitionObjectBuilder')
```
