# AudioEventPoolConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.AudioEventPoolConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultEventLimits` | Default simultaneous max event instance count |
| `EventLimits` | Simultaneous max event instance count |
| `Pools` | Pools for individual events |

## A real one

`Vanilla\Assets\MainMenuData\Audio\AudioEventPoolConfiguration.def`

Too large to inline. Fields present:

`DefaultEventLimits`, `EventLimits`, `Guid`, `Pools`

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioEventPoolConfigurationObjectBuilder')
search_content('', type_contains='AudioEventPoolConfigurationObjectBuilder')
```
