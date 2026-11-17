# AudioTransitionConfigurationObjectBuilder

`Game2:Keen.Game2.Client.RuntimeSystems.Music.AudioTransitionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.RuntimeSystems.Music`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BusesToMute` | Bus paths to mute during loading |
| `InitialMusic` | Music them to start thw world with |
| `SoundRestoreDelay` | Artificial delay to restore after loading a world |

## A real one

`Vanilla\Assets\MainMenuData\Audio\AudioTransitionConfiguration.def`

```json
{
  "Guid": "167063b6-8dcd-416a-bfcc-b27a5672b121",
  "BusesToMute": [
    {
      "Key": "05ea5cfc-ea50-478a-8c51-56dcbf41d4f8",
      "Value": "bus:/SFX"
    },
    {
      "Key": "1b7d79f7-a4f7-4416-b6fe-a0f238965317",
      "Value": "bus:/UI"
    },
    {
      "Key": "4bc07aae-bdc1-460d-b69d-d1f3c902e3ab",
      "Value": "bus:/ReverbSFX"
    },
    {
      "Key": "28f7b68b-5117-4d0d-8f54-e4a9ad7fc228",
      "Value": "bus:/ReverbUI"
    },
    {
      "Key": "06f1ff36-b139-41b9-9f36-ab0822e809be",
      "Value": "bus:/VoiceLines"
    }
  ],
  "InitialMusic": "Space",
  "SoundRestoreDelay": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioTransitionConfigurationObjectBuilder')
search_content('', type_contains='AudioTransitionConfigurationObjectBuilder')
```
