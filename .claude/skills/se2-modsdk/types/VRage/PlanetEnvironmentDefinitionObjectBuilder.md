# PlanetEnvironmentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetEnvironmentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **7**

## What it is

VRage | Planets - 2D Clipmap Spatial Trigger System

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ProceduralTriggerTagTypes` | The type of data tags the procedural system will react to to spawn the items. |
| `SecondaryTriggerEnterMargin` | Secondary margin used for predicting another layer of sectors. Helps to separate if certain areas of the planet (like underground) need a different spawn range to minimize spawn area. NOTE: For detailed information, check the documentation above. |
| `SecondaryTriggerExitMargin` | The margin around each sector for delayed dematerialization. Serves to prevent abrupt transitions by ensuring that sectors are not immediately dematerialized after an entity exits the actual trigger box. For best results, it is recommended that this value is higher than the NOTE: For detailed information, check the documentation above. |
| `TriggerBoxSize` | Specifies the size of a single sector within the environment system. NOTE: For detailed information, check the Spatial Trigger System documentation above. |
| `TriggerEnterMargin` | The margin around each sector for preemptive materialization. Helps to provide a seamless transition by ensuring that sectors are materialized before an entity enters the actual trigger box. NOTE: For detailed information, check the documentation above. |
| `TriggerExitMargin` | The margin around each sector for delayed dematerialization. Serves to prevent abrupt transitions by ensuring that sectors are not immediately dematerialized after an entity exits the actual trigger box. For best results, it is recommended that this value is higher than the NOTE: For detailed information, check the documentation above. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\EnvironmentDataServer.def`

```json
{
  "Guid": "21fcaa32-afa6-420d-ad07-00fba7c906c1",
  "TriggerBoxSize": 256,
  "TriggerEnterMargin": 400,
  "TriggerExitMargin": 500,
  "SecondaryTriggerEnterMargin": 400,
  "SecondaryTriggerExitMargin": 500,
  "ProceduralTriggerTagTypes": [
    {
      "Key": "8ec58ddb-f2ac-43a9-89eb-ae5851882853",
      "Value": "VRage:Keen.VRage.Physics.Data.DynamicTag"
    }
  ]
}
```

Others: `ByblosEnvironmentServer`, `VerdureEnvironmentServer`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentDefinitionObjectBuilder')
search_content('', type_contains='PlanetEnvironmentDefinitionObjectBuilder')
```
