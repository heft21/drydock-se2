# VoxelConfiguratorConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.ConfiguratorComponents.VoxelConfiguratorConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.ConfiguratorComponents`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EnvironmentItemSizeEstimator` | A prefab containing configurators for estimating the sizes of all available environment items. These estimates are crucial for avoiding overlapping spawns by determining the space required for each item upfront. |
| `PlanetPreviewConfigurator` | A prefab containing configurators for processing planet-specific components for preview purposes. Ensures that all relevant components are updated correctly when overriding the planet's object builder values. |

## A real one

`Engine\Assets\Configurations\VoxelConfiguratorConfiguration.def`

```json
{
  "Guid": "79ae2a50-7c95-4153-a3f6-3a38afa4cd9f",
  "EnvironmentItemSizeEstimator": null,
  "PlanetPreviewConfigurator": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelConfiguratorConfigurationObjectBuilder')
search_content('', type_contains='VoxelConfiguratorConfigurationObjectBuilder')
```
