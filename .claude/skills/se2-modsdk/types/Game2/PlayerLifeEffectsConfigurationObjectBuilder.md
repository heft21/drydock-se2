# PlayerLifeEffectsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Respawn.PlayerLifeEffectsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Respawn`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultDeathAudio` | Default one-shot audio event to play when the character dies. |
| `DefaultSpawnAudio` | Default one-shot audio event to play when the character spawns. |

## A real one

`Vanilla\Assets\System\Configurations\PlayerLifeEffectsConfiguration.def`

```json
{
  "Guid": "33c5f66a-da5f-4b4b-a2cc-ad602239894d",
  "DefaultSpawnAudio": "event:/UI/Character_spawn",
  "DefaultDeathAudio": "event:/UI/Character_death"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlayerLifeEffectsConfigurationObjectBuilder')
search_content('', type_contains='PlayerLifeEffectsConfigurationObjectBuilder')
```
