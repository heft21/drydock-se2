# FloatingObjectHitReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FloatingObjectHitReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\FloatingObjects\FloatingObjectHitReceiverDefinition.def`

```json
{
  "Guid": "94f34c0a-b0e8-47b1-90dd-49f6d4c98ca7",
  "ReceivedDamageType": "1a83ac16-b2e3-4fa5-869f-fa1cd63b290e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloatingObjectHitReceiverDefinitionObjectBuilder')
search_content('', type_contains='FloatingObjectHitReceiverDefinitionObjectBuilder')
```
