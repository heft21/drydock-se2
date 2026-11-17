# FloatingObjectPrefabsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FloatingObjectPrefabsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackPrefab` | Floating container for character backpack dropped on death |
| `FallbackPrefab` | Default floating object prefab to use when a no floating object prefab is specified for a given in mapping. |
| `FallbackPrefabByItemType` | Per-item-type fallback floating object prefab |
| `ItemPrefabs` | Maps an item to its corresponding floating object prefab |

## A real one

`Vanilla\Assets\System\Configurations\FloatingObjectPrefabsConfiguration.def`

Too large to inline. Fields present:

`BackpackPrefab`, `FallbackPrefab`, `FallbackPrefabByItemType`, `Guid`, `ItemPrefabs`

---

Read it with the MCP server rather than by hand:

```
describe_type('FloatingObjectPrefabsConfigurationObjectBuilder')
search_content('', type_contains='FloatingObjectPrefabsConfigurationObjectBuilder')
```
