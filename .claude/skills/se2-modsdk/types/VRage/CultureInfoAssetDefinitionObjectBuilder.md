# CultureInfoAssetDefinitionObjectBuilder

`VRage:Keen.VRage.Library.Localization.CultureInfoAssetDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Library.Localization`
- definitions using it: **13**

## What it is

Migrations for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Default` | Get default instance of . The data represents valid state. |
| `Resources` | A collection of resources required for localizing various content types. Each resource maps a localization file to a specific content identifier within the culture. |

## A real one

`Vanilla\Assets\MainMenuData\Texts\cz-CZ.def`

Too large to inline. Fields present:

`CultureId`, `Guid`, `Resources`

Others: `de-DE`, `en-US`

---

Read it with the MCP server rather than by hand:

```
describe_type('CultureInfoAssetDefinitionObjectBuilder')
search_content('', type_contains='CultureInfoAssetDefinitionObjectBuilder')
```
