# PaintToolMaterialSwapperDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.PaintToolMaterialSwapperDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WorkingReplacementsMeshParts` | Collection of Material-Meshpart pairs to be used as replacement for the active paint color |

## A real one

`Vanilla\Assets\CharacterTools\PaintGun\PaintGun_Client_PaintGunMaterialSwapperDefinition.def`

```json
{
  "Guid": "739938d4-8e5e-41ab-977f-4897ce84c7d4",
  "WorkingReplacementsMeshParts": [
    {
      "$Key": "PaintGun_Paint",
      "$Value": "5f7f0ea7-cb67-4098-97a4-033cf96ad01d"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolMaterialSwapperDefinitionObjectBuilder')
search_content('', type_contains='PaintToolMaterialSwapperDefinitionObjectBuilder')
```
