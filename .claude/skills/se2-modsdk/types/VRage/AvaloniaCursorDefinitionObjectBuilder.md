# AvaloniaCursorDefinitionObjectBuilder

`VRage:Keen.VRage.UI.Definitions.AvaloniaCursorDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.UI.Definitions`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HotSpot` | The point within the cursor's icon image considered the click point. Specified in pixel coordinates relative to the top-left corner of the image. |
| `Icon` | The image used to represent the cursor. |

## A real one

`Vanilla\Assets\MainMenuData\UI\Cursors\AvaloniaCursorDefinition_No.def`

```json
{
  "Guid": "29d81ff0-7cd9-4202-a534-5e341e55088a",
  "Icon": "{G}0794d820-59d7-4c33-bbff-cd5c3f4b83a1",
  "HotSpot": {
    "X": 0,
    "Y": 0
  }
}
```

Others: `AvaloniaCursorDefinition_Hand`, `AvaloniaCursorDefinition_Wait`

---

Read it with the MCP server rather than by hand:

```
describe_type('AvaloniaCursorDefinitionObjectBuilder')
search_content('', type_contains='AvaloniaCursorDefinitionObjectBuilder')
```
