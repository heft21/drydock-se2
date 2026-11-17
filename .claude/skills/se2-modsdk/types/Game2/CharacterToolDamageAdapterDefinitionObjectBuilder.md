# CharacterToolDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage.CharacterToolDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Damage` | Damage to be applied to character |
| `DamageSource` | The kind of damge the tool does to characters |
| `Impulse` | Impulse applied to the character |

## A real one

`Vanilla\Assets\CharacterTools\HandGrinders\Shared\HandGrinder_CharacterToolDamageAdapterDefinition.def`

```json
{
  "Guid": "cf20de10-e709-4fab-8ed4-c780759308a9",
  "Damage": 6,
  "Impulse": 100,
  "DamageSource": "19b07230-a7eb-400d-aa70-1a4eea2428e5"
}
```

Others: `HandDrill_DamageAdapterPrefab_Server_CharacterToolDamageAdapterDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterToolDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='CharacterToolDamageAdapterDefinitionObjectBuilder')
```
