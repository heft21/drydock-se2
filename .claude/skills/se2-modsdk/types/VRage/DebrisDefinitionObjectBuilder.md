# DebrisDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Components.Fractures.DebrisDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Components.Fractures`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConflictingTicksToDestroy` | If the fracture penetrates on more than two contacts, or if it is touching more than two different bodies an internal counter is kept. If this counter reaches this value, the fracture is destroyed |

## A real one

`Vanilla\Assets\System\FractureDebris\DebrisDefinition.def`

```json
{
  "Guid": "5e81b064-2aab-45f2-a3bf-e05db6b7418e",
  "ConflictingTicksToDestroy": 15
}
```

Others: `FloraDebrisDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DebrisDefinitionObjectBuilder')
search_content('', type_contains='DebrisDefinitionObjectBuilder')
```
