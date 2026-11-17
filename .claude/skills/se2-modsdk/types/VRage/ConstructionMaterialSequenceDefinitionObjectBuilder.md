# ConstructionMaterialSequenceDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.ConstructionMaterialSequenceDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **13**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | The unique name of this material sequence. This is used for automatic mapping when generating build progress models from model metadata. |
| `SolidSequence` | The second sequence of materials to cycle through. All of these should be non-transparent. |
| `TransparentSequence` | The sequence of materials to cycle through during the first build stage, at which the model may render partially transparent parts. |

## A real one

`Vanilla\Assets\System\Configurations\ConstructionPresets\ConstructionMaterialSequenceDefinition_25cm.def`

```json
{
  "Guid": "a2476d57-9aa0-4ceb-9ad3-09b87e965333",
  "Name": "25cm",
  "TransparentSequence": {
    "_data": [
      {
        "Key": "07444d09-45e9-4527-9528-190adec5b57d",
        "Value": "851d4d6e-9ec8-467f-87a5-06ef06e97336"
      }
    ]
  },
  "SolidSequence": {
    "_data": [
      {
        "Key": "406e974e-c8f4-4cf9-bb4f-90898f487ed7",
        "Value": "03a61f23-40d5-48bf-9fed-f9df6540fdf3"
      }
    ]
  }
}
```

Others: `ConstructionMaterialSequenceDefinition_Default`, `ConstructionMaterialSequenceDefinition_Support`

---

Read it with the MCP server rather than by hand:

```
describe_type('ConstructionMaterialSequenceDefinitionObjectBuilder')
search_content('', type_contains='ConstructionMaterialSequenceDefinitionObjectBuilder')
```
