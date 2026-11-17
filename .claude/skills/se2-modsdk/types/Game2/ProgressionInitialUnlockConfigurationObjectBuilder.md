# ProgressionInitialUnlockConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Progression.ProgressionInitialUnlockConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Progression`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockKinds` | BlockKinds that are unlocked |
| `Blocks` | Blocks that are unlocked |
| `Categories` | Blocks categories that are unlocked |
| `Subcategories` | Blocks subcategories that are unlocked |

## A real one

`Vanilla\Assets\System\Configurations\ProgressionInitialUnlockConfiguration.def`

```json
{
  "Guid": "c7b8e669-e76b-4edb-aa18-8067d0340b96",
  "Blocks": [
    "a5936a12-7c60-4b15-8a78-09356c48c4cd",
    "e3b5f8ef-2446-4504-83ad-8c4091ffdf2f",
    "b71b659d-b27f-46ef-b1d0-33ef52f32981",
    "90c41d51-8ec6-4409-8c15-7faab87d804c",
    "088eacd4-b212-45f0-819e-16679bba8633",
    "8574735f-e98b-487e-9662-21435f0ce3ed",
    "a17bf3a3-8ffc-4543-925e-3c59ffb18c1b",
    "5423f352-f93d-4368-8941-f20a07b40358",
    "2e420bd1-8a02-4680-901d-14655204c043",
    "608317a0-81ed-4ae3-8eab-88bf6e6e0b62",
    "923e8dfb-95f8-45ee-aa9e-052b1e1b786a",
    "ddf3b8d3-f1be-4d72-8432-39d38abeea8a",
    "79df2a89-b422-42a9-809f-749856ae8d19",
    "ee2d59bc-8fa7-43dd-8a8b-df8c73af56bf",
    "014a37b8-1b17-4dc0-9552-88777f359e36",
    "8da7e0d3-b346-4569-a643-facb0f8ca3ef",
    "b5ef9ba0-0683-420d-942c-a113fe3fc7bf",
    "9d0a4105-1e47-474a-b538-9df7911c9d42",
    "47fa73bb-1e12-4ee3-8417-0f2d3698623c",
    "f1d1956d-3d3a-45b2-be6e-f459c99b26f9",
    "a02e2323-bd7d-42c7-91ea-acaebb7ba316",
    "f479f2d7-d277-4260-95a1-3cf952ff9ee5",
    "b3826409-8168-4219-a4e9-58d29b2fd8fa",
    "fcab35f1-3daf-4c02-96a1-ff13b5733b8c",
    "2b59bf55-ef3c-46e5-bb54-551ae6d8c463",
    "4465b025-4193-407f-9a2e-b04f0e51271c",
    "7046873e-c9fe-408c-96c8-53a7f0e62bcd"
  ],
  "BlockKinds": [
    "d65c5eb8-2ff4-4467-966b-9d6045e96fdf",
    "e8f6bc54-271f-48f8-993e-2674578a8da9",
    "ef09aaa4-c926-4936-b54f-afcdcef83fef",
    "2a10a870-50cd-403c-ae16-810d35a9cad8"
  ],
  "Categories": [],
  "Subcategories": [
    "130e4c3d-6aee-44db-ab59-890ab8cacd4d",
    "1a5af0fb-6cae-4997-b1ca-ce638ea8733d",
    "8aa42705-b24b-4336-a213-4560a238dacc",
    "83bc20f4-8282-45d6-81cc-e21c31cd2cdc",
    "1d9ec2e5-8b00-4076-80b9-96372fb29a72",
    "6ad072b2-c9dc-44de-86b8-f136948202e7",
    "dfeaceb9-9946-44c8-8212-50692a7d80cb",
    "34656076-dbfa-46d9-83e9-5d14ecb6a17c",
    "49ac573a-f00b-4685-b240-eb879c087930",
    "6aa595d2-e014-41b3-aef9-8df776ffb257"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProgressionInitialUnlockConfigurationObjectBuilder')
search_content('', type_contains='ProgressionInitialUnlockConfigurationObjectBuilder')
```
