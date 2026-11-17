# MusicPlaylistDefinitionObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.MusicPlaylistDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Tracks` | List of tracks to play with this playlist |

## A real one

`Vanilla\Assets\System\Configurations\CombatMusicConfiguration_MusicPlaylistDefinition.def`

```json
{
  "Guid": "ab68bd9f-3578-4604-a7af-21154a4e1ee9",
  "Tracks": [
    {
      "Key": "f268a3d4-12f8-4dbf-8c8c-014390e00f9a",
      "Value": "event:/Music/Combat/CombatTest"
    },
    {
      "Key": "40a3fd2c-ea65-4ca1-82f8-d5e2def895f0",
      "Value": "event:/Music/Combat/Combat2"
    },
    {
      "Key": "2529488b-7f97-4f03-84e9-9492cc70db97",
      "Value": "event:/Music/Combat/Combat3"
    },
    {
      "Key": "9c78daef-57a1-4ef8-a851-d3a24e0fb845",
      "Value": "event:/Music/Combat/Combat4"
    },
    {
      "Key": "0ef77283-572e-4722-8ef8-0eaab5252c00",
      "Value": "event:/Music/Combat/Combat5"
    },
    {
      "Key": "5d125c5b-f9e1-4fd5-9bbb-6cb4735af4fd",
      "Value": "event:/Music/Combat/Combat6"
    }
  ]
}
```

Others: `Kemik_DefaultMusicPlaylistDefinition`, `Verdure_DefaultMusicPlaylistDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MusicPlaylistDefinitionObjectBuilder')
search_content('', type_contains='MusicPlaylistDefinitionObjectBuilder')
```
