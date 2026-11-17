# MusicPlaylistsConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.MusicPlaylistsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CombatPlaylist` | Combat tracks |
| `CreditsPlaylist` | Credits tracks |
| `MainMenuPlaylist` | Main menu tracks |
| `PlanetPlaylist` | Planet tracks |
| `RemoveVanillaTracks` | If true, no vanilla track will be played. Note that this applies to all playlists. |
| `SpacePlaylist` | Space tracks |

## A real one

`Engine\Assets\Configurations\MusicPlaylistsConfiguration.def`

```json
{
  "Guid": "44c94d13-b8e9-4339-955f-14aaecf66bd8",
  "RemoveVanillaTracks": false,
  "MainMenuPlaylist": [],
  "SpacePlaylist": [],
  "PlanetPlaylist": [],
  "CombatPlaylist": [],
  "CreditsPlaylist": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MusicPlaylistsConfigurationObjectBuilder')
search_content('', type_contains='MusicPlaylistsConfigurationObjectBuilder')
```
