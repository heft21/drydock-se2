# EventControllerIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar.EventControllerIndicatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## What it is

's object builder.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultMaterials` | Default materials to use if not defined in . |
| `IndicatorMeshParts` | Collection of mesh part which the materials should be replaced. |
| `MeshPartMaterialOverrides` | Collection of what materials override that should be assigned to specific MeshParts at specific state. |
| `ReplacementModels` | Collection of Models to which the replacements should be applied. will be applied only to Models in this list. |

## A real one

`Vanilla\Assets\Blocks\EventController\100\EventController_Client_EventControllerIndicatorDefinition.def`

```json
{
  "Guid": "374b5d78-dc1b-4b81-809d-cfb7b2ee0472",
  "ReplacementModels": [
    "{G}18eb076a-6b25-4132-aced-7418689a8d83",
    "{G}f33e876a-de86-4e64-9b6d-928099e05092",
    "{G}dbb59c02-cfe1-45af-ba20-4088d62793c3"
  ],
  "DefaultMaterials": {
    "NotFunctional": "bcefad69-a79d-498b-97c8-5f2c024cfc52",
    "NotPowered": "b6fdd8d4-e494-47d9-bdb4-5ddfdf10fcc8",
    "NullState": "4501676a-6812-4869-af19-e33ddeae57e0",
    "True": "b290e27f-5acc-4235-aa1e-b2f7f237e539",
    "False": "b290e27f-5acc-4235-aa1e-b2f7f237e539"
  },
  "IndicatorMeshParts": [
    "Emissive01",
    "Emissive02",
    "Fracture_01_Hide-Emissive01",
    "Fracture_01_Hide-Emissive02",
    "Fracture_02_Hide-Emissive01",
    "Fracture_02_Hide-Emissive02",
    "Fracture_03_Hide-Emissive01",
    "Fracture_03_Hide-Emissive02",
    "Fracture_04_Hide-Emissive01",
    "Fracture_04_Hide-Emissive02"
  ],
  "MeshPartMaterialOverrides": [
    {
      "IndicatorMeshPart": "Emissive02",
      "State": "True",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_01_Hide-Emissive02",
      "State": "True",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_02_Hide-Emissive02",
      "State": "True",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_03_Hide-Emissive02",
      "State": "True",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_04_Hide-Emissive02",
      "State": "True",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Emissive01",
      "State": "False",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_01_Hide-Emissive01",
      "State": "False",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_02_Hide-Emissive01",
      "State": "False",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_03_Hide-Emissive01",
      "State": "False",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    },
    {
      "IndicatorMeshPart": "Fracture_04_Hide-Emissive01",
      "State": "False",
      "Material": "bcefad69-a79d-498b-97c8-5f2c024cfc52"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EventControllerIndicatorDefinitionObjectBuilder')
search_content('', type_contains='EventControllerIndicatorDefinitionObjectBuilder')
```
