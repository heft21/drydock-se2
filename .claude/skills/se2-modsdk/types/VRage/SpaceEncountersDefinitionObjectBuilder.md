# SpaceEncountersDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.ProceduralGeneration.SpaceEncountersDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.ProceduralGeneration`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Density` | The desired number of encounters per cubic kilometer. |
| `Encounters` | List of all encounters that can be generated. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Encounter\SpaceEncountersDefinition.def`

```json
{
  "Guid": "680501d2-bc43-417c-8f49-0ab209e3a982",
  "Density": 0.00015,
  "Encounters": [
    {
      "Key": "f66fb7dd-8831-42d9-9f6b-954791ddf834",
      "Value": {
        "EntityPrefab": "cdd9be20-471f-4341-b33a-46d198b30940",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "3a325487-0dab-45d1-8746-d9fde6b5ed13",
      "Value": {
        "EntityPrefab": "73cada0f-8fce-44c6-b044-396579d3a161",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "d254d70b-c22d-4b31-a968-f3bc631d8038",
      "Value": {
        "EntityPrefab": "09e69900-5dc1-4f4e-9ced-4c6f94870c5d",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "0158ef97-c6ad-4019-8b4a-3c16e7b3ed36",
      "Value": {
        "EntityPrefab": "83a5d333-60d4-4d11-a0d6-700c9952d426",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "fd8ad22b-ad44-499d-8999-00bd8ca5a9e0",
      "Value": {
        "EntityPrefab": "51ea37b3-9dae-420f-b577-e6e394d63f67",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "43b92a53-4486-4830-8391-3b962304c7c7",
      "Value": {
        "EntityPrefab": "0829d7c7-3679-4e21-bc83-64dde19603ba",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "c1b2ec99-41c3-4180-8bb1-54f9a46abc7b",
      "Value": {
        "EntityPrefab": "7ed22360-5637-4fdd-9903-672b58bb17e0",
        "Probability": 0.125,
        "RandomRotation": true
      }
    },
    {
      "Key": "2ae8bed9-9eea-4534-bdf9-e779d0bc8c30",
      "Value": {
        "EntityPrefab": "44c948a7-b582-412f-9c22-84bce780a159",
        "Probability": 0.125,
        "RandomRotation": true
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpaceEncountersDefinitionObjectBuilder')
search_content('', type_contains='SpaceEncountersDefinitionObjectBuilder')
```
