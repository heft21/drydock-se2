# GameplayDebugScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Game.Debug.GameplayDebugScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.Debug`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\Screens\GameplayDebugScreenConfiguration.def`

```json
{
  "Guid": "760f6911-6f42-4f03-a0af-fef71752f25f",
  "BlockPlacerDefinition": "5696fd72-e2e3-4f91-b131-4b330440ea97",
  "WorldSessionDefinition": "9a129741-96d4-45fa-8b34-60707317cc8a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameplayDebugScreenConfigurationObjectBuilder')
search_content('', type_contains='GameplayDebugScreenConfigurationObjectBuilder')
```
