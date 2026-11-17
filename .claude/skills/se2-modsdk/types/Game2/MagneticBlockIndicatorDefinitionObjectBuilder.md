# MagneticBlockIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.MagneticBlockIndicatorDefinitionObjectBuilder`

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

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MagneticBlockIndicatorDefinition.def`

```json
{
  "Guid": "9b3e4bc1-5ab3-4517-ad9b-b4c421af6183",
  "ReplacementModels": [],
  "DefaultMaterials": {},
  "IndicatorMeshParts": [],
  "MeshPartMaterialOverrides": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MagneticBlockIndicatorDefinitionObjectBuilder')
search_content('', type_contains='MagneticBlockIndicatorDefinitionObjectBuilder')
```
