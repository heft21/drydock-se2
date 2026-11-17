# MaterialGroupDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Toolbars.VoxelHand.MaterialGroupDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Toolbars.VoxelHand`
- definitions using it: **12**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BrushMaterials` | List of materials that can be painted with this brush |
| `Name` | Name of this material group (localization id) TODO SE2-12005 |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\BrushMaterialGroup1.def`

```json
{
  "Guid": "a0addcfe-64fd-42f1-9aa8-a8f31b1867a1",
  "Name": "Default group 1",
  "BrushMaterials": [
    "1f5d7d9b-9fe5-4fbc-8b88-42794e005137",
    "30ca48a2-d182-4892-8629-60433c18883f",
    "b177cb28-26d2-4c2a-bbf9-1d327a469984",
    "35f1586f-1355-4f29-a7c5-b4ac9cd5c9b3",
    "99252318-6504-471b-a0ed-1dbc3ed4cf74",
    "f8b691dc-7aa1-4a44-afa6-f55bcdf78571",
    "dd82e401-023d-4fa2-9865-69d9ddb8bb26",
    "7ab03171-3a9a-4f71-af46-9a346cec4d41",
    "79d74f30-d304-43f7-867f-a7cfc19f28b7",
    "cb218f70-7a84-4524-ad3f-9916e1bd7b0a",
    "c8c6dbdc-7d41-423f-a6bf-4c90b58664b2",
    "be265265-42f4-4609-80c0-7df3eb969a8d",
    "3afcf52b-3134-41b6-85ad-37a06cf9cb25",
    "487755b7-f3ce-440e-86c4-0bf11989d565",
    "27005d01-386d-4f9a-bbd9-f80f9d280d68",
    "509fdeb8-cd07-4a81-911b-1f7dd65a79cd",
    "4644318b-b07c-44d4-bde8-f2c54c086584",
    "8e9a26f2-70c4-4be3-9a3c-89c47e53657b",
    "1c47a44c-3d96-49c7-911c-529ecda31ac7",
    "7659df4e-a405-4b9a-b67b-1858bfc45b5f",
    "2be020a3-440f-48ed-a62b-05274d52bcf4",
    "5b132e78-209c-4036-8db9-4dd5f76878ea",
    "dcc37ad0-1c9e-4949-bb42-380dac53deec",
    "f7d67f44-2b11-45d7-9a0f-9ef2a0a0bc2b",
    "7953219c-6df7-4be0-b56e-473c03eefa34",
    "2bde9647-c6c4-4585-bac0-804fe2ec9dba",
    "98f5c5a7-7cf6-4ecd-ab17-e2f251ca6adf",
    "00109137-7fcf-4ae4-a687-241f9d0a2fbc",
    "18ffa7a4-e8a6-469e-bb41-bd806774dfce",
    "8ce42d81-0100-40f2-b37f-8ae519e8f0c0",
    "4c7d4cd3-ede4-430c-92fc-1a04eebf9077",
    "4af460d1-5dd1-420d-af7b-be9c91409a8d",
    "e3886d85-0a72-404d-89f4-5bfeb47ce1a2"
  ]
}
```

Others: `BrushMaterialGroup2`, `BrushMaterialGroup_Moon`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialGroupDefinitionObjectBuilder')
search_content('', type_contains='MaterialGroupDefinitionObjectBuilder')
```
