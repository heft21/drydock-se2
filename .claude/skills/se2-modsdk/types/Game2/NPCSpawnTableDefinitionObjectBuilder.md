# NPCSpawnTableDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.NPCSpawnTableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC`
- definitions using it: **7**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\Spawners\BoatmanColourVariants.def`

```json
{
  "Guid": "a8c1243d-0775-4f79-87d7-17969c657cc0",
  "Candidates": [
    {
      "Key": "3a35daf5-5f19-42cd-9ae5-d4284adc8517",
      "Value": {
        "Probability": 1,
        "Prefab": "04f6bb08-c713-408d-a865-824c11eb3ab8"
      }
    },
    {
      "Key": "3d277004-4419-4031-872b-c0ac964a81d3",
      "Value": {
        "Probability": 1,
        "Prefab": "f3dd3939-5054-411a-8e05-1c427972ba3a"
      }
    },
    {
      "Key": "53195fea-31e4-4d80-b422-0c4c6980d9c3",
      "Value": {
        "Probability": 1,
        "Prefab": "e08b35d5-2f8a-4bfb-bf44-4dde084de8b7"
      }
    },
    {
      "Key": "23e216e3-f48c-48ee-a68b-8afc0c33d696",
      "Value": {
        "Probability": 1,
        "Prefab": "701de7ad-03d9-4364-ad86-d218439c29e2"
      }
    },
    {
      "Key": "7a95e958-ea9f-4a4e-b4af-e271dd2be85a",
      "Value": {
        "Probability": 1,
        "Prefab": "e5bf4b57-091e-4605-9c21-35749436ba54"
      }
    },
    {
      "Key": "e86644dd-23e0-4c85-aa9a-475be7fabf02",
      "Value": {
        "Probability": 1,
        "Prefab": "2e450013-c54d-4051-b151-1481e162d44d"
      }
    },
    {
      "Key": "e5238488-55b9-4b30-a6ad-317e76a5fe26",
      "Value": {
        "Probability": 1,
        "Prefab": "271785fa-34c5-4200-a277-20e7aa4148f1"
      }
    },
    {
      "Key": "24da0e28-93dc-43c7-b2ba-d5da44b0ecd7",
      "Value": {
        "Probability": 1,
        "Prefab": "3ed4d994-5b52-493b-ae9d-38c2bbaa1835"
      }
    },
    {
      "Key": "968770c6-ccc6-4f0f-9f2c-bec1bb18174e",
      "Value": {
        "Probability": 1,
        "Prefab": "f944fee2-a949-4055-94b4-c7c0f3eb2d56"
      }
    },
    {
      "Key": "ebfbb243-418e-4cc8-bea9-8f51d8485ca5",
      "Value": {
        "Probability": 1,
        "Prefab": "534214b7-de22-4a57-b1cd-8910bfc92cae"
      }
    }
  ]
}
```

Others: `RenegadeColourVariants`, `BoatmanMaleColourVariants`

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCSpawnTableDefinitionObjectBuilder')
search_content('', type_contains='NPCSpawnTableDefinitionObjectBuilder')
```
