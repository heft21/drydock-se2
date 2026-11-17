# SectorsSessionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Colonization.SectorsSessionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Colonization`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InitialStage` | Initial stage per sector name. When not set use the first entry from . |
| `Stages` | Stage the world uses. Requires at least 2 stage to represent the locked and colonized stages. |

## A real one

`Vanilla\Assets\Colonization\VS2-3\Sectors\Default_SectorsSessionDefinition.def`

```json
{
  "Guid": "6d4d73b0-8d86-4e21-b18d-a3bd6c4eac3f",
  "Stages": [
    {
      "Key": "b86271af-0ae2-453a-b114-3069e657cfb0",
      "Value": "fd17e5ef-9a88-4585-843d-44bb9997b61c"
    },
    {
      "Key": "087d8cd7-7e6b-4cee-b178-db89bed2a843",
      "Value": "c812ed86-996a-4eea-b175-89ffcc93679d"
    },
    {
      "Key": "8e1597ed-7234-48e7-8748-9245fc1bbf05",
      "Value": "dda10f29-89a1-403f-8611-9aed4c9bdaf4"
    },
    {
      "Key": "604f5b4d-025c-46f4-9694-a3c5948818a2",
      "Value": "77344e8f-6a1b-41c8-b375-8f31ab3d899a"
    },
    {
      "Key": "6df478de-8654-4ab5-a072-4a62ce41010f",
      "Value": "fa82aba8-e699-451d-886a-bda91cd3c90c"
    }
  ],
  "InitialStage": {}
}
```

Others: `Survival_SectorsSessionDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SectorsSessionDefinitionObjectBuilder')
search_content('', type_contains='SectorsSessionDefinitionObjectBuilder')
```
