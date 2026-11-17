# ToolsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.ToolsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterOnlyMessage` | Localization id of text message shown when spectator or other entity tries to equip a tool with set to true |
| `CreativeOnlyMessage` | Localization id of text message shown when the player tries to equip a tool in survival, but the tool requires creative mode |
| `DebugToolMessage` | Localization id of text message shown when player is not allowed to activate debug tool |
| `GunItems` | Maps a tool gun definition to its corresponding item |
| `ItemPrefabs` | Maps a tool prefab to its corresponding item |
| `ToolActivationMessageTitle` | Localization id of text message title shown when player receives some notification related to tool activation |
| `ToolIsNotPresentInInventoryMessage` | Localization id of text message shown when player can't activate tool because it's not in the Inventory |

## A real one

`Vanilla\Assets\System\Configurations\ToolsConfiguration.def`

```json
{
  "Guid": "e4de8d3f-b37e-4427-8fff-0e13a28ff3b7",
  "ItemPrefabs": {
    "efacf7cd-db36-4176-a899-7ec973733a51": "90ad9e76-53d6-4a5a-8347-8373070751ab",
    "668fc994-a7bc-4cf5-a0af-1fff82f2bde4": "c61a5156-5ff7-4ab5-85ef-4942c4cd47d8",
    "13bef13e-8601-40c4-99f9-99bc7029d2a7": "0ad65a3f-1d03-4db5-bbed-7738b20b6eac",
    "63d99ab7-4079-41c4-ac23-39e6f848c035": "7b8259d3-57d5-4679-9d86-81f6eee952a6",
    "2a4b6f0b-c2c0-4afe-99e9-6687ae6e9b97": "770dc374-ee92-4efd-827e-208d62dedfd9",
    "a7ea95ed-1bcc-4dcb-b310-9179e489fffd": "670d2ff4-ac11-47ce-9b64-ad3ee5cdb554",
    "3b17f1b2-85c4-4f03-b2da-ae6a20cb9b07": "220e4c72-2ea6-48cc-9633-45a6ee078266",
    "2b14c152-0fc7-4184-a862-d8aa0672de46": "8a34da24-1b6a-497d-b82b-c10813d4f905",
    "4d066f59-49bc-4a97-a4d5-03e434e8275c": "d2bd7f3c-a96f-4fe7-9737-f6aeaa9e3542",
    "aee3a3fd-ff8c-4915-8489-a00d1b9694cf": "3ba4f22c-3a5b-4d6d-9c9d-ec2fdd653e51",
    "2f57501e-ab56-47ae-8889-b7a809dd6f9f": "666ddf91-ebef-470b-bcbf-5a8854a8c3b2",
    "7569b116-034d-4e1c-8445-fd3e6252ebb4": "030fc393-80cb-4afb-bbe6-cbe32d59f5cd",
    "eb2e3c27-2542-4274-adfc-a1c82dab9b47": "759a8207-9953-4b2d-bd78-8ec3d2e6fe8c",
    "a2b476b8-6a2c-4df9-b200-96b81785a8ff": "081f7c14-9d34-4552-9fae-27600e9311eb",
    "8ec72f55-dd8d-4a73-bc83-ce89ab621b6c": "3b838d8d-dae4-4050-9ecb-f116921c7c32",
    "a063048b-bdc9-4f7c-a5d1-0f77eef376c6": "054a0637-0129-4009-a223-8fa95a74ddb0"
  },
  "GunItems": {
    "15598221-dc91-4fd4-9a16-9fb00c9bb90b": "759a8207-9953-4b2d-bd78-8ec3d2e6fe8c",
    "4f74a415-652c-4142-90dc-4431e7d821a2": "081f7c14-9d34-4552-9fae-27600e9311eb",
    "cb059bf6-ee9f-4711-8945-226386ba9f91": "054a0637-0129-4009-a223-8fa95a74ddb0"
  },
  "ToolActivationMessageTitle": "ToolActivationMessageTitle",
  "DebugToolMessage": "DebugToolMessage",
  "ToolIsNotPresentInInventoryMessage": "ToolIsNotPresentInInventoryMessage",
  "CharacterOnlyMessage": "ToolCharacterOnlyMessage",
  "CreativeOnlyMessage": "ToolCreativeOnlyMessage"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolsConfigurationObjectBuilder')
search_content('', type_contains='ToolsConfigurationObjectBuilder')
```
