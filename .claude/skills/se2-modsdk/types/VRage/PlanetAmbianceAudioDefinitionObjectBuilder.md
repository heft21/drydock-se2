# PlanetAmbianceAudioDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.PlanetAmbianceAudioDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AltitudeParameterName` | Parameter name for selecting the current altitude. |
| `BiomeParameterName` | Parameter name used when selecting the current biome. |
| `DefaultPlanetPlaylist` | Default playlist to use on planet when a biome doesn't have a specific playlist |
| `HighAltitudeValue` | Parameter value for high altitudes. |
| `LowAltitudeCutoffPoint` | Threshold altitude from the planet's base ground level for selecting the altitude parameter: applies below this threshold; applies at or above it. |
| `LowAltitudeValue` | Parameter value for low altitudes. |
| `MaxAltitude` | Maximum distance above the planet's base ground level at which this planet's ambiance audio is used. |
| `PlanetAmbianceAudio` | Audio event containing ambiance music related to this planet. The music that will be played may vary based on several parameters, such as the current location of the local player and/or time of the day at that location. |
| `PlanetBiomeMusicTracks` | Dictionary of music playlists to play per biome |

## A real one

`Vanilla\Assets\Templates\Planets\PlanetAmbianceAudio.def`

```json
{
  "Guid": "b603a581-5664-413a-b342-7fadeb54ea00",
  "PlanetAmbianceAudio": null,
  "DefaultPlanetPlaylist": null,
  "PlanetBiomeMusicTracks": {},
  "MaxAltitude": 10000,
  "LowAltitudeCutoffPoint": 10000,
  "BiomeParameterName": "Biome",
  "AltitudeParameterName": "Altitude",
  "LowAltitudeValue": 0,
  "HighAltitudeValue": 1
}
```

Others: `EarthLikeAmbianceAudio`, `VerdureAmbianceAudio`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetAmbianceAudioDefinitionObjectBuilder')
search_content('', type_contains='PlanetAmbianceAudioDefinitionObjectBuilder')
```
