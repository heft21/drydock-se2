# MaterialInstancingAssociationConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.MaterialInstancingAssociationConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaterialAssociation` | Material associations |

## A real one

`Engine\Assets\Core\MaterialInstancingAssociationConfiguration.def`

```json
{
  "Guid": "8651a8fa-0e8e-4b9c-9fcc-3d3e69561c97",
  "MaterialAssociation": [
    {
      "Key": "096e51a0-07c7-49df-92b9-31b2d11e65bf",
      "Value": {
        "NonInstancedMaterialState": "9cf999f7-1e08-498c-957e-12a35d07892d",
        "InstancedMaterialState": "07daf0eb-f19d-4477-a67e-96d109982761"
      }
    },
    {
      "Key": "e7b5961c-8207-4ece-bb43-f618db2d3532",
      "Value": {
        "NonInstancedMaterialState": "0789b0ad-baa9-472d-ac6d-f6ecabd27f1c",
        "InstancedMaterialState": "b3da0cb2-482f-4e5b-aeb3-9eb9eb86b9b3"
      }
    },
    {
      "Key": "65028814-5d7f-4061-a84e-35a74dbcedea",
      "Value": {
        "NonInstancedMaterialState": "7dd43edf-bc9b-413c-aab2-8d3e80f9d53a",
        "InstancedMaterialState": "cc0c1cea-68d7-4ebf-a743-99850c3997c5"
      }
    },
    {
      "Key": "843bc2c2-cf8a-41a2-b11e-f69129ef50ad",
      "Value": {
        "NonInstancedMaterialState": "da8fd9b0-d453-4e32-9174-95d86ceb0450",
        "InstancedMaterialState": "07baa9bd-0db7-418c-be29-82aa2bb5affd"
      }
    },
    {
      "Key": "8483b4c5-97e5-4244-82f6-7cca884fd851",
      "Value": {
        "NonInstancedMaterialState": "7ba38030-fb64-4a61-b3e0-5abd976e764c",
        "InstancedMaterialState": "ab3a808d-d408-41c3-ace4-45a4055a7676"
      }
    },
    {
      "Key": "567ca7fb-52f2-4d37-9d00-77c949b95140",
      "Value": {
        "NonInstancedMaterialState": "441607c6-d256-42f3-94b3-6977ef3f99d0",
        "InstancedMaterialState": "aed5b1ea-66c4-4cf1-9e62-5909ee8616d5"
      }
    },
    {
      "Key": "9e91d79c-db5f-4c9b-8ca9-d3fa7f296658",
      "Value": {
        "NonInstancedMaterialState": "548c1c47-3a90-46bd-8eff-de0e27a6fc19",
        "InstancedMaterialState": "33dec0ec-af3c-447a-a00a-f41d5f4300dd"
      }
    },
    {
      "Key": "f586df63-108e-4b12-aa5f-059f569b6b20",
      "Value": {
        "NonInstancedMaterialState": "67a95236-5f44-4341-b0d9-bfc960cb8b81",
        "InstancedMaterialState": "0b627267-6190-4362-ac5e-6e047f990739"
      }
    },
    {
      "Key": "081dc26c-65e2-4a49-bf02-9944fb9b039f",
      "Value": {
        "NonInstancedMaterialState": "6c50a8e7-94f2-4b1d-8a36-d1e7b2c9f048",
        "InstancedMaterialState": "7c5b9a19-6c9a-4fc1-b430-9e6d7c8cf03a"
      }
    },
    {
      "Key": "d201385c-5892-46d9-bc6e-7b3a05ae79a1",
      "Value": {
        "NonInstancedMaterialState": "69af47c6-1205-4f5c-b0db-bf284ec34b5a",
        "InstancedMaterialState": "3b7e1d92-0c4a-4f86-9d21-5e8a7c0f44b1"
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialInstancingAssociationConfigurationObjectBuilder')
search_content('', type_contains='MaterialInstancingAssociationConfigurationObjectBuilder')
```
