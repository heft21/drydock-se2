# Voxel materials and ores

## The chain from a PNG to an ore

Verified against a working mod:

```
VoxelMaterialDefinition             identity: Name, PhysicsMaterial — holds NO textures
  ↑ VoxelMaterial
VoxelRenderMaterialDefinition       binds VoxelMaterial → RenderMaterial + Icon
  ↑ RenderMaterial
TriplanarSingleMaterialDefinition   the actual textures
  ├─ ColorMetal{XZ,Y}{Near,Far1,Far2}       ← *_cm.comptex
  ├─ NormalRoughness{XZ,Y}{Near,Far1,Far2}  ← *_nr.comptex
  ├─ Extensions{XZ,Y}{Near,Far1,Far2}       ← *_add.comptex
  ├─ Displacement{XZ,Y}{Near,Far1,Far2}     ← *_displacement.comptex
  └─ ColorFar3                              a single packed colour for the farthest LOD
       ↑ each .comptex packs source PNGs
PNG sources: Albedo, AO, Height, Normal, Roughness, (Metalness)
             at three levels: _Y_Near, _Y_Far1, _Y_Far2
```

So "replace an ore's texture" means: author the PNGs, let the `.comptex` recipes
pack them, and point a `TriplanarSingleMaterialDefinition` at the results. The
`VoxelMaterialDefinition` itself holds no textures at all.

Textures are named `<Name>_<Axis>_<Distance>_<Type>`, e.g.
`IceAsteroid_Y_Near_Albedo`. Distances are `Near` / `Far1` / `Far2`, and every
file in the set must share one format.

## Where a material spawns

Two completely separate systems, and the distinction decides which file you edit.

### Asteroids — the voxel generator

A mod overrides the vanilla `VoxelGeneratorDefinition` with a partialdef:

```json
"PartialDefinitionKind": "Override",
"DefinitionType": "VRage:Keen.VRage.Voxels.Definitions.VoxelGeneratorDefinition",
"Manipulator": {
  "Settings": { "DepositsCountCoefficient": 1, "DepositSizeDenominator": 12 },
  "DepositMaterials": {
    "$DeltaEncoded": true,
    "Keys": [ … ],
    "Changed": [
      { "Kind": "Insert", "Index": 0,
        "Value": { "Material": "<VoxelMaterial guid>",
                   "AsteroidGeneratorSpawnProbabilityMultiplier": 7 } }
    ],
    "Removed": [ … ]
  }
}
```

The vanilla target is `CombinedGenerator2.def`.

### Planets — the biome

Planet ores come from `PlanetBiomeDefinition.OreRules[].Ore.Material` — again a
`VoxelMaterial` GUID, with `MinSize`, `MaxSize`, `MinBiomeDepth`,
`MaxBiomeDepth` and a `Probability`, plus `OresPerCubicKilometer` on the biome.

So changing a planet's ore means finding the VoxelMaterials named in that
planet's biome definitions — **not** touching the asteroid generator.

`UndergroundBiomes` carry no ColorKey and cannot be painted; vanilla puts only
Nickel, Iron and InnerCore in them. Rare ore is placed through surface biomes,
which is why the biome map can steer it geographically.

## Before changing anything

```
find_references('<VoxelMaterialDefinition guid>')
```

That lists every generator, biome and placement rule that spawns it. A material
used by four planets and the asteroid generator is not a safe thing to retexture
casually.

## Building one

1. `search_content('VoxelMaterial')` and read one vanilla pair.
2. Author `VoxelMaterialDefinition` + `VoxelRenderMaterialDefinition`.
3. Author the PNG set and the `.comptex` recipes; point a
   `TriplanarSingleMaterialDefinition` at them.
4. To change where it spawns, write an `Override` partialdef on the generator
   (asteroids) or edit the biome's `OreRules` (planets).
5. `audit_project`, then `editor_validation`.

Remember the definition-set trap: an `Assets.meta` without a `DefinitionSetItem`
means the game mounts none of this and reports nothing.
