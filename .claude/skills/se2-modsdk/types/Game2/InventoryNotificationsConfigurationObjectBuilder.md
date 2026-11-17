# InventoryNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Items.InventoryNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Items`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FullInventoryIcon` | Icon displayed when inventory is full |
| `FullInventoryText` | Message displayed when inventory is full |
| `GeneralNotifications` | Notifications shown for any inventory not defined in |
| `SpecialtyNotifications` | Custom notifications for particular inventories, like the character's. Behaves like a partial override to |

## A real one

`Vanilla\Assets\System\Configurations\InventoryNotificationsConfiguration.def`

```json
{
  "Guid": "a0e54ec3-1c39-469c-9d05-cede5419e0a4",
  "SpecialtyNotifications": {
    "fe9df47f-5673-4253-b797-54635d4f3f42": {
      "Notifications": {
        "ErrorFit": "74b6e2e6-118b-482e-9ee0-143535bbf20c"
      }
    },
    "3f68b3b4-e5a2-49cb-af37-27a676b7a683": {
      "Notifications": {
        "ErrorFull": "fef5346b-02b7-4de6-8682-358074f957aa"
      }
    }
  },
  "GeneralNotifications": {
    "Notifications": {
      "ErrorFull": "2ba4b9f2-edcd-4067-9484-416df4d8f8f9",
      "ErrorFit": "35b5f033-e485-4da0-9521-8eb0f55352ab",
      "ErrorFilter": "70527190-e810-4052-ba7d-1836b6725e6f",
      "ErrorMissingInventory": "a93b488b-32aa-4e33-9ae4-5d08eccb07ff"
    }
  },
  "FullInventoryText": "InventoryFullNotification",
  "FullInventoryIcon": "{G}9e93802d-967a-4ab8-affb-a32d1cfae1d7"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryNotificationsConfigurationObjectBuilder')
search_content('', type_contains='InventoryNotificationsConfigurationObjectBuilder')
```
