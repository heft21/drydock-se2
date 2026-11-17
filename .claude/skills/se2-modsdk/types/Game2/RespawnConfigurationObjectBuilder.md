# RespawnConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Respawn.RespawnConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Respawn`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AudioFadeIn` | Audio event to fade in sounds when player is respawning |
| `AudioFadeOut` | Audio event to fade out sounds when player is respawning |
| `CharacterVariantPrefabs` | Variants of a character that can be spawned |
| `DeathScreenDuration` | Duration for which the death screen stays displayed before the respawn screen is shown. |
| `DefaultCharacterPrefab` | Physical player character to create at respawn |
| `FadeInDuration` | Duration for screen fade in when player starts respawned, resources were streamed and it's possible to take control |
| `FadeoutDuration` | Duration for screen fade out when player starts respawning (must be in sync with audio) |
| `NotificationTimeOut` | How long the activation/deactivation notifications should show |
| `PlayersBackpackEmptyTitle` | Text used for player's empty backpack GPS - {player}'s backpack (empty). |
| `PlayersBackpackTitle` | Text used for player's backpack GPS - {player}'s backpack. |
| `RespawnClosestNotificationContent` | Content of message shown when respawning at the nearest block |
| `RespawnClosestNotificationTitle` | Title of message shown when respawning at the nearest block |
| `RespawnDefaultNotificationContent` | Content of message shown when respawning at the default location |
| `RespawnDefaultNotificationTitle` | Title of message shown when respawning at the default location |
| `RespawnHomeNotificationContent` | Content of message shown when respawning at the home base |
| `RespawnHomeNotificationTitle` | Title of message shown when respawning at the home base |
| `RespawnPointClaimed` | Text shown when an unowned respawn point is claimed |
| `RespawnPointHomeClear` | Text shown when an owned respawn point is deactivated |
| `RespawnPointHomeSet` | Text shown when an owned respawn point is activated |
| `RespawnPointUnclaimed` | Text shown when an unowned respawn point is unclaimed |
| `SafeRespawnAltitude` | Maximum height in meters (from the ground) that the player can respawn from before the jetpack automatically activates |
| `UnknownDeathMessage` | Text shown when a player has died from unknown causes |

## A real one

`Vanilla\Assets\System\ServerComponentRespawn.def`

Too large to inline. Fields present:

`AudioFadeIn`, `AudioFadeOut`, `BoundItems`, `CharacterVariantPrefabs`, `DeathScreenDuration`, `DefaultCharacterPrefab`, `DefaultSpectatorPrefab`, `FadeInDuration`, `FadeoutDuration`, `Guid`, `NotificationTimeOut`, `PlayersBackpackEmptyTitle`, `PlayersBackpackTitle`, `RespawnClosestNotificationContent`, `RespawnClosestNotificationTitle`, `RespawnDefaultNotificationContent`, `RespawnDefaultNotificationTitle`, `RespawnHomeNotificationContent`, `RespawnHomeNotificationTitle`, `RespawnPointClaimed`, `RespawnPointHomeClear`, `RespawnPointHomeSet`, `RespawnPointUnclaimed`, `SafeRespawnAltitude`, `UnknownDeathMessage`

---

Read it with the MCP server rather than by hand:

```
describe_type('RespawnConfigurationObjectBuilder')
search_content('', type_contains='RespawnConfigurationObjectBuilder')
```
