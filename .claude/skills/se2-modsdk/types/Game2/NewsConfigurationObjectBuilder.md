# NewsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.News.NewsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu.News`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CarouselTransitionInterval` | Interval between news transitions |
| `NewsList` | List of news to be shown on Main Menu |

## A real one

`Vanilla\Assets\MainMenuData\News\NewsConfiguration.def`

```json
{
  "Guid": "2f942df9-f06a-4438-ac14-3177ba1b5a0e",
  "NewsList": [
    {
      "Key": "aa5a4714-fec6-4a0c-aaae-501fc0022ed8",
      "Value": {
        "Title": {
          "RawText": "{Loc:News1}"
        },
        "Url": "https://support.keenswh.com/spaceengineers2/pc/announcements",
        "ProductDefinition": null,
        "Image": "{G}3f8e9c51-85c2-4141-960e-c1babb2e8bd7",
        "ImageHighlighted": "{G}0210a0d5-8937-4ae5-9a62-85f98eecd44b"
      }
    },
    {
      "Key": "032be93e-8774-4a13-a1d5-fa7c22008ff8",
      "Value": {
        "Title": {
          "RawText": "{Loc:LikeSE2}"
        },
        "Url": "https://store.steampowered.com/app/1133870/Space_Engineers_2/",
        "ProductDefinition": null,
        "Image": "{G}6a18adfb-300d-433e-ba12-8a747b88b01c",
        "ImageHighlighted": "{G}f186656a-1a81-4423-9717-19733dbb9b98"
      }
    },
    {
      "Key": "c6da27b9-8f7f-4835-84a2-1a5e03cd05a9",
      "Value": {
        "Title": {
          "RawText": "{Loc:PioneerEdition}"
        },
        "Url": "https://store.steampowered.com/app/3365540/Space_Engineers_2_Pioneer_Edition/",
        "ProductDefinition": "5ee787e5-015b-417c-ac3d-f745651643ea",
        "Image": "{G}18be44b7-a5c2-498e-b8c9-85771c5f6d93",
        "ImageHighlighted": "{G}595d00aa-7096-4c39-a529-a797b1477539"
      }
    },
    {
      "Key": "e35690b7-c043-4ac1-800c-29e47cf62cf5",
      "Value": {
        "Title": {
          "RawText": "{Loc:SE1SE2Bundle}"
        },
        "Url": "https://store.steampowered.com/bundle/55752/Space_Engineers_1_and_Space_Engineers_2/",
        "ProductDefinition": "ebf71772-e684-4897-9cf0-e1a0fa60359c",
        "Image": "{G}95b5c2ba-0429-40e2-8dac-a34e1a8ac9d0",
        "ImageHighlighted": "{G}c7dcf201-9a05-4efc-8877-88e68f4968a4"
      }
    }
  ],
  "CarouselTransitionInterval": 49999988
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('NewsConfigurationObjectBuilder')
search_content('', type_contains='NewsConfigurationObjectBuilder')
```
