# MissionObjectiveNotificationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Missions.MissionObjectiveNotificationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Missions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `JingleAudioVolume` | Volume from 0 to 100% to play for and |
| `ObjectiveCompletedKey` | Localization key representing the completion of the objective |
| `ObjectiveFailedKey` | Localization key used for failed objective notifications |
| `ObjectiveNotificationIcon` | Icon for objective notification |
| `OnObjectiveChangeAudio` | Audio event to play on objective change |
| `OnObjectiveCompleteAudio` | Audio event to play on objective completed |

## A real one

`Vanilla\Assets\System\Configurations\MissionObjectiveNotificationConfiguration.def`

```json
{
  "Guid": "44a413e0-1d21-4cee-a718-f67c4e9f06e8",
  "ObjectiveNotificationIcon": "{G}d5af2a12-1508-4046-944f-fccf44723e9e",
  "ObjectiveCompletedKey": "HUDNotificationObjectiveCompleted",
  "ObjectiveFailedKey": "HUDNotificationObjectiveFailed",
  "PendingContractObjectiveKey": "PendingContractObjectiveKey",
  "OnObjectiveChangeAudio": "event:/UI/jingle_objective_update",
  "OnObjectiveCompleteAudio": "event:/UI/jingle_objective_complete",
  "JingleAudioVolume": 0.25
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MissionObjectiveNotificationConfigurationObjectBuilder')
search_content('', type_contains='MissionObjectiveNotificationConfigurationObjectBuilder')
```
