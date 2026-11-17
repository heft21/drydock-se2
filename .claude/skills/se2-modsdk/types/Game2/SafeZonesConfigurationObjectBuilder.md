# SafeZonesConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.SafeZones.SafeZonesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.SafeZones`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SafeZonePrefab` | Server prefab for spawning safe zone entity. |
| `SphereModel` | Model of the sphere paint brush used by spherical safe zones. |

## A real one

`Vanilla\Assets\System\Configurations\SafeZonesConfiguration.def`

```json
{
  "Guid": "76696532-3d33-4462-8a38-436e54df532a",
  "SafeZonePrefab": "84eec496-0db6-455b-8313-de21e515f9c5",
  "SphereModel": "{G}453eb012-d409-4689-ac68-6d058a2328e4"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SafeZonesConfigurationObjectBuilder')
search_content('', type_contains='SafeZonesConfigurationObjectBuilder')
```
