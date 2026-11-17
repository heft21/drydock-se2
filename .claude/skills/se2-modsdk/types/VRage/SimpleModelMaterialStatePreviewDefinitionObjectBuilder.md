# SimpleModelMaterialStatePreviewDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.Previews.SimpleModelMaterialStatePreviewDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Previews`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Models` | Model assets that can be used to preview the material |

## A real one

`Engine\Assets\Preview\Materials\SimpleModelMaterialStatePreviewDefinition.def`

```json
{
  "Guid": "e2870385-ed50-4541-8d0c-f4b8f2517b2b",
  "Models": [
    {
      "Key": "6fe231f0-a3a1-46d9-8991-db39f700fb3f",
      "Value": "{G}aab3b5f7-acd7-4d49-895d-dfee5ed8a71e"
    },
    {
      "Key": "7b1fb9c7-90a8-4560-bc44-afd5a435f4ac",
      "Value": "{G}74d49b22-6684-4308-bc89-aeaf289c4d24"
    },
    {
      "Key": "638f8643-aaeb-40b0-ac8b-4ceae7eee173",
      "Value": "{G}621e2c2b-3fb9-49d5-ac06-c92e668470cc"
    },
    {
      "Key": "0bd3698f-aeca-470f-9aa7-288836fc3f94",
      "Value": "{G}0f1df1d1-abe6-4daa-ba37-cd2d1acb4af0"
    },
    {
      "Key": "38a336ae-b977-4097-896a-68f81cf2621e",
      "Value": "{G}22a15fb9-4240-44d8-8072-e48be7c9a676"
    },
    {
      "Key": "6dc95e3c-9fae-4675-842c-adf491037636",
      "Value": "{G}205d9ad9-e079-4bf4-83fe-7229d63e0de4"
    },
    {
      "Key": "df2ac61b-a2e0-4aeb-b964-f21d11e75fb6",
      "Value": "{G}e7e12ca9-ff5c-4a3f-af78-eac18813484b"
    },
    {
      "Key": "d3cc07b4-5957-42c8-b5ec-502f3dae37da",
      "Value": "{G}28b7c280-7b82-4f5f-9469-c7514ae5dba7"
    },
    {
      "Key": "d6e6f886-f741-41a2-83c0-e3164960cdda",
      "Value": "{G}40bbd069-e2d9-451c-a824-91324b305bd5"
    },
    {
      "Key": "7feb17c3-d3a5-45b7-8659-8465ad7f90a9",
      "Value": "{G}efabfe49-700e-4385-84ed-2c201ad46dca"
    },
    {
      "Key": "3d2badba-f5ab-4787-9a9d-6bd567ce7497",
      "Value": "{G}8e4c0a04-eebe-4d32-b3ff-3320adce2f9b"
    },
    {
      "Key": "de9e01a7-23e9-4c71-9316-3ac7a2584a43",
      "Value": "{G}2d8d61be-cd4c-4099-99e4-f0baad632b50"
    },
    {
      "Key": "c1e82ce1-23e7-4858-9214-192340c92253",
      "Value": "{G}cb345be6-fa58-4001-843b-bc2100fe4e37"
    },
    {
      "Key": "dc6bca6e-3166-4a1f-898f-d7e788bbee7b",
      "Value": "{G}a07f8b0b-d0c5-4498-a98f-8175b6010134"
    },
    {
      "Key": "fb81a93e-ad01-4b1b-a0cb-fdb9b9345729",
      "Value": "{G}307d6ac1-068c-499a-b44a-0d4d177c9a05"
    },
    {
      "Key": "b713c77a-ddc7-42e0-8fcd-ab5cf1c47614",
      "Value": "{G}19ecb154-66b7-46f7-ba31-db978ae33fea"
    },
    {
      "Key": "df8d4926-c9d0-41c3-b6c9-ea1eeec0ceeb",
      "Value": "{G}f6471d43-599e-43bf-8c50-ab99c0a89807"
    },
    {
      "Key": "87472e52-c521-4bf6-a48b-e947821a0e0a",
      "Value": "{G}ce6224af-6a8a-4ee9-9bf1-b732d4c7ab3e"
    }
  ]
}
```

Others: `BlendedModelMaterialStatePreviewDefinition`, `SkinnedModelMaterialStatePreviewDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SimpleModelMaterialStatePreviewDefinitionObjectBuilder')
search_content('', type_contains='SimpleModelMaterialStatePreviewDefinitionObjectBuilder')
```
