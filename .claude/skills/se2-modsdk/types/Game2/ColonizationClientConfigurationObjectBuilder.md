# ColonizationClientConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Colonization.ColonizationClientConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Colonization`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EndlessColonizationAvailableFanfare` | The fanfare to notify the player that endless colonization is available. |
| `OnSectorProgressAudio` | Audio event to play when the player progresses in a sector. Timed loop |
| `SectorColonizedFanfare` | The fanfare to show when the player colonizes a sector. |
| `SectorProgressAudioEndParameter` | Parameter to send to to signify the end of the loop |
| `SectorProgressAudioEndValue` | Parameter value for to signify the end of the loop |
| `SectorProgressAudioGracePeriod` | A timer of this duration will be started after the world loads, preventing all progress audio from being player until it is done. |
| `SectorProgressAudioStartValue` | Parameter value for to signify the start of the loop |
| `SectorProgressAudioTime` | How long should play in loop for each progress event |

## A real one

`Vanilla\Assets\System\Colonization\ColonizationClientConfiguration.def`

```json
{
  "Guid": "5e3c0048-3e00-448b-b8b4-2329fc5b1a3e",
  "SectorColonizedFanfare": "6c0da83d-2845-4cdf-a59d-876171a439d7",
  "EndlessColonizationAvailableFanfare": "a33f9124-dc2f-4e33-b10a-0df7caf2e90a",
  "OnSectorProgressAudio": "event:/UI/contract_sector_progress",
  "SectorProgressAudioTime": 5000000,
  "SectorProgressAudioEndParameter": "End",
  "SectorProgressAudioStartValue": 0,
  "SectorProgressAudioEndValue": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ColonizationClientConfigurationObjectBuilder')
search_content('', type_contains='ColonizationClientConfigurationObjectBuilder')
```
