# WaterSessionDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.WaterSessionDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **2**

## What it is

Generated object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CanCreateGrids` | Session can create domains and grids |
| `CanUpdateSolids` | Session and its water grids can update solids from collisions |
| `DebugForbidWatergridCollisions` | Whether this water session should check that no watergrids are overlapping |
| `DebugForbidWatergridCreations` | Whether this water session is forbidden from creating water grids (in which case all watergrids will be from replication) |
| `DebugForbidWatergridRemovals` | Whether this water session is forbidden from removing water grids, similar to |
| `DefaultPlanetaryWaterProfile` | which water visual profile is used on the planets if no were defined |
| `DynamicWaterDomainPrefab` | The prefab for the water domain |
| `GravityProxyPrefab` | The prefab for the gravity proxy |
| `SpaceWaterProfile` | which water visual profile is used for water in space |
| `WaterDomainPrefab` | The prefab for the water domain |
| `WaterRegionPrefab` | The prefab for the water region |

## A real one

`Vanilla\Assets\System\Water\ClientWaterSessionDefinition.def`

```json
{
  "Guid": "ade20776-5f2d-4f9b-9bf4-598c4fa0fc17",
  "WaterDomainPrefab": "3339a14c-ba42-4d0a-9aa4-63e5a9af2371",
  "DynamicWaterDomainPrefab": "4eb3e236-8364-4496-9d32-0c9d3117834b",
  "GravityProxyPrefab": "66cd0ebc-4d32-40fc-8555-c329f85bd8e5",
  "WaterRegionPrefab": "61b387ba-cf8d-493a-8697-ed3314f1a390",
  "SpaceWaterProfile": "33bec425-f3f2-42ba-bc2d-9def6427d41d",
  "DefaultPlanetaryWaterProfile": "f3758eee-d286-494d-9f43-f8cc1ba1af8f",
  "DebugForbidWatergridCollisions": false,
  "DebugForbidWatergridCreations": true,
  "DebugForbidWatergridRemovals": true,
  "CanUpdateSolids": false,
  "CanCreateGrids": false,
  "DebugParticleEffect": "2f633b0c-b381-48fb-81e9-9fd73b7c2aa3",
  "DefaultGPUParticleEffect": "6d2fa91b-39cf-4be2-a12c-3924d08f7551"
}
```

Others: `ServerWaterSessionDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterSessionDefinitionObjectBuilder')
search_content('', type_contains='WaterSessionDefinitionObjectBuilder')
```
