# PlanetEnvironmentClientDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.PlanetEnvironmentClientDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **7**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\EnvironmentClient.def`

```json
{
  "Guid": "8ee025c4-c3a7-4177-aa8b-63ba6f8e6004",
  "TriggerBoxSize": 256,
  "TriggerEnterMargin": 4000,
  "TriggerExitMargin": 5000,
  "SecondaryTriggerEnterMargin": 400,
  "SecondaryTriggerExitMargin": 500,
  "ProceduralTriggerTagTypes": [
    {
      "Key": "b842de93-92e6-4ee4-b802-a1162fde8c65",
      "Value": "VRage:Keen.VRage.Core.Game.GameSystems.GamePruning.ClientTriggerTag"
    }
  ]
}
```

Others: `ByblosEnvironmentClient`, `VerdureEnvironmentClient`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentClientDefinitionObjectBuilder')
search_content('', type_contains='PlanetEnvironmentClientDefinitionObjectBuilder')
```
