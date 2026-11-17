# AudioBanksConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.AudioBanksConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PreloadedBanks` | A list of FMOD Banks that are preloaded during game startup. |

## A real one

`Vanilla\Assets\MainMenuData\Audio\AudioBanksConfiguration.def`

```json
{
  "Guid": "af6006b2-ad4d-4649-bab4-59a6194e6eec",
  "PreloadedBanks": [
    {
      "Key": "b7bf65b9-fb02-4fa8-92ec-2aae7df2fd19",
      "Value": "UI.bank"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioBanksConfigurationObjectBuilder')
search_content('', type_contains='AudioBanksConfigurationObjectBuilder')
```
