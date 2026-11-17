# ConsumablesUIConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Consumables.ConsumablesUIConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Consumables`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumableCooldownLocKey` | Localization key for a consumable that is in cooldown. |
| `ConsumableReadyLocKey` | Localization key for a consumable that is ready to use. |

## A real one

`Vanilla\Assets\Characters\System\ConsumablesUIConfiguration.def`

```json
{
  "Guid": "504f3ea6-8a59-4140-a197-54e6c826302a",
  "ConsumableReadyLocKey": "ConsumableReady",
  "ConsumableCooldownLocKey": "ConsumableCooldown"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConsumablesUIConfigurationObjectBuilder')
search_content('', type_contains='ConsumablesUIConfigurationObjectBuilder')
```
