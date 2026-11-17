# ContractNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Contracts.ContractNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Contracts`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AvailableGPSMarker` | GPS type to display when contracts are available. |
| `AvailableGPSMarkerDelay` | Delay before the GPS shows up. |
| `AvailableGPSMarkerName` | Name used on the GPS marker. |
| `ContractFailedKey` | Text of notification shown when the player fails a contract |
| `OnContractCompletedFanfare` | Fanfare shown when the active contract is marked as finished (can be collected) |
| `ReminderEnabled` | Enable the periodic "go do some contracts" reminder notifications (in survival mode only) |
| `ReminderInterval` | Time interval controlling the how often the contract reminder notifications are displayed |
| `ReminderNotifications` | List of contract reminder notification variants |

## A real one

`Vanilla\Assets\System\Configurations\ContractNotificationsConfiguration.def`

```json
{
  "Guid": "9fee0dcb-1d90-4813-a8af-56ff19558a12",
  "OnContractCompletedFanfare": "8ea586b8-ce4c-4200-8f06-af9291bb2ea8",
  "ContractFailedKey": "HUDNotificationContractFailed",
  "ReminderEnabled": true,
  "ReminderNotifications": [
    {
      "Key": "65a29c06-02f5-4335-b0bb-f3544ee453b2",
      "Value": "9a350dc0-f42b-4432-b377-8f11dca51a29"
    },
    {
      "Key": "a3907c34-b390-4a7d-ac97-9d84ff3e0e0d",
      "Value": "0a348247-6710-4b99-a85d-0e7c13fdba24"
    },
    {
      "Key": "98599bc9-3b17-44cd-ae6b-e6d9c432532c",
      "Value": "a61ab02b-da64-4733-9f05-76acbe0a10c0"
    },
    {
      "Key": "c11bea54-19f9-46eb-af3b-7d4a8aa9170a",
      "Value": "1aafe024-104a-4b7f-89b9-2e3414d64c8a"
    },
    {
      "Key": "1d76a282-e39e-4275-bea2-04a507f4fc0a",
      "Value": "a1b973f6-0472-4d82-8664-d48bac6d90e5"
    },
    {
      "Key": "97013a15-1cdd-4462-bcfe-703322c0d874",
      "Value": "dde3e95e-972c-409e-be2c-4beacfb79dc6"
    },
    {
      "Key": "7b1a8f70-a64b-4342-898c-2683d69dfd9c",
      "Value": "f98d11d5-a20a-4029-ad65-b01b82dd7b42"
    },
    {
      "Key": "e09acc8d-59dd-4096-9c2e-1ec8b98df92e",
      "Value": "c3bd831c-d26d-4bc4-a455-31799a4190b1"
    },
    {
      "Key": "796f07af-eafa-4bb8-b818-3754f75ed27f",
      "Value": "32cc3c4b-c741-42de-9776-b02a319c893d"
    }
  ],
  "ReminderInterval": 36000000000,
  "AvailableGPSMarker": "4b71d10d-a503-4cf7-82aa-1b62b4d40af2",
  "AvailableGPSMarkerName": "ContractsNext",
  "AvailableGPSMarkerDelay": 50000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractNotificationsConfigurationObjectBuilder')
search_content('', type_contains='ContractNotificationsConfigurationObjectBuilder')
```
