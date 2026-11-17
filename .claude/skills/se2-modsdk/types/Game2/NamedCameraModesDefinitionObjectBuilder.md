# NamedCameraModesDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.NamedCameraModesDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `NamedCameraModes` | Pairs named camera mode key to its prefab (e.g. ) |

## A real one

`Vanilla\Assets\System\Controller\NamedCameraPrefabs\GridNamedCameraModesDefinition.def`

```json
{
  "Guid": "c925f4e4-c750-442b-8fd7-71bb97188dc6",
  "NamedCameraModes": {
    "443536e7-6513-4fbd-a77b-9fbfa9ab9ca4": "4cf1a60f-4d91-4efc-9ac1-433916ccd9b5",
    "104cf078-21fa-41a8-a28a-022132fdef37": "7b8e4a27-bbe5-45a9-9c17-0ea68620785b",
    "5224bace-25bd-4808-8f9f-68cea53b1d94": "36ff3343-ad75-444c-a69b-555ea0e5f913",
    "caee6e17-8a52-416a-9a15-bd593ed8336f": "abebac26-b026-412f-b22b-47fdc89e0ef4"
  }
}
```

Others: `CharacterNamedCameraModesDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('NamedCameraModesDefinitionObjectBuilder')
search_content('', type_contains='NamedCameraModesDefinitionObjectBuilder')
```
