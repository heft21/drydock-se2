# WindTurbineIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Production.WindTurbineIndicatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Production`
- definitions using it: **1**

## What it is

Object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultMaterials` | Default materials to use if not defined in . |
| `IndicatorMeshParts` | Collection of mesh parts which the materials should be replaced. |
| `LowEfficiencyThreshold` | Efficiency threshold below which is shown. |
| `MediumEfficiencyThreshold` | Efficiency threshold below which is shown. |
| `MeshPartMaterialOverrides` | Collection of what materials override that should be assigned to specific MeshParts at specific state. |
| `ReplacementModels` | The model to which the material replacements should be applied. will be applied only to Models in this list. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WindTurbine_Client_WindTurbineIndicatorDefinition.def`

```json
{
  "Guid": "9928156b-33d4-4a0a-93e1-57650e806e49",
  "ReplacementModels": [],
  "IndicatorMeshParts": [],
  "DefaultMaterials": {
    "NotFunctional": "ca0cf806-7ac2-4427-93d9-5dbf5cdf9803",
    "FunctionalNoEfficiency": "dc384332-a23e-45f1-9a1a-e60f5ad2250a",
    "FunctionalLowEfficiency": "4a74bc1c-0530-4c06-a5c5-5d91f11353f4",
    "FunctionalMediumEfficiency": "413f1a47-9eba-4311-88d5-cd1ddece5a97",
    "FunctionalHighEfficiency": "bbbb06ff-6210-4f4b-a806-28f6a77c1cf1",
    "FunctionalMaxEfficiency": "9124c1e5-20b4-4669-8404-9f75bedc23f1"
  },
  "MeshPartMaterialOverrides": [],
  "LowEfficiencyThreshold": 0.33,
  "MediumEfficiencyThreshold": 0.66
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WindTurbineIndicatorDefinitionObjectBuilder')
search_content('', type_contains='WindTurbineIndicatorDefinitionObjectBuilder')
```
