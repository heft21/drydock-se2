# PlanetFloraSectorPhysicsComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.Flora.PlanetFloraSectorPhysicsComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components.Flora`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TriggerTagTypes` | The type of data tags the flora sector will react to create the physics colliders for flora items. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\PlanetFloraSectorPhysicsComponentDefinition.def`

```json
{
  "Guid": "5418f4b2-01f1-4156-bdf1-eaf19591b34f",
  "QualityType": "Default",
  "DestructionLayer": "81672fe8-a7b1-4fff-9ad3-9aa4055857d4",
  "Material": "501fec2b-f978-41ea-b16a-13168b8c8665",
  "EntityLayer": "Flora",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1,
  "TriggerTagTypes": [
    {
      "Key": "3253be6d-f56a-439d-8197-0a3b4339fec1",
      "Value": "VRage:Keen.VRage.Physics.Data.DynamicTag"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetFloraSectorPhysicsComponentDefinitionObjectBuilder')
search_content('', type_contains='PlanetFloraSectorPhysicsComponentDefinitionObjectBuilder')
```
