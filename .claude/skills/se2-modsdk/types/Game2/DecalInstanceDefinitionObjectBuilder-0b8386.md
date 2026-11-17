# DecalInstanceDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Decals.DecalInstanceDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Decals`
- definitions using it: **10**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\UI3D\VoxelHand\Axis\VoxelHandDecal.def`

```json
{
  "Guid": "606af65c-133b-4c43-b5c4-acf3db71e73c",
  "Size": {
    "X": 5,
    "Y": 5,
    "Z": 5
  },
  "Decal": "58646778-6cb4-4b4f-80ad-6e46009767e0",
  "Flags": "Voxels",
  "Budget": "a1320f3e-6849-4382-8a7b-46e4f40682bd"
}
```

Others: `DecalMaterial_ProjectileVoxelHit`, `Decal_ProjectileHit_Voxel_Rock`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalInstanceDefinitionObjectBuilder')
search_content('', type_contains='DecalInstanceDefinitionObjectBuilder')
```
