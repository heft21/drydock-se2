# InventoryConfigurationObjectBuilder

`Game2:Keen.Game2.Game.DefaultDefinitions.InventoryConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.DefaultDefinitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EssentialItems` | Important items that should not be automatically transferred to target inventories when performing a "move all items" inventory operation |

## A real one

`Vanilla\Assets\System\Configurations\InventoryConfiguration.def`

```json
{
  "Guid": "d0ed6c94-7146-4d25-94ff-d12b5745c1de",
  "EssentialItems": [
    "c61a5156-5ff7-4ab5-85ef-4942c4cd47d8",
    "90ad9e76-53d6-4a5a-8347-8373070751ab",
    "0ad65a3f-1d03-4db5-bbed-7738b20b6eac",
    "3b838d8d-dae4-4050-9ecb-f116921c7c32",
    "670d2ff4-ac11-47ce-9b64-ad3ee5cdb554",
    "d2bd7f3c-a96f-4fe7-9737-f6aeaa9e3542",
    "3ba4f22c-3a5b-4d6d-9c9d-ec2fdd653e51",
    "770dc374-ee92-4efd-827e-208d62dedfd9",
    "220e4c72-2ea6-48cc-9633-45a6ee078266",
    "8a34da24-1b6a-497d-b82b-c10813d4f905",
    "7b8259d3-57d5-4679-9d86-81f6eee952a6",
    "666ddf91-ebef-470b-bcbf-5a8854a8c3b2",
    "030fc393-80cb-4afb-bbe6-cbe32d59f5cd",
    "64ceb520-d2f0-433f-88fa-5ddc900b5f60",
    "759a8207-9953-4b2d-bd78-8ec3d2e6fe8c",
    "248b2687-a9c6-4806-8c55-d0fe4ba65784",
    "081f7c14-9d34-4552-9fae-27600e9311eb",
    "e5554fdd-3bd3-4489-99a7-3fdbaeea3e8b",
    "3042ad6b-e888-4ee0-9e04-bf7cf77afd4a",
    "20e40fb1-92ba-47d5-9e15-4cc4353aa6c9",
    "3a8f0ff6-2c90-47d8-8915-752dbde5dbd5",
    "eca055ba-f61f-4d28-bde6-a3cfc8fdb4ae",
    "6f0c8017-457d-4a0a-a3c1-333a983a1997",
    "634bf393-b14b-496c-b14d-91111b6e1178",
    "9a31cafc-3c5f-4c97-951d-7fd7a17bef8d",
    "43039af7-670f-4c7d-a5fc-b055b4febb0c",
    "77f1876f-cae1-4acf-8d38-20b3d3283891",
    "a205b61c-caa8-4df6-8824-f4ccd56cd758",
    "002649ce-220f-48c3-8b1d-44ad27ae6ade",
    "01561ee0-9ba8-4cbb-9b4e-b77cebc5f921",
    "9d8c0754-a615-4518-bdb5-d86c064b445e",
    "35a9dd93-a01e-4364-8076-e29f4f0bc82a",
    "01065eee-bfd3-4803-a678-bbaaa6bc70a3",
    "cdf6ddf3-feb0-4939-a912-78e49f1561e0",
    "c1468778-0d37-4ad6-a3bd-7da77bf1c734",
    "3467b5dd-bdf1-4971-b744-2e75a4174dbf",
    "f084c277-1052-4e19-99f5-9a6eff49865d",
    "1c036684-854c-4776-872e-ac8452b2f99d",
    "7bd271d9-389a-4972-9139-9cbd863dfd12"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryConfigurationObjectBuilder')
search_content('', type_contains='InventoryConfigurationObjectBuilder')
```
