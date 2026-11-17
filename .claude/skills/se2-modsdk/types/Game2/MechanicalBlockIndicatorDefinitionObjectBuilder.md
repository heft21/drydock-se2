# MechanicalBlockIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockIndicatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks`
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

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MechanicalBlockIndicatorDefinition.def`

```json
{
  "Guid": "6ac5adad-f3ab-4364-99c1-1ad3c47e2747",
  "ReplacementModels": [],
  "DefaultMaterials": {
    "NotPowered": "b6fdd8d4-e494-47d9-bdb4-5ddfdf10fcc8",
    "NotFunctional": "bcefad69-a79d-498b-97c8-5f2c024cfc52",
    "TurnedOff": "a9ca4ce7-175d-4bc1-a47c-c109966f5928",
    "ReadyToAlign": "5fa3aeb0-0e36-406c-b22c-3e05ebde345b",
    "ReadyToConnect": "4501676a-6812-4869-af19-e33ddeae57e0",
    "Aligning": "1565ddbb-0ba9-4a75-a1eb-321f6c2485a6",
    "Connected": "b290e27f-5acc-4235-aa1e-b2f7f237e539"
  },
  "IndicatorMeshParts": [],
  "MeshPartMaterialOverrides": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockIndicatorDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockIndicatorDefinitionObjectBuilder')
```
