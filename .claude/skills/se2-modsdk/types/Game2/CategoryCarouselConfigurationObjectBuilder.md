# CategoryCarouselConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.CategoryCarouselConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CarouselLeftDisabledIcon` | Left arrow icon for carousel when disabled |
| `CarouselLeftHighContrastIcon` | Left arrow icon for carousel when in high contrast |
| `CarouselLeftHighlightIcon` | Left arrow icon for carousel when highlighted |
| `CarouselLeftIcon` | Left arrow icon for carousel |
| `CarouselRightDisabledIcon` | Right arrow icon for carousel when disabed |
| `CarouselRightHighContrastIcon` | Right arrow icon for carousel when in high contrast |
| `CarouselRightHighlightIcon` | Right arrow icon for carousel when highlighted |
| `CarouselRightIcon` | Right arrow icon for carousel |

## A real one

`Vanilla\Assets\MainMenuData\UI\Terminal\CategoryCarouselConfiguration.def`

```json
{
  "Guid": "6c03c221-6c91-4d25-ba92-df303977d2df",
  "CarouselLeftIcon": "{G}0ce1bbe4-97c1-4faa-af63-b13ef6429cee",
  "CarouselLeftHighlightIcon": "{G}34f9a628-daa5-4422-bdd5-3aa3ada4dc98",
  "CarouselLeftHighContrastIcon": "{G}1b5bf214-72c5-4393-ad0b-1feeac63c2ab",
  "CarouselLeftDisabledIcon": "{G}604022fd-7fb8-4024-82fe-09939513eb38",
  "CarouselRightIcon": "{G}ec4f8f56-01a0-45ed-b453-1c8c72a9f978",
  "CarouselRightHighlightIcon": "{G}6dc81daa-cd20-4786-bde2-951598d6a3b9",
  "CarouselRightHighContrastIcon": "{G}60e44d1e-a3a5-4e9a-8021-5669706035c5",
  "CarouselRightDisabledIcon": "{G}9baad671-91fb-4853-995a-4d6cab0684a0"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CategoryCarouselConfigurationObjectBuilder')
search_content('', type_contains='CategoryCarouselConfigurationObjectBuilder')
```
