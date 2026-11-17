# DiscoveriesConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Discoveries.DiscoveriesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Discoveries`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DiscoveryFanfare` | Fanfare to display when the player makes a discovery. |
| `DiscoveryUnknown` | Localized text to display for unknown discoveries, based on the . |

## A real one

`Vanilla\Assets\System\Configurations\DiscoveriesConfiguration.def`

```json
{
  "Guid": "95e916ce-288a-43f9-bd01-03811beed5f4",
  "DiscoveryFanfare": "5b236495-b2a9-4363-bd40-3a20b418409b"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DiscoveriesConfigurationObjectBuilder')
search_content('', type_contains='DiscoveriesConfigurationObjectBuilder')
```
