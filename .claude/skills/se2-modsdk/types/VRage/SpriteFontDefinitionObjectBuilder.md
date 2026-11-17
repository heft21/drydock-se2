# SpriteFontDefinitionObjectBuilder

`VRage:Keen.VRage.Render.UI.SpriteFontDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.UI`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Sprites` | Sprites used by this font. |

## A real one

`Engine\Assets\Data\Fonts\Monospace\Monospace.def`

```json
{
  "Guid": "34c4c656-ccc7-4ad2-9fc9-324087b8423d",
  "File": "{G}7d8635c7-8393-4447-9860-617bfc5c4676",
  "Style": "Regular",
  "Weight": "Regular",
  "Sprites": [
    {
      "Key": "dabd40c6-381a-4365-9cda-a3b2ee135ec1",
      "Value": "{G}e1251390-6a39-47f6-aed9-eb1a9a2baccc"
    },
    {
      "Key": "07f6e8b6-371e-40f8-8397-fde0dba3946a",
      "Value": "{G}20aef846-5368-4436-ab58-cdfec06952a8"
    },
    {
      "Key": "2d14fbf4-5a0e-47ae-8422-6552b8b8270e",
      "Value": "{G}82e8c753-89c5-4a39-8b97-e35cd1c8ec9a"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpriteFontDefinitionObjectBuilder')
search_content('', type_contains='SpriteFontDefinitionObjectBuilder')
```
