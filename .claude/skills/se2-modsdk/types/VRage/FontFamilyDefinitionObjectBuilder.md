# FontFamilyDefinitionObjectBuilder

`VRage:Keen.VRage.Render.UI.FontFamilyDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.UI`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FontFamily` | Name of the family. |
| `Fonts` | List of fonts that make up this family. |

## A real one

`Engine\Assets\Data\Fonts\NotoSans\NotoSans_FontFamilyDefinition.def`

```json
{
  "Guid": "558bf912-cbe6-49ce-9e8d-f211e5c70506",
  "FontFamily": "NotoSans",
  "Fonts": [
    {
      "Key": "4507a35b-314f-45a0-88c6-610cf59bc790",
      "Value": "0c519c1d-22ea-49ea-b82c-70e3a937f193"
    },
    {
      "Key": "80f0357d-a2d6-46c0-93a1-fe20e325a35a",
      "Value": "38c5488b-15e2-47de-bc42-73871f24a978"
    },
    {
      "Key": "c9c82f0d-2b4e-44fb-b190-40a4adffc397",
      "Value": "1fef3b82-1091-45e8-b9f8-5e11722f7f8f"
    }
  ]
}
```

Others: `RobotoMonoFontFamily`

---

Read it with the MCP server rather than by hand:

```
describe_type('FontFamilyDefinitionObjectBuilder')
search_content('', type_contains='FontFamilyDefinitionObjectBuilder')
```
