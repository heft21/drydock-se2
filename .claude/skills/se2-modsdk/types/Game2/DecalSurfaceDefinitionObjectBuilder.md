# DecalSurfaceDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalSurfaceDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Mapping` | Mapping from to |

## A real one

`Vanilla\Assets\System\Decals\Overrides\MetalDecalOverrideDefinition.def`

```json
{
  "Guid": "958d28a4-5474-4536-b8f1-2e5cb0893497",
  "Mapping": {
    "5c753183-9148-44e0-a1cc-9ac04af229b8": "420d20c2-4052-49da-905d-1dad5ef4ef09",
    "00e7ba7f-a60f-42f5-9b1c-74cc1d6605ef": "4706fcd6-c070-48a6-bbd1-43652c7000cd"
  }
}
```

Others: `DecalOverride_FbxRocks_Definition`, `DefaultVoxelDecalOverrideDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalSurfaceDefinitionObjectBuilder')
search_content('', type_contains='DecalSurfaceDefinitionObjectBuilder')
```
