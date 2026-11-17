"""Procedures for building SE2 content, as data the server can hand back.

An agent handed forty tools still has to guess the order to call them in, and
the expensive mistakes in SE2 modding are all ordering and convention mistakes
rather than API mistakes. Everything here was measured on this install — the
figures come from reading vanilla files, importing vanilla FBXs and running the
editor, not from documentation.

Each recipe is a list of steps naming the exact tool to call, plus the traps
that are invisible until they have already cost an afternoon.
"""

from __future__ import annotations

from typing import Any

# The single most destructive mistake, so it leads every relevant recipe.
_DEFINITION_SET_TRAP = (
    "Assets.meta must contain a DefinitionSetItem naming a definition set the "
    "project mounts (normally 'World'). With an empty InternalItems the project "
    "still builds, the editor still validates clean, and the game loads nothing "
    "at all — there is no error anywhere. audit_project checks this."
)

_VANILLA_TRAP = (
    "validate_project / build_project cannot load any project that depends on "
    "Vanilla, and every real mod does: the SDK ships ~384 orphaned '.meta' files "
    "and the CLI has no stripped mode. Use audit_project for offline checks and "
    "editor_validation / editor_build for the authoritative ones."
)

_PROCESSING_TRAP = (
    "editor_build (GenerateCacheAndDefinitionSet) rebuilds the caches and the "
    "definition set — it does NOT re-run the per-asset processors. Assets are "
    "processed when the project is LOADED. After editing a definition by hand, "
    "restart the editor on the project, or the compiled copy in Content/ keeps "
    "the old values while Assets/ shows the new ones."
)

_REFRESH_META_TRAP = (
    "refresh_meta writes the new hash into both the source record and the "
    "processing record, which tells the pipeline the output is already current. "
    "If the file was edited by hand and Content/ still holds the old output, the "
    "edit will be skipped. Either leave the '.meta' stale until after the next "
    "project load, or delete the matching file under Content/."
)


_GSCREEN_TRAP = (
    "A block template makes the block buildable but NOT visible on its own "
    "tile: BlockKind, BlockGroup and the recipe are not created by the "
    "template, and the copied block inherits the vanilla kind. Worse, a kind "
    "with an empty Blocks list is filtered out of the G screen with no log "
    "line at all - GScreen.BlockGroupTileModel keeps only kinds with "
    "Blocks.Length > 0, and BlockKindDefinition.Blocks is computed at load from "
    "the server composites whose CubeBlockDefinition.BlockKind points at the "
    "kind. So: author kind + group + recipe, set BlockKind on the block "
    "definition, make sure the prefab and both compositions are in Content "
    "before building, then read the kind back and confirm Blocks > 0. "
    "'No invalid assets' proves nothing about the menu. See explain('g-screen')."
)

_TAGSLOT_TRAP = (
    "After swapping components inside a copied composition, check TagSlots. "
    "Every slot maps an interface name to a component key; the allocator "
    "assigns that component to the field and a type mismatch throws at spawn. "
    "The game then reports 'Assertion Failure: Dead block in add' plus a "
    "NullReferenceException inside the grid, hiding the real line one second "
    "earlier: 'EntityBundleInitException ... ---> ArgumentException: Object of "
    "type X cannot be converted to type Y'. Copy the template's tag block "
    "verbatim, keep only keys that exist in that composition, and diff the "
    "server and client compositions separately - they fail independently. "
    "See explain('composition-tags')."
)

_COMPOSITION_PARTS_TRAP = (
    "Adding or removing a component in a composition is a two-file edit: the "
    "composition's Keys list AND the prefab's _entity.ObjectBuilders list are "
    "the same parts in the same order. Grow the composition (Keys + Insert at "
    "Index=len-1 with {Definition, Type}) and the prefab (Keys + Insert at the "
    "same index with Value null) in one script. Otherwise the editor reports "
    "'Mismatch in Entity parts OBs:13 IDs:15 ...' or 'ObjectBuilder "
    "...IntegrityToolObjectBuilder type doesn't match expected "
    "...BlockPermissionsObjectBuilder' - both are index errors, not definition "
    "errors. See explain('composition-tags')."
)

_CONTENT_COPY_TRAP = (
    "Content/*.def are compiled build outputs, not source assets. Copying one "
    "into Assets/ and loading the project can crash VRage.Editor outright, with "
    "no dialog and no recoverable state. Read Content files for values, but "
    "author the definition yourself (or copy from GameData/Vanilla/Assets "
    "templates). Related: a $DeltaEncoded list inside a partialdef Manipulator "
    "must carry the base's Keys array - 'Keys: []' plus an Update at index 2 "
    "raises 'Index was out of range' during load. See "
    "explain('composition-tags')."
)


RECIPES: dict[str, dict[str, Any]] = {

    "block": {
        "goal": "A new buildable block (thruster, battery, armor piece...).",
        "why_not_by_hand": (
            "One block is ~14 definitions — placement, model, breakable, "
            "recipe, client/server prefab and composition, effects, icon. "
            "IonThruster500 is exactly 14. Authoring that set by hand is a "
            "mistake; a template generates all of it consistently."
        ),
        "steps": [
            "subject_files(subject='IonThruster500') — see the full file set of a "
            "block that already works, before designing anything.",
            "blender_status() — confirm VRAGE Tools is enabled.",
            "blender_material_library() — append the shared SE2 materials. Do not "
            "paint LOD0 textures; vanilla blocks do not have any.",
            "blender_measure(subject='<Block><size>') — the number in the name is "
            "the largest dimension in centimetres; the model must fit it.",
            "blender_export_model(name, models_dir='<mod>/Assets/<Block>/Models', "
            "lods=[0,1,2,3], collisions=True).",
            "launch_editor(project) then editor_generators(contains='Thruster') — "
            "find the template menu path.",
            "editor_create_from_template('Blocks/Breakable/Ion Thrusters') — "
            "generates all definitions at once in the folder the Project Explorer "
            "is showing, so select that folder first with editor_explorer.",
            "read_definition on the generated files, then write_definition to "
            "override the values you actually want to change.",
            "Give the block its own identity: author a BlockKindDefinition "
            "(Name + Description loc keys, BlockGroups -> the group), a "
            "BlockGroupDefinition (Name loc key, Subcategories -> the vanilla "
            "subcategory guid, normally Tools/Construction 57d383fb-...), and a "
            "CubeBlockRecipeDefinition. Then point the block definition at them "
            "by adding BlockKind and Recipe to its manipulator.",
            "Add the localisation keys (explain('localization')) or reuse "
            "existing vanilla keys while testing - an unknown key fails "
            "validation.",
            "Restart the editor so the prefab and both compositions are "
            "processed, then editor_build(). A definition set generated before "
            "the prefab exists links the kind to zero blocks.",
            "Verify the menu link, not just validation: read the kind definition "
            "and check Blocks > 0 and BlockGroups == 1, and the group's "
            "Subcategories == 1. Then read both compositions and check every "
            "TagSlots target against the interface it satisfies.",
            "Blocks that consume items (welders, assemblers, BaR-style tools) need "
            "ItemRequesterComponent + InventoryStockpileComponent in the server "
            "composition or they only use their own inventory. Add both, with the "
            "SAME keys in the prefab, plus the five tag slots. "
            "See explain('inventory-logistics').",
            "audit_project(project) then editor_validation().",
        ],
        "measured": {
            "size_rule": "Block name number = largest dimension in cm. "
                         "IonThruster150 = 1.508 x 1.016 x 1.514 m; "
                         "IonThruster500 = 5.006 x 2.511 x 2.514 m.",
            "poly_budget": "IonThruster150 LOD0 = 8,459 verts; "
                           "IonThruster500 LOD0 = 17,859. A few thousand "
                           "triangles reads as under-detailed next to vanilla.",
            "materials": "LOD0-3 use the shared library "
                         "(PaintedMetalColorable, MetalDull, Chrome, Rubber, "
                         "AtlasDecal_*). Only the last LOD uses a baked "
                         "per-block atlas in LODMaterial/.",
            "form_language": "Hard-edged boxes plus open-ended cylinders. No "
                             "lathed or soft surfaces. Detail lives on the "
                             "surface: raised panels, conduits, vents, ~2 cm "
                             "chamfers. Keep the silhouette to three masses.",
        },
        "traps": [_DEFINITION_SET_TRAP, _VANILLA_TRAP, _PROCESSING_TRAP,
                  _GSCREEN_TRAP, _TAGSLOT_TRAP, _COMPOSITION_PARTS_TRAP,
                  _CONTENT_COPY_TRAP],
    },

    "planet": {
        "goal": "A new planet, spawnable from the debug menu.",
        "required_definitions": [
            "PlanetGeneratorDefinition — heightmap cubemap + the six face PNGs, "
            "DefaultMaterial, HillParams, MaxAltimeter, Version.",
            "BiomeMapDefinition + PlanetBiomeMapDefinition — biome cubemap and "
            "the material map it pairs with.",
            "MaterialMapDefinition + one PlanetMaterialMapDefinition per surface "
            "material, keyed by ColorKey.",
            "AtmosphereDefinition + PlanetEnvironmentRenderDefinition (which also "
            "names the CloudDefinition).",
            "PlanetOverlayDefinition + the CM/NAO cubemaps built from _cm/_nao "
            "composed textures.",
            "VoxelPlanetRenderComponentDefinition — clipmap, overlay, "
            "spherization.",
            "The prefab set copied from Templates/Planets/PlanetWithAtmosphere: "
            "binding, _Client, _ClientComposition, _Server, _ServerComposition.",
            "PlanetInfoDefinition — WITHOUT THIS THE PLANET IS UNSPAWNABLE. It is "
            "what puts the planet in the debug menu's planet template list. "
            "Name = the label shown, Spawn = the planet's *_Server prefab GUID, "
            "Preview = the shared Vanilla prefab "
            "ab7795e6-b1be-44df-9f05-d002ff859409 (PlanetPreview_Server, used by "
            "every planet from VS2_2 on).",
        ],
        "steps": [
            "search_content('PlanetGenerator') and read the Byblos set under "
            "Assets/Procedural/VS3_0/Planets/Byblos — it is the newest complete "
            "planet and the right thing to copy.",
            "Author the maps: six 8192x8192 16-bit greyscale PNGs per cubemap, "
            "plus a .planetcubemap naming all six by GUID.",
            "write_definition for each definition above.",
            "audit_project(project) — catches unresolved GUIDs and missing "
            "sidecars that the editor will not.",
            "launch_editor + editor_validation + editor_build.",
            "In game: CTRL+F12 -> Gameplay -> Voxel -> pick the planet in the "
            "templates list -> set radius -> Activate planet placer.",
        ],
        "measured": {
            "HillParams": "Terrain relief as a fraction of planet radius; the "
                          "heightmap's 0..65535 maps linearly onto Min..Max. "
                          "Min=Max=0 makes a perfectly smooth sphere and the "
                          "heightmaps do nothing. Vanilla: EarthLike -0.01/0.12, "
                          "Byblos -0.3333/0.03333, Geomeles -0.2/0.2.",
            "MaxAltimeter": "Every vanilla planet sets this equal to "
                            "HillParams.Max. It drives the altimeter readout.",
            "Version": "Any planet made after VS2.0 should reference "
                       "PlanetVersionDefinition_VS2-2 "
                       "(f36276b0-3b93-44b3-9391-38a0cb8f4099).",
            "keys_do_not_resolve": "In MaterialMappings, SurfaceBiomes and "
                                   "MaterialRules the 'Key' GUIDs resolve to "
                                   "nothing — in vanilla too. They are identity "
                                   "keys, not asset references. Only 'Value' "
                                   "must resolve.",
            "shared_prefabs": "PlanetPreview_Server "
                              "ab7795e6-b1be-44df-9f05-d002ff859409 (VS2_2+), "
                              "PlanetPreview_Client "
                              "ea21c45c-178d-4ac6-8445-7cad4c8faa63 (older).",
        },
        "traps": [_DEFINITION_SET_TRAP, _VANILLA_TRAP, _PROCESSING_TRAP,
                  "A planet can validate clean, build clean and still be "
                  "impossible to spawn, because PlanetInfoDefinition is not "
                  "referenced by anything — nothing detects that it is missing."],
    },

    "voxel_material": {
        "goal": "A new ore or surface material.",
        "steps": [
            "search_content('VoxelMaterial') and read one vanilla pair.",
            "Author VoxelMaterialDefinition + VoxelRenderMaterialDefinition.",
            "Textures are named <Name>_<Axis>_<Distance>_<Type>, e.g. "
            "IceAsteroid_Y_Near_Albedo. Distances are Near / Far1 / Far2 and "
            "every file in the set must share one format.",
            "To change where it spawns, write an Override partialdef on "
            "CombinedGenerator2.def.",
            "audit_project then editor_validation.",
        ],
        "traps": [_DEFINITION_SET_TRAP],
    },

    "armor": {
        "goal": "A new armor block.",
        "steps": [
            "Model to a 25x25x25 cm bounding box with a planar mating face.",
            "blender_export_model into the mod's Assets folder.",
            "In the editor: right-click the FBX -> Create Asset -> Armors -> "
            "ArmorSide, name it with the _250 suffix, set Scale to 10.",
            "Then Create Prefab -> Armors -> Armor Block.",
        ],
        "traps": ["Scale 10 is not optional — the ArmorSide asset is authored in "
                  "decimetres."],
    },

    "texture": {
        "goal": "Surfacing, and when to make a texture at all.",
        "measured": {
            "blocks": "Do not author LOD0-3 textures. Vanilla thrusters use only "
                      "shared library materials; the per-block LODMaterial/ "
                      "folder holds a baked atlas for the furthest LOD only "
                      "(_albedo, _ao, _colormask, _metal, _normal, _roughness).",
            "planets": "Overlay faces are composed: a .comptex per face per "
                       "channel group (_cm = colour+metal, _nao = normal+AO), "
                       "then a .cubemap naming the six faces, then "
                       "PlanetOverlayDefinition naming the two cubemaps.",
            "shortcut": "Import a vanilla FBX into Blender; its materials come "
                        "with it. Assign those same material objects to your "
                        "mesh and the names are guaranteed to match.",
        },
        "steps": [
            "blender_material_library() to append the shared set.",
            "blender_python(...) to assign materials by name.",
            "blender_export_model(...).",
        ],
        "traps": ["Painting a bespoke LOD0 texture makes a block look wrong next "
                  "to vanilla, not better — the shared materials carry the "
                  "colourable paint mask the game recolours."],
    },

    "model": {
        "goal": "Getting geometry out of Blender correctly.",
        "steps": [
            "blender_status() — VRAGE Tools must be enabled.",
            "blender_measure(subject='<name><size>') — check the size class.",
            "blender_export_model(name=..., models_dir='<mod>/Assets/<Block>/"
            "Models', variant='NON_FRACTURED', lods=[0,1,2,3], collisions=True).",
            "Repeat with variant='DEFORMED' and 'FRACTURED' for a breakable "
            "block.",
        ],
        "measured": {
            "layout": "models_dir is the PARENT of the variant folder. The "
                      "operator writes Models/NonFractured/<Name>.fbx, "
                      "_LOD1..3.fbx and <Name>_collision.gltf + .bin, matching "
                      "Keen's ExampleMod1 exactly.",
            "no_popup": "bpy.ops.scene.vrt_quick_export() from a script runs "
                        "execute() directly, so the confirmation dialog never "
                        "appears and automation is safe.",
            "empty_selection": "limit='SELECTED_OBJECTS' with nothing selected "
                               "exports nothing and reports success. "
                               "blender_export_model reports the files actually "
                               "written, so check that list.",
        },
    },

    "sound": {
        "goal": "Block sounds and music.",
        "steps": [
            "FMOD Studio 2.02.x only — newer versions are incompatible.",
            "Assets -> Create Asset -> FMOD Project in the editor.",
            "Block sounds: 3D Timeline event, max distance 5-20 m for idles. "
            "Music: 2D Timeline event under Music/<Category>, routed to the "
            "Music Group in the mixer.",
            "In FMOD: Scripts > VRage > Save project to VRage Editor.",
            "Assign it on the block's BlockEffectsComponentDefinition, field "
            "OnUseAudio: an FMOD event path such as 'event:/SFX/Block/LightSmall', "
            "not a GUID (every vanilla value sampled on 4.0.0.3169). Copy a shared "
            "vanilla component rather than overriding it.",
        ],
        "traps": ["Added music joins the vanilla pool rather than replacing it.",
                  "The editor label 'On Activation Audio' is the field "
                  "OnActivationAudio, which exists only on the thrust-effects "
                  "components (ship and jetpack thrust), not on a block's "
                  "BlockEffectsComponentDefinition."],
    },

    "publish": {
        "goal": "Getting a mod onto the Workshop.",
        "steps": [
            "CLOSE Mod HUB and the editor first. Both hold the project in "
            "memory and write their own .vrgproj back over yours, silently "
            "undoing any project-level setting you just made.",
            "If the mod ships a planet, run tools/prepare_publish.py — the "
            ".planetcubemap assets cannot pass Mod HUB's validator without it, "
            "because ModHUB does not load the assembly holding their processor. "
            "See explain('publish-hash').",
            "finish_and_publish(project) — does the first two steps for you: "
            "removes the editor bridge and audits. Read its 'blocking' list; "
            "if it is empty, carry on from the editor_validation step below.",
            "audit_project(project) — must be clean.",
            "uninstall_bridge(project) — the bridge must never ship inside a mod.",
            "launch_editor(project); editor_validation() must report no errors, "
            "because Mod HUB refuses to publish while any Error remains and only "
            "says 'open the project in the editor to see the validation "
            "problems'.",
            "editor_build(with_blobs=True).",
            "Close the editor, then launch_modhub() and press Publish there — "
            "Mod HUB has no publish command line.",
            "If it fails: read_app_log(app='modhub', contains='publish'). "
            "Publishing runs inside the HUB and leaves nothing in the editor log.",
        ],
        "checklist": [
            "Assets.meta declares a DefinitionSetItem.",
            "thumb.jpg exists at the project root.",
            "ModProject.modhub-metadata has the Name, Summary and Tags you want "
            "shown on the Workshop page.",
            "No EditorExtensionAssemblies left in the .vrgproj.",
            "Nothing under Content/ without a matching source under Assets/ — "
            "stale compiled output ships too.",
        ],
        "traps": ["ShowDetailedErrors in "
                  "%APPDATA%/VRAGE3.ModHUB/Settings/ApplicationSettings.json "
                  "decides whether the HUB shows the real problem list or one "
                  "generic line."],
    },

    "troubleshoot": {
        "goal": "Symptom to cause.",
        "symptoms": {
            "Mod loads but nothing appears in game":
                _DEFINITION_SET_TRAP,
            "Edited a definition but the game still shows the old value":
                _PROCESSING_TRAP + " " + _REFRESH_META_TRAP,
            "validate_project fails with 'Loose metafile'":
                _VANILLA_TRAP,
            "Planet is a perfectly smooth sphere":
                "HillParams Min/Max are both 0, so the heightmap contributes no "
                "elevation. Set them (and MaxAltimeter = Max) to a fraction of "
                "the radius; EarthLike uses -0.01 / 0.12.",
            "Planet does not appear in the debug menu template list":
                "There is no PlanetInfoDefinition. Nothing references it, so no "
                "validator reports it missing.",
            "Editor plugin does not load, with no error":
                "One of the three attributes is missing: [assembly: "
                "IndexMetadata], [assembly: MetadataDependencies(...)], "
                "[module: ModuleIndexedAttributes(typeof(ProjectPluginAttribute), "
                "...)]. Without all three the assembly loads and the plugin is "
                "never instantiated, silently.",
            "Mod HUB says 'Project validation failed'":
                "Open the project in the editor and read editor_validation().",
            "Blender export produced nothing":
                "limit='SELECTED_OBJECTS' with an empty selection. Select the "
                "mesh or pass limit='VISIBLE_OBJECTS'.",
            "A GUID will not resolve":
                "Dictionary keys, TagSlots values and animation node ids are "
                "GUIDs that name a type or a node, not a file. They do not "
                "resolve in vanilla either. Only real asset references must.",
        },
    },
}


_FORMAT = {
    "content_format": (
        "Every .def/.partialdef is JSON with $Bundles, $Type and $Value. "
        "A .def's identity is $Value.Guid; a .partialdef's is "
        "$Value.Manipulator.Guid. Both must equal the AssetID in the sibling "
        ".meta. Serialisation is 2-space indent, CRLF, UTF-8 — write_definition "
        "reproduces it byte for byte."
    ),
    "partial_definitions": (
        "Copy makes a new asset from an existing one; Override changes the "
        "existing one. All 9,118 vanilla partialdefs are Copy, because vanilla "
        "defines rather than modifies. Mods use Override to change base-game "
        "content, and fields you do not touch keep tracking the original, so a "
        "game update does not break the mod."
    ),
    "meta_sidecars": (
        "FileHash is base64(MD5(file bytes)). Media GUIDs live only in the "
        ".meta, which is why model and texture references cannot be resolved "
        "without indexing them."
    ),
    "project_guids": {
        "Engine": "079da0f2-4755-491e-8688-b68b91b2fad3",
        "Vanilla": "56dacb76-e25e-468a-9432-21964a9a0569",
    },
}


def get(topic: str = "index") -> dict[str, Any]:
    topic = (topic or "index").strip().lower()
    if topic in ("index", "", "list"):
        return {
            "topics": {k: v["goal"] for k, v in RECIPES.items()},
            "content_format": _FORMAT,
            "start_here": (
                "sdk_info -> mod_recipes(topic) -> search_content to find how "
                "vanilla does it -> read_definition -> describe_type -> "
                "write_definition -> audit_project -> launch_editor -> "
                "editor_validation -> editor_build."
            ),
            "universal_traps": [_DEFINITION_SET_TRAP, _VANILLA_TRAP,
                                _PROCESSING_TRAP],
        }
    if topic in RECIPES:
        return {"topic": topic, **RECIPES[topic]}
    near = [k for k in RECIPES if topic in k or k in topic]
    return {"error": f"No recipe '{topic}'", "available": sorted(RECIPES),
            "did_you_mean": near or None}
