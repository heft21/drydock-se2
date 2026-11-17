# PartialDefinitionDiff

`VRage:Keen.VRage.ContentPipeline.Definitions.PartialDefinitionDiff`

- bundle: **VRage**
- namespace: `Keen.VRage.ContentPipeline.Definitions`
- definitions using it: **10504**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseDefinition` | The definition or partial definition that this partial definition is based on. |

## A real one

`Vanilla\Assets\Blocks\Seat\Seat150.partialdef`

```json
{
  "BaseDefinition": "4c410e15-b5d8-4af3-888a-786d70357387",
  "PartialDefinitionKind": "Copy",
  "Manipulator": {
    "Guid": "310ff4f9-6f4f-4e87-a8d8-8bc39a74fa57",
    "ServerComposite": "45fedc87-d06c-4499-bc06-05a7864a8343",
    "ClientPrefab": "cff45eec-20db-4f4a-9683-77b96bbb69d1"
  },
  "DefinitionType": "VRage:Keen.VRage.Multiplayer.Data.PrefabBindingDefinition",
  "PriorityOverride": false
}
```

Others: `Bed200`, `BaseHandTools`

---

Read it with the MCP server rather than by hand:

```
describe_type('PartialDefinitionDiff')
search_content('', type_contains='PartialDefinitionDiff')
```
