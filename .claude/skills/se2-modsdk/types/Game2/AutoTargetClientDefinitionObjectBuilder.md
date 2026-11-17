# AutoTargetClientDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Weapons.AutoTargetClientDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Weapons`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraModeKey` | Direct control camera mode key |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\AutoTargetClientDefinition.def`

```json
{
  "Guid": "4db9fd0a-1eae-4678-8a7f-319991da0f0d",
  "CameraModeKey": "caee6e17-8a52-416a-9a15-bd593ed8336f"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AutoTargetClientDefinitionObjectBuilder')
search_content('', type_contains='AutoTargetClientDefinitionObjectBuilder')
```
