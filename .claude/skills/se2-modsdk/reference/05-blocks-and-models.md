# Blocks, models and surfacing

## Do not author a block by hand

One block is roughly **14 definitions** — placement, model, breakable, recipe,
client/server prefab and composition, effects, icon. `IonThruster500` is exactly
14. The editor's template menus generate the whole consistent set at once:

```
editor_explorer()                        select the target folder first
editor_generators(contains='Thruster')   ~330 menu entries; filter
editor_create_from_template('Blocks/Breakable/Ion Thrusters')
```

Then `read_definition` the generated files and `write_definition` to override
only the values you actually want to change.

To learn a block's structure before designing anything:
`subject_files(subject='IonThruster500')` returns every file belonging to it.

## Size is encoded in the name

**A block's name carries its largest dimension in centimetres.** A model that
overflows its declared size places incorrectly in game.

| block | measured bounds |
|---|---|
| IonThruster150 | 1.508 × 1.016 × 1.514 m |
| IonThruster500 | 5.006 × 2.511 × 2.514 m |

## Polygon budget

| block | LOD0 vertices |
|---|---|
| IonThruster150 | 8,459 |
| IonThruster500 | 17,859 |

A few thousand triangles reads as under-detailed next to vanilla.

## Form language

Hard-edged boxes plus open-ended cylinders. No lathed or soft surfaces. Detail
lives on the surface: raised panels, conduits, vents, roughly 2 cm chamfers.
Keep the silhouette to three masses.

## Surfacing: do not paint LOD0 textures

Vanilla blocks carry **no per-block LOD0 textures**. They reference a shared
material library — `PaintedMetalColorable`, `MetalDull`, `Chrome`, `Rubber`, the
`AtlasDecal_*` set — and only the furthest LOD uses a baked per-block atlas in a
`LODMaterial/` folder (`_albedo`, `_ao`, `_colormask`, `_metal`, `_normal`,
`_roughness`).

Painting a bespoke LOD0 texture makes a block look *wrong* next to vanilla, not
better: the shared materials carry the colourable paint mask the game recolours.

```
blender_material_library()     appends the shared set from
                               <SDK>/BlenderMaterialLibrary/SE2Decal&Material.zip
```

The reliable shortcut: import a vanilla FBX into Blender, and its materials come
with it. Assign those same material objects to your mesh and the names are
guaranteed to match.

## Export

Keen ships an official Blender add-on, `vrage_tools`, whose 27 operators produce
exactly the FBX/LOD/collision layout the pipeline expects. Nothing else does.

```
blender_status()                          VRAGE Tools must be enabled
blender_measure(subject='MyThruster250')  checks the model against its declared size
blender_export_model(name='MyThruster250',
                     models_dir='<mod>/Assets/MyThruster250/Models',
                     variant='NON_FRACTURED', lods=[0,1,2,3], collisions=True)
```

`models_dir` is the **parent** of the variant folder. The operator writes
`Models/NonFractured/<Name>.fbx`, `_LOD1..3.fbx` and `<Name>_collision.gltf`
plus `.bin`, matching Keen's `ExampleMod1` exactly. Repeat with
`variant='DEFORMED'` and `'FRACTURED'` for a breakable block.

Two measured behaviours:

- `bpy.ops.scene.vrt_quick_export()` called from a script runs `execute()`
  directly, so the confirmation dialog never appears — that is what makes VRAGE
  Tools scriptable at all.
- `limit='SELECTED_OBJECTS'` with an empty selection exports **nothing and
  reports success**. Always check the files that actually landed on disk, or
  pass `limit='VISIBLE_OBJECTS'`.

## Armor blocks

Armor is its own path:

1. Model to a 25 × 25 × 25 cm bounding box with a planar mating face.
2. Export into the mod's Assets folder.
3. In the editor: right-click the FBX → Create Asset → Armors → ArmorSide, name
   it with the `_250` suffix, **set Scale to 10**.
4. Then Create Prefab → Armors → Armor Block.

Scale 10 is not optional — the ArmorSide asset is authored in decimetres.

## Sound

FMOD Studio **2.02.x only**; newer versions are incompatible.

1. Assets → Create Asset → FMOD Project in the editor.
2. Block sounds: 3D Timeline event, max distance 5–20 m for idles. Music: 2D
   Timeline event under `Music/<Category>`, routed to the Music Group in the
   mixer.
3. In FMOD: Scripts → VRage → Save project to VRage Editor.
4. Assign it on the block's `BlockEffectsComponentDefinition`, field
   `OnUseAudio`: an FMOD event path such as `event:/SFX/Block/LightSmall`, not
   a GUID (every vanilla value sampled on 4.0.0.3169). The block's state picks the
   sound inside that event through audio parameters. Copy a shared vanilla
   component rather than overriding it, or every block using it changes.

The editor label "On Activation Audio" is the field `OnActivationAudio`, which
exists only on the thrust-effects components (`GridThrustEffectsComponentDefinition`,
`ThrustEffectsComponentDefinition`: ship and jetpack thrust), not on a block.

Added music joins the vanilla pool rather than replacing it.
