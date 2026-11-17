# RespawnPointEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Respawn.RespawnPointEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Respawn`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnRespawnPointClaimedAsHomeAudio` | Audio event to play when a respawn point is claimed as home by the local player. One shot audio |

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\RespawnPointEffectsDefinition.def`

```json
{
  "Guid": "f78bef28-f4df-414b-93fa-91d5a6f10c92",
  "OnRespawnPointClaimedAsHomeAudio": "event:/UI/Block/RegisterDeregisterBlock",
  "OnRespawnPointClaimedAudio": "event:/UI/Block/RegisterDeregisterBlock",
  "OnRespawnPointUnclaimedAudio": "event:/UI/Block/RegisterDeregisterBlock"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RespawnPointEffectsDefinitionObjectBuilder')
search_content('', type_contains='RespawnPointEffectsDefinitionObjectBuilder')
```
