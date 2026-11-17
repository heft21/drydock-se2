# ItemDiscoveryFanfareConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ItemKnowledge.ItemDiscoveryFanfareConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.ItemKnowledge`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\ItemDiscoveryFanfareConfiguration.def`

```json
{
  "Guid": "fb9b2c0e-9628-4ea1-955a-4cf1510ae773",
  "NewItemFanfare": "f8b05504-3000-4d50-acc3-7ee766ae6dde"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemDiscoveryFanfareConfigurationObjectBuilder')
search_content('', type_contains='ItemDiscoveryFanfareConfigurationObjectBuilder')
```
