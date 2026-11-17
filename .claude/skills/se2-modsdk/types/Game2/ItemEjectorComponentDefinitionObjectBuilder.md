# ItemEjectorComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.ItemEjectorComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EjectionSpeed` | Speed at which ejected items will move away. |
| `EjectorDummy` | Dummy at which ejected items are spawned, moving in Z direction. Items are only spawned if the dummy volume is empty. |
| `MaxBatchMass` | Maximum amount of mass to eject in one batch. If an item is not divisible, it will be ejected in whole units, rounded down, and at minimum 1 at a time, even if it has more mass than set here. If an item does not stack, it is always ejected 1 at a time. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ItemEjectorComponentDefinition.def`

```json
{
  "Guid": "26a6ab1d-b57d-4e29-8c79-67769e4b0eb0",
  "EjectorDummy": null,
  "MaxBatchMass": 0,
  "EjectionSpeed": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemEjectorComponentDefinitionObjectBuilder')
search_content('', type_contains='ItemEjectorComponentDefinitionObjectBuilder')
```
