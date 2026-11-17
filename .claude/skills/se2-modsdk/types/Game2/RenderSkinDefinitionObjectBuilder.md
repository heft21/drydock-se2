# RenderSkinDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.RenderSkinDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DLC` | For the player to apply this skin, they must own the associated DLC, if any. |
| `DisplayName` | Name of the skin displayed in UI |
| `HoverIcon` | Hover icon shown for this skin in selection UI. Falls back to if not set. |
| `Icon` | Icon shown for this skin in UI |
| `MaterialPairing` | Maps character model parts to the materials that should be used to render them |
| `Model` | Optional override of the character model. When set, all render strategies on the character render this model instead of the one declared on their CharacterRenderStrategyDefinition. Must share the same skeleton/bones. |
| `MovementEffectsOverride` | Optional override of the character's movement effects definition. Used for relocating the jetpack particles |

## A real one

`Vanilla\Assets\Characters\System\Skins\PioneerSkin.def`

```json
{
  "Guid": "2fce00cb-41a1-4b20-b891-b1992977c90b",
  "MaterialPairing": [],
  "Model": "{G}29b72b95-9d6a-402a-99e8-eef99ae29166",
  "DLC": "8a7446cb-3b0c-4fbc-8b82-82a26e604674",
  "DisplayName": "SkinPioneer",
  "Icon": "{G}aaa31dbe-309c-4323-9e1a-aea53421011a",
  "HoverIcon": null,
  "MovementEffectsOverride": "50bf3a8d-10be-43f8-9cda-46d09e7eff03",
  "BackpackPrefab": "fadb43a8-7e9f-4c5f-8a8d-e03cc12a16d0"
}
```

Others: `CharacterKeenSkin`, `VeteranSkin`

---

Read it with the MCP server rather than by hand:

```
describe_type('RenderSkinDefinitionObjectBuilder')
search_content('', type_contains='RenderSkinDefinitionObjectBuilder')
```
