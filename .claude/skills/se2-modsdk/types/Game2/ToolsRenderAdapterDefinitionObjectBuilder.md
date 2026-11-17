# ToolsRenderAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.ToolsRenderAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FirstPersonToolShadowCasterChildPrefab` | Prefab of a subpart which isn't renderer but casts shadows. Works similar to but is not root |
| `FirstPersonToolShadowCasterPrefab` | Prefab of entity that is spawned on client while in first person. This tool is not visible in main view, however it casts a shadow. |
| `FirstPersonToolShadowCastersLinkPrefab` | Serves as a link between and . If a tool has hierarchy with nodes without - such nodes will be mimicked by instances of this prefab |

## A real one

`Vanilla\Assets\Characters\System\ToolsRenderAdapter.def`

```json
{
  "Guid": "35b3612a-a697-4b16-a8ec-7aa25b4e2b6e",
  "FirstPersonToolShadowCasterPrefab": "439a84c1-717a-4696-9d32-f4e10209096c",
  "FirstPersonToolShadowCastersLinkPrefab": "05c49c22-aec1-46e9-8a87-63e6f8bece3e",
  "FirstPersonToolShadowCasterChildPrefab": "305b453d-97b9-457e-bddb-c88635297ff1"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolsRenderAdapterDefinitionObjectBuilder')
search_content('', type_contains='ToolsRenderAdapterDefinitionObjectBuilder')
```
