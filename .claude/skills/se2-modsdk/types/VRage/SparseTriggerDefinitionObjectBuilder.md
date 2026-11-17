# SparseTriggerDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.SpatialTrigger.SparseTriggerDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.SpatialTrigger`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SparseUpdate` | Defines the update frequency of the trigger. See . |

## A real one

`Vanilla\Assets\System\SpatialTriggers\SparseTrigger_Gravity.def`

```json
{
  "Guid": "0d3438e0-7421-4b58-bb5e-4af28ed58c8b",
  "SparseUpdate": 60
}
```

Others: `SparseTrigger_Targetting`, `SparseTrigger_PlanetWatchdogAssert`

---

Read it with the MCP server rather than by hand:

```
describe_type('SparseTriggerDefinitionObjectBuilder')
search_content('', type_contains='SparseTriggerDefinitionObjectBuilder')
```
