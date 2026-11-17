# TimerBlockIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar.TimerBlockIndicatorDefinitionObjectBuilder`

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

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Timers_Client_TimerBlockIndicatorDefinition.def`

```json
{
  "Guid": "b5d3aa6e-27bb-4a1d-bd30-9da4aa0aa1b2",
  "ReplacementModels": [],
  "DefaultMaterials": {},
  "IndicatorMeshParts": [],
  "MeshPartMaterialOverrides": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TimerBlockIndicatorDefinitionObjectBuilder')
search_content('', type_contains='TimerBlockIndicatorDefinitionObjectBuilder')
```
