# PhysicsDebugMaterialsConfigurationObjectBuilder

`VRage:Keen.VRage.Physics.Client.Definitions.PhysicsDebugMaterialsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Client.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BillboardedTriangleListOpaque` | Material for rendering of billboarded opaque Havok geometry |
| `BillboardedTriangleListTransparent` | Material for rendering of billboarded transparent Havok geometry |
| `FilledTriangleListOpaque` | Material for rendering of filled opaque Havok geometry |
| `FilledTriangleListTransparent` | Material for rendering of filled transparent Havok geometry |
| `LineList` | Material for rendering of line debug Havok geometry |
| `WireframeTriangleListOpaque` | Material for rendering of wire opaque Havok geometry |
| `WireframeTriangleListTransparent` | Material for rendering of wire transparent Havok geometry |

## A real one

`Engine\Assets\Configurations\Setup\PhysicsDebugMaterialsConfiguration.def`

```json
{
  "Guid": "0dce04d5-678d-4753-a13a-56faa1671d0f",
  "LineList": "35375d8e-2440-4bbc-bf55-42973e5e89f5",
  "FilledTriangleListOpaque": "a9d156e8-b36c-4c29-8977-5277fb041773",
  "FilledTriangleListTransparent": "aec39835-56bf-423b-9bda-599199dc07cf",
  "WireframeTriangleListOpaque": "6e6b70d2-6df8-4aa2-bd33-901c3f91a4fe",
  "WireframeTriangleListTransparent": "aec39835-56bf-423b-9bda-599199dc07cf",
  "BillboardedTriangleListOpaque": "a9d156e8-b36c-4c29-8977-5277fb041773",
  "BillboardedTriangleListTransparent": "aec39835-56bf-423b-9bda-599199dc07cf"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsDebugMaterialsConfigurationObjectBuilder')
search_content('', type_contains='PhysicsDebugMaterialsConfigurationObjectBuilder')
```
