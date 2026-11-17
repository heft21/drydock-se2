# MapSectorsModelComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.ColonizationMap.MapSectorsModelComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.ColonizationMap`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaterialDefinition` | Base material used to render the colonization map sectors. |

## A real one

`Vanilla\Assets\System\ColonizationMap\MapSectorsModelComponentDefinition.def`

```json
{
  "Guid": "31c4d70b-2657-4fe8-b218-46c726c21e2d",
  "Model": "{G}99ae37fa-1715-423f-abad-65d7d5703d15",
  "Dummies": [],
  "MaterialDefinition": "985dc538-4556-4ef1-a385-45b0b1e3813a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MapSectorsModelComponentDefinitionObjectBuilder')
search_content('', type_contains='MapSectorsModelComponentDefinitionObjectBuilder')
```
