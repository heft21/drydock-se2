# InventorySlotRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.InventorySlotRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SlotDummyType` | that will be used to find which dummy the items should be attached to. To support multiple slots, the dummy name must contain an index at the end of the name like "CellSlot 0". |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Battery_Client_InventorySlotRenderDefinition.def`

```json
{
  "Guid": "0d9b719d-f1b4-4e12-a882-bd19ba500bc9",
  "SlotDummyType": "0dd8466e-8e44-4ebf-93de-218954b34f43"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventorySlotRenderDefinitionObjectBuilder')
search_content('', type_contains='InventorySlotRenderDefinitionObjectBuilder')
```
