# DummyInteractedEntityProviderAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.DummyInteractedEntityProviderAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Dummy` | Dummy that will be used as a position and normal source for interaction |

## A real one

`Vanilla\Assets\Blocks\Welder\350\Welder350DummyInteractedEntityProviderAdapterDefinition.def`

```json
{
  "Guid": "c5664df6-9225-4ddf-9e89-b6603427c89f",
  "Dummy": "fb621cb9-438c-4141-9751-f4a59196658f"
}
```

Others: `Grinder350DummyInteractedEntityProviderAdapterDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DummyInteractedEntityProviderAdapterDefinitionObjectBuilder')
search_content('', type_contains='DummyInteractedEntityProviderAdapterDefinitionObjectBuilder')
```
