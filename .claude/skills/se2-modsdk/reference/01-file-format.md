# The definition file format

## The envelope

Every `.def` and `.partialdef`:

```json
{
  "$Bundles": { "System.Runtime": "1.0.0.0", "VRage": "2.3.0.2798" },
  "$Type": "Bundle:Full.Type.Name",
  "$Value": { "Guid": "…", … }
}
```

- `$Bundles` stamps the assembly versions the file was authored against.
  Measured over 400 vanilla files the key set is always
  `{System.Runtime, VRage}` or `{Game2, System.Runtime, VRage}`;
  `System.Runtime` is always `1.0.0.0` and every other bundle carries one shared
  version — the SDK build that wrote the file. Include `Game2` when any `$Type`
  in the document is a `Game2:` type.
- `$Type` is `bundle:namespace.TypeObjectBuilder`.
- `$Value.Guid` is the definition's identity, and must equal the `AssetID` in
  the sibling `.meta`.

**Serialisation is 2-space indent, CRLF line endings, UTF-8.** Key order is
significant: the game side uses Newtonsoft.Json, which requires `$id` to be the
first property of an object when present. Never re-serialise a definition with a
generic JSON writer that reorders keys.

## `.meta` sidecars

Every source file — definition, texture, model, folder — has a `<name>.meta`
beside it. Without one the content pipeline does not see the file at all.

```json
{
  "$Type": "VRage:Keen.VRage.ContentPipeline.Metafiles.MetaData",
  "$Value": {
    "AssetID": "…",
    "InternalItems": [
      { "$Type": "…Structure.FileInfoMetaDataItem", "FileHash": "…" },
      { "$Type": "…AssetProcessing.AssetProcessingMetaDataItem",
        "ProcessorInfo": { "Version": 2, "Identifier": "P_DEF" },
        "ContentFiles": { "MainOutput": { "FileHash": "…", "FileName": "…" },
                          "AdditionalOutputs": [] },
        "Problems": [], "DependenciesHashes": [],
        "AssetHash": "…", "OverrideDetachedState": false,
        "IgnoredErrors": "None" },
      { "$Type": "…Definitions.DefinitionFlagsMetadata", "Flags": "None" }
    ]
  }
}
```

**`FileHash` is `base64(MD5(file bytes))`** — verified byte-for-byte against
vanilla content. The pipeline compares the stored hash with the file, so editing
an asset and leaving its `.meta` alone manufactures the *"dependencies hashes do
not match"* publish failure.

A `.meta` with an empty `InternalItems` is a marker, not a processed asset —
that is what folders and definition sets use.

**Media GUIDs live only in the `.meta`.** A `.png` or `.fbx` has no GUID inside
it, so a `Model`/`Texture`/`Icon` reference can only be resolved by indexing the
sidecars.

## Partialdefs

`.partialdef` is the SDK's central pattern — over 9,100 of the shipped
definitions. A partialdef is a delta against a base rather than a whole object:

```json
{
  "$Type": "VRage:Keen.VRage.ContentPipeline.Definitions.PartialDefinitionDiff",
  "$Value": {
    "BaseDefinition": "<guid of the thing being patched>",
    "PartialDefinitionKind": "Copy" | "Override",
    "Manipulator": { "Guid": "<this file's identity>", …fields to change… },
    "DefinitionType": "VRage:Full.Type.Of.The.Base",
    "PriorityOverride": false
  }
}
```

- **`Copy`** makes a *new* definition from an existing one. Its `Manipulator`
  carries a `Guid` — the new asset's identity. All ~9,100 vanilla partialdefs
  are `Copy`, because vanilla defines rather than modifies.
- **`Override`** changes the existing definition in place. It declares **no
  Guid anywhere in its body**; its identity is only the `.meta` `AssetID`. This
  is what a mod uses to patch base-game content, and fields you do not touch
  keep tracking the original — so a game update does not silently break you.

Note `DefinitionType` names the runtime definition type (`…PlanetaryWaterLayersDefinition`),
not the object builder (`…PlanetaryWaterLayersDefinitionObjectBuilder`).

## Delta-encoded collections

Lists and dictionaries inside a `Manipulator` are usually delta-encoded rather
than written out whole:

```json
"Components": {
  "$DeltaEncoded": true,
  "Keys": [ "<guid>", "<guid>", … ],
  "Changed": [
    { "Kind": "Update", "Index": 4,  "Value": { "Definition": "<guid>" } },
    { "Kind": "Insert", "Index": 26, "Value": { "Definition": "<guid>",
                                                "Type": "Bundle:Full.Component.Type" } }
  ],
  "Removed": []
}
```

`Keys` is the identity list — one GUID per slot, positional. To **add** an entry
you append a fresh GUID to `Keys` and add a `Changed` entry with
`"Kind": "Insert"` at that index. To **change** an inherited entry you leave
`Keys` alone and use `"Kind": "Update"` at its index.

Dictionaries use a different shape with `$Key`/`$Value` pairs:

```json
"TagSlots": {
  "$DeltaEncoded": true,
  "RemovedKeys": [],
  "ModifiedKeys": [ { "$Key": "PhysicsColliderProvider", "$Value": "<guid>" } ]
}
```

**The `Keys` GUIDs do not resolve to anything**, in vanilla either. They are
identity keys for the slot, not asset references. The same is true of
`SurfaceBiomes` keys, `MaterialRules` keys, `TagSlots` values and animation node
ids. Only the `Value` side has to resolve. Do not go hunting for a file behind a
key GUID.

## Types that carry JSON but are not definitions

`.planetcubemap`, `.cubemap`, `.comptex` and `.fbxsettings` are asset files whose
*content* is JSON referencing other assets by GUID. They are processed as media
(their GUID comes from the `.meta`), so their outgoing references are invisible
to a definition index — `audit_project` walks them separately for exactly this
reason.
