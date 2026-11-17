# BlockMaterialGroupDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.BlockMaterialGroupDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Materials` | List of render materials included to this group |

## A real one

`Vanilla\Assets\System\Configurations\Effects\BlockMaterialGroups\GlassBlockMaterialGroup.def`

```json
{
  "Guid": "cc0ae580-0c18-465a-83c7-4a24afc39a2c",
  "Materials": [
    {
      "Key": "ced25bd6-6d40-4039-8e04-9d9e91783401",
      "Value": "30072ea8-c740-4a4c-8c5c-1276d102d939"
    },
    {
      "Key": "661c610b-18b4-4b6c-b46d-c161ef5fc283",
      "Value": "83c075f5-f177-460d-94a7-8aca19fd4d6f"
    },
    {
      "Key": "6086bf73-4af7-47b3-9b6e-4193c4e381e8",
      "Value": "b9db8238-9373-4690-b743-17e37759179e"
    },
    {
      "Key": "4abfe6c8-3645-4436-9947-5b94de3cce17",
      "Value": "8badb36c-3551-4f48-b1c1-b86c34bed900"
    },
    {
      "Key": "1f54011b-fe29-42f0-b550-ebdb7eefd6cb",
      "Value": "42f1feac-dd82-4cea-9676-ce502f1f7217"
    },
    {
      "Key": "f9850ea7-0f5e-4f77-94d0-17382ae6f1aa",
      "Value": "646cbd24-5fd8-4b80-9c45-4e3ddee5a79d"
    },
    {
      "Key": "b5b40ed1-beba-417c-8795-b907dededd50",
      "Value": "ee0588d7-65e4-47e5-8c70-8b8684bc5552"
    },
    {
      "Key": "d2ec7ecb-5198-42f7-99fa-8494e732c5e0",
      "Value": "73b146d6-2a17-405c-ac00-dd7ddb4454d6"
    },
    {
      "Key": "9f19d6c5-a936-46de-9cf3-7fabc835a6b2",
      "Value": "8a35c12c-0fb9-45fa-be7b-6d97cb624c75"
    },
    {
      "Key": "5197ecbd-4a02-4e41-abad-d921c1e45cba",
      "Value": "eaaac298-66e9-48aa-9576-6e4b682968d6"
    },
    {
      "Key": "8942eba7-74b9-42b3-b6b1-6735c10078d8",
      "Value": "d6961173-5d20-4be4-ac9d-5a5e1a636f38"
    },
    {
      "Key": "c96284ab-f847-41d3-b477-67407fc0a528",
      "Value": "0d19e127-adfc-4e01-b849-6ce357c06798"
    },
    {
      "Key": "d47c02f8-d30b-43ad-ac35-d5dcc17a4533",
      "Value": "bd7f946b-3867-4aaf-8aaf-2a8eed16e832"
    },
    {
      "Key": "58630d50-6011-40a0-90b9-b232dce4ca2b",
      "Value": "fa0a1f34-75c1-4899-bc3c-761ec9f70877"
    },
    {
      "Key": "6960d383-957b-4be9-8242-7c061c29b2c3",
      "Value": "9b678814-68f3-4fa2-91ba-3b0c6f7d4757"
    },
    {
      "Key": "94b27011-22d1-48b6-8b77-b132a118f0df",
      "Value": "6a5cdee6-32b2-452c-aa11-c2b55319372f"
    },
    {
      "Key": "740bd299-84d8-4d1f-a681-09d86cf946b4",
      "Value": "36eb5589-bf85-4f4f-afc6-4a26ac3e1389"
    }
  ]
}
```

Others: `MetalBlockMaterialGroup`, `DarkPlasticMaterialGroupDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockMaterialGroupDefinitionObjectBuilder')
search_content('', type_contains='BlockMaterialGroupDefinitionObjectBuilder')
```
