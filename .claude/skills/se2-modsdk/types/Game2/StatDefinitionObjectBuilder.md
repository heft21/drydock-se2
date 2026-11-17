# StatDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Stats.StatDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Stats`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxValue` | Base maximum value this stat can have |
| `MinValue` | Base minimum value this stat can have |
| `ModifiableInCreative` | Should this stat be modifiable in creative mode. For example Health shouldn't so the character can't die |
| `ValueOnSwitchingToCreative` | What value should this stat have when switching to creative mode. For example Health should be restored to 100% |

## A real one

`Vanilla\Assets\Characters\System\Stats\Energy.def`

```json
{
  "Guid": "675206d7-7a7a-445c-946c-e0a74bbcd862",
  "MinValue": 0,
  "MaxValue": 342,
  "ModifiableInCreative": false,
  "ValueOnSwitchingToCreative": 342
}
```

Others: `Health`, `Oxygen`

---

Read it with the MCP server rather than by hand:

```
describe_type('StatDefinitionObjectBuilder')
search_content('', type_contains='StatDefinitionObjectBuilder')
```
