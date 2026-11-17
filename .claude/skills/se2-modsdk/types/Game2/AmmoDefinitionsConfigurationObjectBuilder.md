# AmmoDefinitionsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.AmmoDefinitionsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmmoTypes` | Pairs an item to its corresponding ammo type/definition Multiple items can source the same ammo type. |

## A real one

`Vanilla\Assets\System\Configurations\AmmoDefinitionsConfiguration.def`

```json
{
  "Guid": "07ee91a5-d57d-420e-a5e2-7c912cc26120",
  "AmmoTypes": {
    "a74caed5-d6ff-4b3d-9c6b-2f55bfb16c31": "5ef0ffbc-21f9-4aa3-a0ed-b1b97174c071",
    "248b2687-a9c6-4806-8c55-d0fe4ba65784": "158ea0f6-0466-4570-8e4a-8bc1f4e7f6be",
    "64ceb520-d2f0-433f-88fa-5ddc900b5f60": "c95b8a8b-4741-4147-99ad-2a8f4b500a05",
    "00bbce06-a2f3-4ab4-96ed-cb29e76f94ba": "d3bb4ae0-ee27-4aca-8923-139e5806f445",
    "a18c2657-c527-4c67-8b9c-8e18928b2e01": "06a03753-0c79-4f2a-9b81-aa695cce29be"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AmmoDefinitionsConfigurationObjectBuilder')
search_content('', type_contains='AmmoDefinitionsConfigurationObjectBuilder')
```
