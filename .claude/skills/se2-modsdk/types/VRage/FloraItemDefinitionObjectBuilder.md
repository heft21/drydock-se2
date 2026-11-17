# FloraItemDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.Flora.FloraItemDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions.Flora`
- definitions using it: **289**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BottomCollider` | Collider data used for overlap avoidance at ground level |
| `Cluster` | Initialized in order to generate a cluster of flora items instead of a single one. Contains all required information for creating such a cluster. |
| `CollisionTolerance` | Represents a collision tolerance archetype that will be used for this entity. Configurable in |
| `Density` | How many items to spawn in count per kilometer squared |
| `FracturesCanBecomeStatic` | If true, fractures intersecting with a planet will be physically static. Disable to force fractures to always respond dynamically to physics. |
| `HasCollider` | If false, this flora item can only be destroyed by voxel changes, but does not block walking. Useful for smaller items like bushes |
| `HeightPlacementRule` | The percentage height at which the item can be placed. |
| `HueVariance` | Hue variation amplitude |
| `ItemPrefab` | Prefab to spawn when the flora item is destroyed |
| `LuminosityVariance` | Luminosity variation amplitude |
| `Mass` | Mass of the entire flora item |
| `MaximumCollisionDamage` | Maximum damage from a collision TODO: https://marekrosa.atlassian.net/browse/SE2-26995 |
| `MaximumDamagePhysicsImpulse` | Maximum impulse on prefab collision for maximum damage TODO: https://marekrosa.atlassian.net/browse/SE2-26995 Strange bug when remove migration on these. Needs investigation. |
| `PreciseSlopeHeightRange` | Only works if UsePreciseSlopeRange is true. The percentage range of the detected slope height the item will be allowed to spawn in. |
| `ScaleRule` | The percentage scale that the flora item can be sized to. |
| `SlopePlacementRule` | Slope angle at which the item can be placed. |
| `TolerableImpulse` | Impulse the flora item can tolerate before taking damage. TODO: This should be kept after ticket below is fixed - but as a [NoSerialize] field. TODO: https://marekrosa.atlassian.net/browse/SE2-26995 |
| `TopCollider` | Collider data used for overlap avoidance above ground level (e.g. treetops) |
| `UsePreciseSlopeRange` | If this is set the positioning of the item will consider the surrounding area and determine where on the slope is the item allowed to spawn. |
| `UseWideSlope` | If this is set the is checked against a large area instead of a single point. |
| `WindAnimationDefinition` | Wind animation to associate with this flora item |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Placeholders\Planet\FloraItemDefinition.def`

```json
{
  "Guid": "af567a2c-fc3e-4335-8f3b-783b4efec989",
  "ItemPrefab": "3292b88f-4f2f-47a7-be2e-2bd9186709ba",
  "Mass": 150,
  "MaximumDamagePhysicsImpulse": 10000,
  "MaximumCollisionDamage": 100,
  "TolerableImpulse": 500,
  "CollisionTolerance": "WeakTree",
  "HasCollider": true,
  "FracturesCanBecomeStatic": true,
  "Density": {
    "Unit": "SquareKilometer",
    "ValuePerUnit": 300
  },
  "SupportedVoxelMaterials": [],
  "SlopePlacementRule": {
    "Min": 0,
    "Max": 90
  },
  "UseWideSlope": false,
  "UsePreciseSlopeRange": false,
  "PreciseSlopeHeightRange": {
    "Min": 0,
    "Max": 1
  },
  "HeightPlacementRule": {
    "Min": 0,
    "Max": 1
  },
  "ScaleRule": {
    "Min": 0.8,
    "Max": 1.2
  },
  "FollowTerrainInclination": 0,
  "BottomCollider": {
    "Height": 1,
    "Radius": 0.5,
    "HeightOffset": 0
  },
  "TopCollider": {
    "Height": 4,
    "Radius": 4,
    "HeightOffset": 2
  },
  "Cluster": null,
  "HueVariance": 0,
  "LuminosityVariance": 0,
  "WindAnimationDefinition": null
}
```

Others: `FloraSpawn_LargeBirchHero_VS2-3`, `VerdureSpawn_Flora_SmallStachys01`

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraItemDefinitionObjectBuilder')
search_content('', type_contains='FloraItemDefinitionObjectBuilder')
```
