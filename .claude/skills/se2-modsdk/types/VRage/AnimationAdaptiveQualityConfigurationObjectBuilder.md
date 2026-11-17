# AnimationAdaptiveQualityConfigurationObjectBuilder

`VRage:Keen.VRage.Animation.AdaptiveQuality.AnimationAdaptiveQualityConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.AdaptiveQuality`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\AnimationAdaptiveQualityConfiguration.def`

```json
{
  "Guid": "957135f5-1a5b-4d16-a2a9-eaafc3a2ff1d",
  "ObserverTag": "AnimationObserver",
  "TargetUpdatesPerFrame": 6,
  "MaxBuckets": 4
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AnimationAdaptiveQualityConfigurationObjectBuilder')
search_content('', type_contains='AnimationAdaptiveQualityConfigurationObjectBuilder')
```
