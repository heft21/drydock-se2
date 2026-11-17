# VideoDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.VideoDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Video` | Video asset carried by this definition |

## A real one

`Vanilla\Assets\System\Videos\FTUECutsceneVideoDefinition.def`

```json
{
  "Guid": "a12b702e-5a26-46fb-b586-7e6866b11848",
  "Video": "{G}03bb455c-002a-4db2-a2a3-ea6f1afd6dce"
}
```

Others: `VallationStationCutsceneVideoDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('VideoDefinitionObjectBuilder')
search_content('', type_contains='VideoDefinitionObjectBuilder')
```
