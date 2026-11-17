# AnimationResourceStreamingConfigurationObjectBuilder

`VRage:Keen.VRage.Animation.Configurations.AnimationResourceStreamingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Configurations`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CatchUpFramesCount` | The number of frames it takes to transition to the correct animation pose after the clip becomes available. Applied when the animation is already in progress. |

## A real one

`Engine\Assets\Configurations\Setup\AnimationResourceStreamingConfiguration.def`

```json
{
  "Guid": "6ed0ce44-ec46-4f86-a213-259fe938cc81",
  "CatchUpFramesCount": 10
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AnimationResourceStreamingConfigurationObjectBuilder')
search_content('', type_contains='AnimationResourceStreamingConfigurationObjectBuilder')
```
