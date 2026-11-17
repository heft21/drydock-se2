# CargoShipEncounterSpawnDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.CargoShips.CargoShipEncounterSpawnDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.CargoShips`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Encounters` | List of cargo ship that can spawn. |
| `SpawnPerHour` | Frequency at which cargo ship encounter spawns. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Encounter\DefaultCargoShipEncounterSpawnDefinition.def`

```json
{
  "Guid": "8ac002e6-b64e-4dba-8366-402e8f30fd5a",
  "SpawnPerHour": {
    "Min": 6,
    "Max": 12
  },
  "Encounters": [
    {
      "Key": "90c129c4-2f20-4e08-b268-ec05f5da3136",
      "Value": {
        "Probability": 1,
        "Prefab": "dd8285f9-8841-454a-bbd8-8997f0090b10"
      }
    },
    {
      "Key": "cd0c4dd9-46a9-494d-ae41-e3d79d12d3df",
      "Value": {
        "Probability": 1,
        "Prefab": "9c95bcf3-fe59-4ebc-843d-4ecb6fa61d37"
      }
    },
    {
      "Key": "84e26497-8fe4-4e83-a6d0-48e880681d50",
      "Value": {
        "Probability": 1,
        "Prefab": "3a9d2387-86f4-405c-90dd-63feae963cbf"
      }
    },
    {
      "Key": "2a28b7cc-f774-4582-8870-4fc26132bc4c",
      "Value": {
        "Probability": 1,
        "Prefab": "f8c0082d-750b-4e9d-8886-c4d6dc511c4e"
      }
    },
    {
      "Key": "742e146b-83a7-4e6e-8805-6fb526fc2c74",
      "Value": {
        "Probability": 1,
        "Prefab": "553ffc79-7ec5-43d4-84bb-01889d78c7f5"
      }
    },
    {
      "Key": "a33a1638-5717-41d7-a3d8-eaef6618914e",
      "Value": {
        "Probability": 1,
        "Prefab": "57c9cf6b-d639-4352-820e-63cbb574eb0e"
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CargoShipEncounterSpawnDefinitionObjectBuilder')
search_content('', type_contains='CargoShipEncounterSpawnDefinitionObjectBuilder')
```
