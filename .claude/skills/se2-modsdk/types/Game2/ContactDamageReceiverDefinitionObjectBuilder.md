# ContactDamageReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.ContactDamageReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageCoefficient` | Multiplier of impulse to convert to damage |
| `DamageSource` | The kind of damage that will be applied |
| `ImpulseThreshold` | Minimum impulse that will be used for contact damage. Anything lower will be ignored |
| `MinSeparationSpeed` | Minimum separation speed at which impulses will be used for contact damage |

## A real one

`Vanilla\Assets\Characters\System\CharacterContactDamage.def`

```json
{
  "Guid": "d1101417-4d25-4954-b4e0-bb26fd1ab7bc",
  "ImpulseThreshold": 1000,
  "MinSeparationSpeed": 20.05,
  "DamageCoefficient": 0.01,
  "DamageSource": "c28c6d5f-44a0-4543-ba28-a7f1b2233e10"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContactDamageReceiverDefinitionObjectBuilder')
search_content('', type_contains='ContactDamageReceiverDefinitionObjectBuilder')
```
