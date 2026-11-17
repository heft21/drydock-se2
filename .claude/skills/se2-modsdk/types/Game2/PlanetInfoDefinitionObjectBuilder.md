# PlanetInfoDefinitionObjectBuilder

`Game2:Keen.Game2.Client.Debugging.Screens.Voxels.PlanetInfoDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Debugging.Screens.Voxels`
- definitions using it: **15**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Friendly name for this planet, displayed in debug menu list |
| `Preview` | The preview version of the planet |
| `Spawn` | The spawned/placed version of the planet |

## A real one

`Vanilla\Assets\Procedural\VS3_0\Planets\Byblos\Data\PlanetInfoDefinition.def`

```json
{
  "Guid": "e6f43029-a1dc-4285-b318-cdceca75d655",
  "Name": "Byblos",
  "Preview": "ab7795e6-b1be-44df-9f05-d002ff859409",
  "Spawn": "9658d1f0-2ecc-4097-99b0-dc9dd4818ebc"
}
```

Others: `VerdureInfoDefinition`, `KemikInfoDefinition_VS2-3`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetInfoDefinitionObjectBuilder')
search_content('', type_contains='PlanetInfoDefinitionObjectBuilder')
```
