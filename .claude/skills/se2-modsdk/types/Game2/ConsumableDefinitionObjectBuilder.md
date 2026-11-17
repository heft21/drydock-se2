# ConsumableDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Consumables.ConsumableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Consumables`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AutoUseThresholds` | Allows automatically using the consumable if present in inventory |
| `ConsumableUsedAudio` | Audio event played when the consumable is used |
| `Cooldown` | Cooldown applied to the cooldown category after use |
| `CooldownCategory` | Shared category for the consumable for cooldown. |
| `Effects` | Effect to apply when consumed. |
| `MissingItemLocKey` | Localization key for when corresponding consumable that is missing in the inventory. |
| `StatsMaxLocKey` | Localization key for when the affected stats are already maxed |

## A real one

`Vanilla\Assets\Items\Consumables\Medikit\ConsumableMedikitSmall.def`

```json
{
  "Guid": "3042ad6b-e888-4ee0-9e04-bf7cf77afd4a",
  "DisplayName": "ConsumableMedikit",
  "Description": "",
  "Icon": "{G}7f6ec201-75be-478d-98c2-ec64cdbbbba5",
  "MassPerUnit": 5,
  "Flags": 0,
  "Type": "Consumable",
  "DefaultMetaData": null,
  "IsRareLoot": false,
  "ShouldAutoEquip": true,
  "ShowDiscoveryFanfare": true,
  "ExplosiveRisk": 0,
  "Effects": [
    {
      "Key": "5fcd92c0-8955-4e84-ab31-20c629a8eab3",
      "Value": {
        "Stat": "3a40976e-7f57-46ea-a1a3-4d8124722e04",
        "Duration": 49999996,
        "ApplicationInterval": 4999997,
        "Amount": 100
      }
    }
  ],
  "CooldownCategory": "04194257-f33b-4613-9b8e-ee76f335bf6f",
  "AutoUseThresholds": [],
  "Cooldown": 100000000,
  "StatsMaxLocKey": "ConsumableHealthMax",
  "MissingItemLocKey": "ConsumableMissingMedikit",
  "ConsumableUsedAudio": "event:/UI/Restore_health"
}
```

Others: `ConsumableSuitBattery`, `ConsumableOxygenRecharge`

---

Read it with the MCP server rather than by hand:

```
describe_type('ConsumableDefinitionObjectBuilder')
search_content('', type_contains='ConsumableDefinitionObjectBuilder')
```
