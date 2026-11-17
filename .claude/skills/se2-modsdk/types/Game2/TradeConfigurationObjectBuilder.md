# TradeConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Trade.TradeConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Trade`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BuyHeaderKey` | Localization key for buy header text |
| `BuyKey` | Localization key for buy text |
| `CreditsIcon` | Icon to use for displaying credits in the UI |
| `CreditsName` | Localized name for credits. |
| `CurrencyKey` | Localization key for currency |
| `ItemCantFit` | Generic reason to use when a more specific reason can't be determined. |
| `ItemNotTradable` | Indicates that the item can't be traded at a particular trade terminal. |
| `OnItemBuyAudio` | Audio event to play upon buying an item from a trader. One-shot sound |
| `OnItemSellAudio` | Audio event to play upon selling an item to a trader. One-shot sound |
| `PlayerInsufficientCredits` | Indicates that the player doesn't have enough credits to complete the transaction. |
| `PriceKey` | Localization key for price |
| `SellHeaderKey` | Localization key for sale header text |
| `SellKey` | Localization key for sale text |
| `TotalCostKey` | Localization key for total cost text |
| `TotalProfitKey` | Localization key for total profit text |
| `TradeNotPossible` | Generic reason to use when a more specific reason can't be determined. |
| `TraderBackground` | Background image for the right-side panel (trader panel) |
| `TraderIcon` | Icon to use for displaying the trader in the UI |
| `TraderInsufficientCredits` | Indicates that the trader doesn't have enough credits to complete the transaction. |

## A real one

`Vanilla\Assets\UI\TradeConfiguration.def`

```json
{
  "Guid": "affc554d-0e7a-4e73-ba50-7d1019e2e291",
  "CreditsIcon": "{G}bd36407f-85f9-4828-87d2-f73f8ac2243c",
  "TraderIcon": "{G}567103f7-bc83-4247-80d0-e34e5ce8d843",
  "TraderBackground": "{G}6b6437b4-cf29-446b-b817-1618f2378e7e",
  "CreditsName": "Credits",
  "SellHeaderKey": "TradeScreenSellHeader",
  "SellKey": "TradeScreenSell",
  "BuyHeaderKey": "TradeScreenBuyHeader",
  "BuyKey": "TradeScreenBuy",
  "CurrencyKey": "TradeScreenCurrency",
  "PriceKey": "TradeScreenPrice",
  "TotalCostKey": "TradeScreenTotalCost",
  "TotalProfitKey": "TradeScreenTotalProfit",
  "TraderInsufficientCredits": "TraderNotEnoughCredits",
  "PlayerInsufficientCredits": "NotEnoughCredits",
  "ItemNotTradable": "ItemNotTradable",
  "ItemCantFit": "ItemCantFit",
  "TradeNotPossible": "TradeNotPossible",
  "OnItemBuyAudio": "event:/UI/trading_buy",
  "OnItemSellAudio": "event:/UI/trading_sell"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TradeConfigurationObjectBuilder')
search_content('', type_contains='TradeConfigurationObjectBuilder')
```
