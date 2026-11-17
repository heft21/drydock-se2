# CargoShipEncounterSessionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.CargoShips.CargoShipEncounterSessionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.CargoShips`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultDefinition` | Default spawn settings when the player is not in a sector configured in . |
| `DespawnDistance` | Distance from the closest player at which the encounter can despawn. |
| `MaxInstances` | Maximum number of instance that can spawn at once. |
| `PathMaxDistance` | Distance at which the path start and end points will be placed. |
| `PathMinDistance` | Minimum distance the cargo will be along the path from the player if the player is not moving. |
| `SectorDefinitions` | Spawn settings per . No cargo ship will spawn if the sector doesn't have a definition with at 0. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Encounter\CargoShipEncounterSessionDefinition.def`

```json
{
  "Guid": "dda619d9-d9eb-430a-8eb1-62f299150a9d",
  "MaxInstances": 1,
  "PathMinDistance": {
    "Min": 5000,
    "Max": 7000
  },
  "PathMaxDistance": 15000,
  "DespawnDistance": 4000,
  "DefaultDefinition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a",
  "SectorDefinitions": {
    "Verdure Sector": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Delfos Sector": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Kemik Sector": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Nadirae": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Oblivara": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Helionis": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Echelon": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Byblos Sector": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Tarnyx": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Zarkon": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Cygnark": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Trinarc": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Pyrethra": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Axionis": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ],
    "Vantaris": [
      {
        "Stage": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
        "Definition": "8ac002e6-b64e-4dba-8366-402e8f30fd5a"
      }
    ]
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CargoShipEncounterSessionDefinitionObjectBuilder')
search_content('', type_contains='CargoShipEncounterSessionDefinitionObjectBuilder')
```
