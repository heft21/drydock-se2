# AddRemoveShadowsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.AddRemoveShadowsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `StatePairs` | Pairs of material states with and without shadows |

## A real one

`Engine\Assets\Configurations\AddRemoveShadowsConfiguration.def`

```json
{
  "Guid": "32f8c075-16ac-44b5-b614-99b5638a68cb",
  "StatePairs": [
    {
      "Key": "52afade9-f464-4ae6-9b25-cfeea802d034",
      "Value": {
        "WithShadow": "28b46a4e-18ee-459f-a3b1-f268e7a20801",
        "WithoutShadow": "cdfbb474-8da5-479b-b3a6-4d81adf4de4f"
      }
    },
    {
      "Key": "d2e07b9a-17b2-4b02-83d8-04401445c0fe",
      "Value": {
        "WithShadow": "f97448f5-2971-4147-985d-2e9cfccfde98",
        "WithoutShadow": "be357bc7-a106-42b6-98e2-e52942c971bd"
      }
    },
    {
      "Key": "d20299e4-1977-4b30-8141-69f0334298d6",
      "Value": {
        "WithShadow": "4e212478-f98f-4486-9c0f-2dbed6dd6cb4",
        "WithoutShadow": "a9b63c54-d6d7-438d-a277-0109118df8c9"
      }
    },
    {
      "Key": "911ee361-e172-4af9-83a5-77ba4383f1b2",
      "Value": {
        "WithShadow": "3f35202a-dc1a-4747-915a-0ac7af2e2286",
        "WithoutShadow": "2519045f-a54c-45dd-824d-2deefa4c743d"
      }
    },
    {
      "Key": "d09db4ab-4f80-4cdb-a9e9-7205b6788f38",
      "Value": {
        "WithShadow": "7436e9f2-f45d-4dac-9360-da3a5e87698b",
        "WithoutShadow": "f5039572-700d-4aa4-9330-a50fe5edf1a6"
      }
    },
    {
      "Key": "29d81ee5-2f2b-48a3-89c4-b219c2ca6ad2",
      "Value": {
        "WithShadow": "c5d29980-6370-47e9-ab08-e621395292b9",
        "WithoutShadow": "da213fdf-5073-4e15-9b0d-8ba4a2e0dc95"
      }
    },
    {
      "Key": "246b485a-34f8-4af3-8073-4b4d8af5202e",
      "Value": {
        "WithShadow": "7c8eaae1-f967-48c9-becf-5401eb950bf2",
        "WithoutShadow": "6723a788-ab23-4436-8007-063cfb0da1d6"
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AddRemoveShadowsConfigurationObjectBuilder')
search_content('', type_contains='AddRemoveShadowsConfigurationObjectBuilder')
```
