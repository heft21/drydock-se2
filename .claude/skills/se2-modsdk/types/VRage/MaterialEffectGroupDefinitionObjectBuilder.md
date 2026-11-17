# MaterialEffectGroupDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Definitions.MaterialEffectGroupDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Definitions`
- definitions using it: **24**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Category` | Group category to use for FMOD parameters. |
| `Name` | Group name to use for FMOD parameters. |
| `PhysicsMaterials` | List of materials belonging to the same effect group. |

## A real one

`Vanilla\Assets\Environment\System\VoxelDefaultMaterialGroup.def`

```json
{
  "Guid": "44ac27b1-7c39-4a2b-bc71-6a31b80db2c1",
  "Name": "VoxelDefaultMaterialGroup",
  "Category": "Voxel",
  "PhysicsMaterials": [
    {
      "Key": "de80e123-7fa3-4cde-97da-6f741d1eb126",
      "Value": "6dadf3ac-aa96-4b1b-a4c5-891633a0b48a"
    },
    {
      "Key": "c790426c-0ecb-4108-a7d7-5268d44c8a3d",
      "Value": "29408c69-b360-48a5-ad06-fc04fe9717f9"
    }
  ]
}
```

Others: `IceMaterialGroup`, `GridMaterialGroup`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialEffectGroupDefinitionObjectBuilder')
search_content('', type_contains='MaterialEffectGroupDefinitionObjectBuilder')
```
