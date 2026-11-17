# KeyDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.Utils.KeyDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.Utils`
- definitions using it: **4**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Controller\NamedCameraPrefabs\DeltaSpectatorKey.def`

```json
{
  "Guid": "104cf078-21fa-41a8-a28a-022132fdef37"
}
```

Others: `AutomatedTurretKey`, `ColonizationMapKey`

---

Read it with the MCP server rather than by hand:

```
describe_type('KeyDefinitionObjectBuilder')
search_content('', type_contains='KeyDefinitionObjectBuilder')
```
