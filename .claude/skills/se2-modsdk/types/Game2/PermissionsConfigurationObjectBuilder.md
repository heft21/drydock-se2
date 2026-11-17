# PermissionsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Permissions.PermissionsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Permissions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AccessesAllCrew` | All Accesses that are for crew ownership |
| `AccessesAllPersonal` | All Accesses that are for personal ownership |
| `AdvancedUse` | Key representing advanced actions that can be performed with block. |
| `BasicUse` | Key representing basic actions that can be performed with block. The most general kind. |
| `CrewAccess` | Key representing access allowed only for crew and owner/owners. |
| `EveryoneAccess` | Key representing access allowed for everyone. |
| `FriendAccess` | Key representing access allowed only for friendly crews, crew and owner/owners. |
| `GridConnectionsRequiringSameOwner` | List of connection types that require two connecting grids to have the same owner |
| `OwnerAccess` | Key representing access allowed only for owner/owners. |
| `UnrestrictedUse` | Key representing all actions that can be performed with block. Should cover all actions except owner specific ones. |
| `UsesAdvanced` | All uses included in AdvancedUse |
| `UsesAll` | All Use settings that are available |
| `UsesBasic` | All uses that are included in BasicUse |
| `UsesUnrestricted` | All uses included in UnrestrictedUse |

## A real one

`Vanilla\Assets\System\Configurations\PermissionsConfig.def`

```json
{
  "Guid": "7b92355b-ae1b-465a-8fed-260f1e7e60bc",
  "GridConnectionsRequiringSameOwner": [
    "2ed2d414-fedb-42a2-bc75-2b26417e1346"
  ],
  "OwnerAccess": "Owner",
  "CrewAccess": "Crew",
  "FriendAccess": "Friendly",
  "EveryoneAccess": "Everyone",
  "AccessesAllPersonal": [
    {
      "Key": "e1eabe7e-e8eb-4709-9958-732e247fbe40",
      "Value": "Owner"
    },
    {
      "Key": "63b4d120-e9c0-4d79-95ee-c7d26894a3b9",
      "Value": "Crew"
    },
    {
      "Key": "3c73f8e8-1926-4ed9-b4c6-6e0ce9e08fe1",
      "Value": "Friendly"
    },
    {
      "Key": "d9216444-84d3-40eb-aa6c-437fa79069c9",
      "Value": "Everyone"
    }
  ],
  "AccessesAllCrew": [
    {
      "Key": "13674183-318d-4ede-8edf-17b43425fe4e",
      "Value": "Crew"
    },
    {
      "Key": "264cd567-e192-4f47-8fcc-c33cb1c3da52",
      "Value": "Friendly"
    },
    {
      "Key": "d7827a5d-54fb-4438-b801-f9ba4b79d9ee",
      "Value": "Everyone"
    }
  ],
  "BasicUse": "Basic",
  "AdvancedUse": "Advanced",
  "UnrestrictedUse": "Unrestricted",
  "UsesAll": [
    {
      "Key": "89abf516-3829-40cb-858c-dbee4b35dd80",
      "Value": "Basic"
    },
    {
      "Key": "b5294d31-5bee-4535-8d06-f68e3a13de0f",
      "Value": "Advanced"
    },
    {
      "Key": "97e12d9a-e9b6-4329-864e-67f246c58d72",
      "Value": "Unrestricted"
    }
  ],
  "UsesBasic": [
    "Basic"
  ],
  "UsesAdvanced": [
    "Basic",
    "Advanced"
  ],
  "UsesUnrestricted": [
    "Basic",
    "Advanced",
    "Unrestricted"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PermissionsConfigurationObjectBuilder')
search_content('', type_contains='PermissionsConfigurationObjectBuilder')
```
