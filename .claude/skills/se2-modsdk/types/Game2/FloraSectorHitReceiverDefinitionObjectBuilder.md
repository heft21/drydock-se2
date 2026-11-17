# FloraSectorHitReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Voxels.FloraSectorHitReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Voxels`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Planets\FloraSectorHitReceiverDefinition.def`

```json
{
  "Guid": "fb8c851d-1179-474f-9e80-c46d536959b2",
  "ReceivedDamageType": "9fc2643b-1e26-4aa6-957d-e72b7292d505"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraSectorHitReceiverDefinitionObjectBuilder')
search_content('', type_contains='FloraSectorHitReceiverDefinitionObjectBuilder')
```
