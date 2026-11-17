# ContractBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ContractBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **12**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OptionalContractCount` | Number of contract that will be generated from the . |
| `OptionalContracts` | List of optional contracts that may be generated. |
| `RequiredContracts` | List of required contracts that are always generated. |

## A real one

`Vanilla\Assets\Colonization\VS2-3\Contracts\Kemik_ContractBlockDefinition.def`

```json
{
  "Guid": "3f70cbff-edea-475f-bd7c-7c5fbae13728",
  "RequiredContracts": [
    {
      "Key": "744ae64a-7db7-442b-8b86-2ae90911adb5",
      "Value": "b5371e63-d8fc-4f21-aa6e-2b687fd5284f"
    },
    {
      "Key": "5adc4c8a-e115-4818-92ac-11e2ee77b738",
      "Value": "b0df1437-0c67-4240-8451-622ca6aba182"
    },
    {
      "Key": "694b9ed7-0712-405f-8795-e3fbe889bd22",
      "Value": "717f863d-901d-4f62-82bc-4341720ba404"
    },
    {
      "Key": "209d4504-8477-4d8d-997c-78567ab91e13",
      "Value": "896c3e8b-9936-4fbe-8de3-e9a97ca1cbfb"
    },
    {
      "Key": "b7e2b3ea-1832-430f-8d19-ffbfecf416c3",
      "Value": "f3cc3e02-6ac1-42aa-87e4-b57530f9d781"
    }
  ],
  "OptionalContractCount": 0,
  "OptionalContracts": []
}
```

Others: `TestKemik23_ContractBlockDefinition`, `NPCDemoContractBlockDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractBlockDefinitionObjectBuilder')
search_content('', type_contains='ContractBlockDefinitionObjectBuilder')
```
