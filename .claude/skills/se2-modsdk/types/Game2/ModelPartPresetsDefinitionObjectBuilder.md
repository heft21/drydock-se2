# ModelPartPresetsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.ModelPartPresetsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RenderPartsChanges` | Specify how the model parts should change for each preset. |

## A real one

`Vanilla\Assets\Characters\System\ModelPresetsMiroslavSokol.def`

```json
{
  "Guid": "34349ab7-8fed-4597-bb5d-3da7e47a3577",
  "RenderPartsChanges": {
    "c3eec452-93ae-4d19-af33-c71ca4c524b1": {
      "HiddenParts": [],
      "OverrideMaterials": [
        {
          "$Key": "MiroslavSokol_HelmetVisor",
          "$Value": "64416872-188e-4919-a258-aedcd80ebc30"
        },
        {
          "$Key": "MiroslavSokol_Helmet",
          "$Value": "64416872-188e-4919-a258-aedcd80ebc30"
        },
        {
          "$Key": "MiroslavSokol_Head",
          "$Value": "64416872-188e-4919-a258-aedcd80ebc30"
        },
        {
          "$Key": "MiroslavSokol_Hair",
          "$Value": "64416872-188e-4919-a258-aedcd80ebc30"
        },
        {
          "$Key": "MiroslavSokol_Eyes",
          "$Value": "64416872-188e-4919-a258-aedcd80ebc30"
        }
      ]
    },
    "cc221cf4-a2ef-4b26-98ba-8c3d81646e08": {
      "HiddenParts": [
        {
          "Key": "604dff53-6b1c-4595-9500-6eddc3180707",
          "Value": "MiroslavSokol_Backpack"
        },
        {
          "Key": "123ba083-c01b-422d-9062-724e7ae376a0",
          "Value": "MiroslavSokol_BackpackLOD2"
        },
        {
          "Key": "ac69319f-7b3f-4485-9fe3-c20b79c4e799",
          "Value": "MiroslavSokol_BackpackLOD3"
        }
      ],
      "OverrideMaterials": []
    }
  }
}
```

Others: `VeteranMale_ModelPartPresetsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ModelPartPresetsDefinitionObjectBuilder')
search_content('', type_contains='ModelPartPresetsDefinitionObjectBuilder')
```
