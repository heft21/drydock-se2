# PowerableBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.PowerableBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedResource` | Specify the type and amount of resource consumed by this block while operational. When 0, no resource will be consumed, but resource must still be present to work. When null, no resource will be consumed (useful for having blocks with on/off state but no power consumption). |
| `ConsumptionPriority` | Priority of this block in the resource distribution system. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\PowerableBlockDefinition.def`

```json
{
  "Guid": "794c5233-6a1c-4932-b37c-03a0e539d069",
  "UIData": {
    "Name": "",
    "Icon": "{G}f07eda89-27f7-4d23-8073-00b72b3e7397"
  },
  "PlacerDefinition": null,
  "MountPointGeneratorSettings": {
    "Enabled": true,
    "Sampler": "Circular8",
    "Directions": "All"
  },
  "MountPointsGroupsPerDirection": {},
  "Density": null,
  "Fragility": "eaaa3a8d-d04c-461f-a7f5-00e8cabd27bd",
  "DisplaySizeOverride": null,
  "Permeability": false,
  "DeformationResistance": 0.9,
  "DestructionThreshold": 0.3,
  "WeakThreshold": 0.8,
  "WeaknessMultiplier": 0.8,
  "Recipe": null,
  "RecipeEfficiency": null,
  "BlockKind": null,
  "PCU": 1,
  "ConsumedResource": {
    "Type": null,
    "Amount": 0
  },
  "ConsumptionPriority": {
    "Priority": 10
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PowerableBlockDefinitionObjectBuilder')
search_content('', type_contains='PowerableBlockDefinitionObjectBuilder')
```
