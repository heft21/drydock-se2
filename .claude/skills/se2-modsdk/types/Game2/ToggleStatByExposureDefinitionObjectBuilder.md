# ToggleStatByExposureDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.ToggleStatByExposureDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ComponentEnabled` | If this stat is on (has value greater than min) is enabled. Disabled otherwise |
| `DelayBeforeDisable` | Amount of time exposure must be less than for to be set to its |
| `DelayBeforeEnable` | Amount of time exposure must be greater than for to be set to its |
| `ExposureDisableThreshold` | If exposure is less than this value, is to be set to its after has passed |
| `ExposureEnableThreshold` | If exposure is greater than this value, is to be set to its after has passed |
| `StatToToggle` | Stat to be controlled by |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\CharacterPrefabInputAdapter_ToggleStatByExposureDefinition.def`

```json
{
  "Guid": "08eb981b-b072-4142-9437-5f0d1e5ad4ab",
  "StatToToggle": "b4de981d-1ed7-4603-95c8-e76f6281a928",
  "ComponentEnabled": "73b66f23-d596-474c-b481-2ca6a1458990",
  "ExposureDisableThreshold": 0.15,
  "ExposureEnableThreshold": 1.3,
  "DelayBeforeEnable": 10000000,
  "DelayBeforeDisable": 129999997
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToggleStatByExposureDefinitionObjectBuilder')
search_content('', type_contains='ToggleStatByExposureDefinitionObjectBuilder')
```
