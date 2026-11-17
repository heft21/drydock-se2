# SpectatingModesConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Spectators.SpectatingModesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Spectators`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DeltaSpectatorKey` | Delta Spectator camera mode key |
| `StaticSpectatorKey` | Static Spectator camera mode key |

## A real one

`Vanilla\Assets\System\Controller\NamedCameraPrefabs\SpectatingModesConfiguration.def`

```json
{
  "Guid": "e12073de-2a51-4dab-b610-0db7902f988e",
  "DeltaSpectatorKey": "104cf078-21fa-41a8-a28a-022132fdef37",
  "StaticSpectatorKey": "443536e7-6513-4fbd-a77b-9fbfa9ab9ca4"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpectatingModesConfigurationObjectBuilder')
search_content('', type_contains='SpectatingModesConfigurationObjectBuilder')
```
