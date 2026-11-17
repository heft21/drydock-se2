# GPSMarkerTypeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GPS.GPSMarkerTypeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GPS`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Editable` | Can player edit markers in this group? |
| `Name` | TextKey for the name of the marker type (Example "System"/"Personal") |

## A real one

`Vanilla\Assets\System\Mission\MissionGPSMarkerType.def`

```json
{
  "Guid": "3d5ca81c-5453-4012-869e-e7c07080b5d3",
  "Name": "Mission",
  "Editable": false
}
```

Others: `SystemGPSMarkerType`, `UserGPSMarkerTypedef`

---

Read it with the MCP server rather than by hand:

```
describe_type('GPSMarkerTypeDefinitionObjectBuilder')
search_content('', type_contains='GPSMarkerTypeDefinitionObjectBuilder')
```
