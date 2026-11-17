# CultureIdDefinitionObjectBuilder

`VRage:Keen.VRage.Library.Localization.CultureIdDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Library.Localization`
- definitions using it: **13**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CultureId` | The unique short identifier for the culture. Example: en-US. |
| `Default` | Get default instance of . The data represents valid state. |
| `LocalizedName` | The display name used to reference the culture. This field is required to have this localization show in the GUI menu. Example: English (United States). |

## A real one

`Vanilla\Assets\MainMenuData\Texts\CultureIdentifiers\ID_cz-CZ.def`

```json
{
  "Guid": "86528d8b-0ab3-477e-bc21-cf1d22464b16",
  "LocalizedName": "\u010ce\u0161tina",
  "CultureId": "cz-CZ"
}
```

Others: `ID_de-DE`, `ID_en-US`

---

Read it with the MCP server rather than by hand:

```
describe_type('CultureIdDefinitionObjectBuilder')
search_content('', type_contains='CultureIdDefinitionObjectBuilder')
```
