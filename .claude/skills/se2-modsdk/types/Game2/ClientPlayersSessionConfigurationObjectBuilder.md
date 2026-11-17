# ClientPlayersSessionConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.ClientPlayersSessionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PlayerController` | Prefab with that will be spawned for the local player on the client-side and is responsible for dealing with possession of entities. It also must carry the as its responsibility also include dealing with camera modes. |
| `RenderCamera` | Camera prefab to spawn for local player on client side. |

## A real one

`Vanilla\Assets\System\ClientPlayerDefinition.def`

```json
{
  "Guid": "7b25b543-a10e-473e-a600-a23170340372",
  "PlayerController": "a7370ee6-ab20-45d3-a47c-05c317770158",
  "RenderCamera": "8a6b77be-837d-4866-a8a8-cadebcf78dd1"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ClientPlayersSessionConfigurationObjectBuilder')
search_content('', type_contains='ClientPlayersSessionConfigurationObjectBuilder')
```
