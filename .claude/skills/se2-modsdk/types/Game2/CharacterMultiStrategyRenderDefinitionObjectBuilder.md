# CharacterMultiStrategyRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterMultiStrategyRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MagneticBootsActiveMaterial` | The material used on the magnetic boots to indicate the boots are on and actively connected to a surface (e.g. green) |
| `MagneticBootsEnabledMaterial` | The material used on the magnetic boots to indicate they are enabled (e.g. yellow) |
| `MagneticBootsIndicatorMeshPartId` | The character mesh part to apply the or to. Set to null to disable this feature. |

## A real one

`Vanilla\Assets\Characters\System\ComponentCharacterMultiStrategyRender.def`

```json
{
  "Guid": "4d37e2ff-2b9a-421f-b6a2-46d13a6bad66",
  "MagneticBootsIndicatorMeshPartId": "MagBootsEnabled",
  "MagneticBootsEnabledMaterial": "0d5995f5-2d89-4c09-b34e-507daeb84cbe",
  "MagneticBootsActiveMaterial": "317b8924-832c-4a23-9607-e0018505946e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMultiStrategyRenderDefinitionObjectBuilder')
search_content('', type_contains='CharacterMultiStrategyRenderDefinitionObjectBuilder')
```
