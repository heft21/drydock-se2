# FloraConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.Flora.FloraConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions.Flora`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AsymmetricDestructionDefinition` | When set applies asymmetric destructions to flora items. |
| `DefaultSafeSpeedOverride` | Override the global safe speed value for flora items. Use this in conjunction with to make flora items stronger or weaker than other entities. |
| `DestroyedFloraItemLifetime` | How long until a partially destroyed flora item stays spawned before being collected by trash collector |
| `FractureLinearImpulse` | Impulse to apply to flora fractures in the damage direction when spawned |
| `MaxSectorDistance` | Sectors further away than this value from are not created and eagerly unloaded |
| `MaxUpdateMovementDistance` | If moves more than this distance every 10 ticks, flora will not be updated for render |
| `MaximumClusterSpawnDepth` | Defines the maximum recursive depth when spawning clusters to prevent infinite recursions due to bad data setup |
| `MaximumItemBodyCount` | Defines the FloraItem body pool size. This pool is used by flora items close by to the physics enabled client avatar |
| `MaximumItemBodyDistance` | Defines the maximum distance from the client avatar at which bodies are used for spawned flora items |
| `MinimumInstanceBreakPhysicsImpulse` | Minimum impulse to transition from an item instance to a prefab |
| `ObserverTag` | Tag associated to the observable entity whose transform we should use as vantage point for this system (e.g. camera) |
| `PenetrationProportionToDamage` | Proportional damage to deal for penetration. This means that if penetration is equal to "PenetrationToDamage", the full flora health is dealt as damage. Damage is calculated as `blockHealth * (penetration / penetrationProportionToDamage)` |
| `SectorPhysicsPrefab` | Prefab spawned to handle non entity flora item collision and destruction |
| `TolerableImpulseFallback` | A value to fallback in case tolerable impulse for flora item couldn't be found. |
| `ToleranceToValueTable` | A table of conversion values for specific collision tolerance to integer value of tolerable impulse. |

## A real one

`Vanilla\Assets\System\Configurations\FloraConfiguration.def`

```json
{
  "Guid": "8b6cc7e2-5f14-4f6b-81f1-2026ba4385a3",
  "MaximumItemBodyCount": 256,
  "MaximumItemBodyDistance": 100,
  "MaximumClusterSpawnDepth": 2,
  "DestroyedFloraItemLifetime": 100000000,
  "MinimumInstanceBreakPhysicsImpulse": 2000,
  "SectorPhysicsPrefab": "7b7382b3-22f5-437d-bfaf-62750bd9ed06",
  "MaxSectorDistance": 2000,
  "MaxUpdateMovementDistance": 56,
  "ObserverTag": "VoxelObserver",
  "AsymmetricDestructionDefinition": "2bb3ea5a-f7fe-4118-8714-366a7ebf17e7",
  "DefaultSafeSpeedOverride": 0,
  "PenetrationProportionToDamage": 0.3,
  "TolerableImpulseFallback": 500,
  "ToleranceToValueTable": {
    "WeakTree": 7500,
    "StrongTree": 30000,
    "SmallRock": 15000,
    "LargeRock": 45000
  },
  "FractureLinearImpulse": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraConfigurationObjectBuilder')
search_content('', type_contains='FloraConfigurationObjectBuilder')
```
