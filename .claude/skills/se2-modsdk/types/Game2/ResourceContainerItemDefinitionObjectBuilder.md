# ResourceContainerItemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.ResourceContainerItemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxStored` | The maximum amount of resource the item can contain. Use with |
| `Resource` | The resource the item contains. |

## A real one

`Vanilla\Assets\Components\Simple\PowerCell\PowerCellResourceContainerItemDefinition.def`

```json
{
  "Guid": "24208f84-e312-47ea-a5db-44b724d31e50",
  "MaxStored": 180000,
  "Resource": "bcded093-f5c0-4997-af3a-a6fbd853ad66"
}
```

Others: `PowerModule_ResourceContainerItemDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceContainerItemDefinitionObjectBuilder')
search_content('', type_contains='ResourceContainerItemDefinitionObjectBuilder')
```
