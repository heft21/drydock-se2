# SimpleRigidBodyComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Components.SimpleRigidBodyComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Components`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\DamagedBlockDebris\DamagedBlockDebrisPrefab_Client_SimpleRigidBodyComponentDefinition.def`

```json
{
  "Guid": "acde6b4f-6449-43ae-9d11-6488b1eb1757",
  "QualityType": "Default",
  "DestructionLayer": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
  "Material": "07b7d4eb-e2d6-4f1f-8e58-c46cc9a391a0",
  "EntityLayer": "Default",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SimpleRigidBodyComponentDefinitionObjectBuilder')
search_content('', type_contains='SimpleRigidBodyComponentDefinitionObjectBuilder')
```
