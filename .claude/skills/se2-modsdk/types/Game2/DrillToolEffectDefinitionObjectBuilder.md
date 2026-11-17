# DrillToolEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.Effects.DrillToolEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools.Effects`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmountMultiplier` | Defines the relative amount of debris that will be created and scattered around the mining area in a single request when a voxel mining operation occurs. 1 means default amount. |
| `DecalPlacementDistance` | Distance of sphere cast to determine decal position |
| `DecalPlacementOffset` | Origin from where sphere cast will be performed to find out decal position |
| `DecalPlacementRadius` | Radius of sphere cast to determine decal position |
| `DecalSpawnInterval` | Interval over which the decal placement is checked |
| `DefaultDebris` | Configures debris spawned while drilling. |
| `DrillContactAnimationEvent` | Name of animation event when the drill is meant to be in contact with the object. If set, drilling effects are only spawned for the duration specified in after the event is triggered. |
| `DrillContactEffectDuration` | Duration for which the effects should play when is triggered. |
| `DrillDecal` | Decal to be placed by the drill |
| `DrillEndAudioParameter` | Parameter to use to indicate audio ending when drilling stops |
| `DrillEndAudioParameterValue` | Value to send to to indicate audio ending when drilling stops |
| `DrillEntityGroundType` | Value to send to on instance when drilling and damaging entities like grids and other characters |
| `DrillNothingGroundType` | Value to send to on instance when drilling nothing |
| `DrillStartAudioParameterValue` | Value to send to to indicate audio starting when drilling starts |
| `DrillVoxelGroundType` | Value to send to on instance when drilling voxels |
| `FirstPersonDecalPlacementDistance` | Only applicable for hand tools, when first person mode is enabled. In that case the decal cast will be performed from the camera and will have this distance |
| `GridDrillPhysicsMaterial` | Physics material group used with when drilling a grid. |
| `NothingDrillPhysicsMaterial` | Physics material group used with when drilling nothing. |
| `OnActivationParticleEffect` | Particle Effect to spawn when the drill is activated |
| `OnDrillAudio` | Audio event to play when drilling. looped sound |
| `OnMineVoxelAudio` | Audio event to play when mining voxel occurs. one shot sound |
| `OnUseOnEntitiesParticleEffect` | Particle Effect to spawn when damaging entities |
| `OnUseOnVoxelsParticleEffect` | Particle Effects to spawn when drilling voxels |
| `OnVoxelMinedEffectScale` | Defines the scale of the of the effect |
| `OnVoxelMinedParticleEffect` | Particle Effects to spawn when a voxel is mined |
| `PerMaterialDebris` | Configures debris for specific voxel materials spawned while drilling. |
| `PerMaterialDrillAudio` | Configures drill audio for specific physics material groups. Will default to if material group is not specified. |
| `StopAudioDebounceTime` | Artificial delay to stop and debounce successive audio launches and voxel mining |
| `VoxelDebrisSpawnRadius` | Defines the radius of spawn area within which voxel debris will be spawned and distributed randomly. Spawn area is a hemisphere facing the opposite direction of the voxel brush's forward vector with the center at the voxel brush's position. |
| `VoxelLayer` | Layer of voxels. Will be used to check where to place decal to |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DrillBlock_DrillToolEffectDefinition.def`

Too large to inline. Fields present:

`AmountMultiplier`, `DefaultDebris`, `DrillContactAnimationEvent`, `DrillContactEffectDuration`, `DrillEndAudioParameter`, `DrillEndAudioParameterValue`, `DrillEntityGroundType`, `DrillNothingGroundType`, `DrillStartAudioParameterValue`, `DrillVoxelGroundType`, `GridDrillPhysicsMaterial`, `Guid`, `NothingDrillPhysicsMaterial`, `OnActivationParticleEffect`, `OnDrillAudio`, `OnMineVoxelAudio`, `OnUseOnEntitiesParticleEffect`, `OnUseOnVoxelsParticleEffect`, `OnVoxelMinedEffectScale`, `OnVoxelMinedParticleEffect`, `PerMaterialDebris`, `PerMaterialDrillAudio`, `StopAudioDebounceTime`, `VoxelDebrisSpawnRadius`

Others: `HandDrill_Client_DrillToolEffectDefinition`, `DrillTool_DrillToolEffectDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillToolEffectDefinitionObjectBuilder')
search_content('', type_contains='DrillToolEffectDefinitionObjectBuilder')
```
