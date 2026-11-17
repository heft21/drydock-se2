# PerceptionProfileDefinitionObjectBuilder

`VRage:Keen.VRage.AI.Perception.PerceptionProfileDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.AI.Perception`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlertDecayRate` | Rate at which alertness decays per second when no hostile stimulus is active. |
| `AlertThreshold` | AlertnessLevel threshold to transition from Suspicious to Alert. |
| `AudioSensitivity` | Audio sensitivity multiplier. Higher values detect quieter sounds. |
| `AudioThreatDuration` | How long an audio threat persists for investigation after the last stimulus (seconds). |
| `BaseVisualPerceptionRate` | Base perception accumulation rate for visual sense (units/sec at optimal conditions). |
| `BodyHeightFraction` | Estimated body/torso height as fraction of EyeHeight. Used for LOS body raycast target. |
| `EyeHeight` | Eye height above entity origin (meters). Used for visual sense raycast origin. |
| `HearingMaxDistance` | Maximum hearing distance in meters. |
| `MaxObscuredTime` | Time a target can be obscured (LOS blocked) before transitioning to Memory. V1 MaxObscuredTime. |
| `MaxRaycastsPerTick` | Maximum number of raycasts per perception tick for this NPC. |
| `MemoryRetentionTime` | How long a target is retained in Memory state before being forgotten (seconds). |
| `MemoryUncertaintyGrowthRate` | Rate at which position uncertainty grows in Memory state (meters/sec). |
| `PartialToFullThreshold` | PerceivedAmount threshold to transition from Partial to Full. |
| `PerceptionDecayRate` | Rate at which PerceivedAmount decays per second when no stimulus is active. |
| `PrimaryFOVDegrees` | Primary (narrow) vision cone full angle in degrees. |
| `ProximityRadius` | Range at which entities are immediately fully perceived (meters). |
| `RaycastInterval` | Minimum time between raycasts for the same target (seconds). V1 RaycastRate. |
| `SecondaryFOVDegrees` | Secondary (wide) vision cone full angle in degrees. |
| `SecondaryFOVWeight` | Perception weight multiplier for targets in the secondary cone (0-1). |
| `SuspiciousThreshold` | AlertnessLevel threshold to transition from Idle to Suspicious. |
| `TakingFireDecayTime` | How long TakingFire stays true after the last hit before decaying (seconds). |
| `ThreatEstimateDistance` | Distance along bullet direction to place synthetic threat position (meters). |
| `VisionMaxDistance` | Maximum visual detection distance in meters. |

## A real one

`Vanilla\Assets\System\AI\PerceptionProfileDefinition.def`

```json
{
  "Guid": "eef3712d-27f4-4422-8fdd-fda61122c53e",
  "VisionMaxDistance": 60,
  "PrimaryFOVDegrees": 90,
  "SecondaryFOVDegrees": 180,
  "SecondaryFOVWeight": 0.3,
  "BaseVisualPerceptionRate": 1,
  "MaxRaycastsPerTick": 2,
  "RaycastInterval": 0.3,
  "MaxObscuredTime": 2,
  "HearingMaxDistance": 100,
  "AudioSensitivity": 1,
  "AudioThreatDuration": 15,
  "FlinchDuration": 1.5,
  "FlinchCooldown": 6,
  "FlinchMinIntensity": 0.15,
  "FlinchMaxAlertness": "Suspicious",
  "MinSoundOcclusionDistance": 4,
  "SoundOcclusionPenaltyPerSurface": 8,
  "MaxSoundOcclusionSurfaces": 8,
  "MaxSoundOcclusionRaycastsPerTick": 4,
  "SoundOcclusionFilter": "bc152ea4-584c-4290-87ce-2c083fe8f98a",
  "ProximityRadius": 5,
  "SuspiciousThreshold": 0.3,
  "SuspiciousFallThreshold": 0.2,
  "AlertThreshold": 0.7,
  "AlertFallThreshold": 0.6,
  "AlertDecayRate": 0.1,
  "CautiousDecayRate": 0.05,
  "SuspiciousDecayRate": 0.05,
  "AlertDecayDelay": 5,
  "CautiousDecayDelay": 7.5,
  "SuspiciousDecayDelay": 3,
  "TakingFireDecayTime": 5,
  "ThreatEstimateDistance": 25,
  "MemoryRetentionTime": 30,
  "MemoryUncertaintyGrowthRate": 2,
  "PartialToFullThreshold": 0.6,
  "PerceptionDecayRate": 0.2,
  "BodyHeightFraction": 0.5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PerceptionProfileDefinitionObjectBuilder')
search_content('', type_contains='PerceptionProfileDefinitionObjectBuilder')
```
