# SpectatingModesComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Spectators.SpectatingModesComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Spectators`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterControl` | Input to take possession of next controllable character |
| `DeltaSpectator` | Input to switch to delta spectator mode |
| `FreeSpectator` | Input to switch to free-roaming spectator mode |
| `InputContextDefinition` | Context for spectator mode inputs |
| `SpectatorPrefab` | Spectator entity to spawn for local client/player when entering spectator mode |
| `StaticSpectator` | Input to switch to static spectator mode |
| `TeleportPlayerToSpectator` | Input to teleport first character found in scene to current local player/spectator position and possess it |
| `TeleportSpectatorToPlayer` | Input for teleporting the spectator to the currently controlled entity. |

## A real one

`Vanilla\Assets\System\Spectator\ComponentSpectatorInput.def`

```json
{
  "Guid": "af11e5fc-cddf-417d-a11c-32be80bb40c6",
  "SpectatorPrefab": "a1f0b0c0-4031-4766-8747-31abf0c288c7",
  "InputContextDefinition": "a73644a4-5118-459b-8cbd-8b793a86a784",
  "FreeSpectator": "45d22fd9-c4bf-447f-bc4d-c7c2b1af8337",
  "StaticSpectator": "3ba81530-c7f4-4d86-a73b-685c16caae77",
  "DeltaSpectator": "5966491a-62d5-4b3e-8ba0-9911e7936ede",
  "CharacterControl": "cac55fe6-28e5-4e27-9f97-6e1bc25f0c55",
  "TeleportPlayerToSpectator": "eb236853-2d35-499a-aaef-b430f0b0037a",
  "TeleportSpectatorToPlayer": "02dcd144-af3d-444f-8c4f-1f5e094d9898"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpectatingModesComponentDefinitionObjectBuilder')
search_content('', type_contains='SpectatingModesComponentDefinitionObjectBuilder')
```
