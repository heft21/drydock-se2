# DecalPreviewConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.Previews.DecalPreviewConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Previews`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Material` | Material to apply to any previewed model |
| `Models` | List of models that can be chosen when previewing decals |

## A real one

`Engine\Assets\Configurations\Preview\DecalPreviewConfiguration.def`

```json
{
  "Guid": "5c83a90a-4953-4ac8-9208-5ef0248456b8",
  "Models": [
    {
      "Key": "6089fa54-6c1f-405d-9575-a7f4d8de72ed",
      "Value": "{G}aab3b5f7-acd7-4d49-895d-dfee5ed8a71e"
    },
    {
      "Key": "d31f788c-d3c3-4e54-94cc-25a1e261900d",
      "Value": "{G}74d49b22-6684-4308-bc89-aeaf289c4d24"
    },
    {
      "Key": "bebd9268-83c0-4fe7-bb1b-091739ae4159",
      "Value": "{G}0f1df1d1-abe6-4daa-ba37-cd2d1acb4af0"
    },
    {
      "Key": "a7c7f308-4f6e-43cf-ada3-844eddcc5a78",
      "Value": "{G}e7e12ca9-ff5c-4a3f-af78-eac18813484b"
    },
    {
      "Key": "b9f85793-ae7e-46fb-8046-31f41afb56d2",
      "Value": "{G}cb345be6-fa58-4001-843b-bc2100fe4e37"
    },
    {
      "Key": "c5f9ecf7-bf7e-4dc8-9722-8a7d283b79c5",
      "Value": "{G}307d6ac1-068c-499a-b44a-0d4d177c9a05"
    },
    {
      "Key": "4ce5086a-f5bb-4ebf-8e70-04ac6bc49083",
      "Value": "{G}f6471d43-599e-43bf-8c50-ab99c0a89807"
    }
  ],
  "Material": "3f767d72-d408-48c5-beee-6ba238be945e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalPreviewConfigurationObjectBuilder')
search_content('', type_contains='DecalPreviewConfigurationObjectBuilder')
```
