# BoneDeformationConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Armor.Definitions.BoneDeformationConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Armor.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoneCellDistance` | Distance between the two neighboring bones in the bone grid. Distance is expressed in multiples of the grid cells. |
| `MaxBlockDeformationRatio` | Limits how much can block be deformed, depending on block size. - Limit of 1 means 1m big armor block can be displaced at most 1m. - Limit of 2 means 1m block can be displaced at most 2 meters in each direction, but 0.25m block can be displaced 0.5m. |
| `MaxBoneOffset` | The maximum displacement per axis for deformed vertices. |

## A real one

`Engine\Assets\Configurations\BoneDeformationConfiguration.def`

```json
{
  "Guid": "40ef6aba-0ba8-47f3-a89f-c4d018fc029a",
  "BoneCellDistance": 4,
  "MaxBoneOffset": 0.85,
  "MaxBlockDeformationRatio": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BoneDeformationConfigurationObjectBuilder')
search_content('', type_contains='BoneDeformationConfigurationObjectBuilder')
```
