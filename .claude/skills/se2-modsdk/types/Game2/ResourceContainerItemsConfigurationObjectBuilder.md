# ResourceContainerItemsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.ResourceContainers.ResourceContainerItemsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items.ResourceContainers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Containers` | Pairs an item to its corresponding |

## A real one

`Vanilla\Assets\System\Configurations\ResourceContainerItemsConfiguration.def`

```json
{
  "Guid": "a05180d2-b76b-40e6-a5e9-cba490f823a1",
  "Containers": {
    "089240e7-2ad9-4ec9-adef-cceeda83666e": "24208f84-e312-47ea-a5db-44b724d31e50",
    "c8f857ea-30eb-44bd-82bc-9957d764a38e": "45fb8976-e943-454b-b73b-ff16adaa7338"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceContainerItemsConfigurationObjectBuilder')
search_content('', type_contains='ResourceContainerItemsConfigurationObjectBuilder')
```
