# TagsToRemoveProcessorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityConfigurators.TagsToRemoveProcessorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityConfigurators`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RemoveByTag` | Collection of components to be removed by their tag |

## A real one

`Vanilla\Assets\System\Configurations\Planets\PlanetTagsToRemoveProcessor.def`

```json
{
  "Guid": "1606735a-03d9-4436-89cc-dd6fc59a4c9d",
  "RemoveByTag": [
    {
      "Key": "3618d9d9-69f9-4685-8070-e2fe1ea7b3b5",
      "Value": "SpherePreviewComponent"
    }
  ]
}
```

Others: `PreviewTagsToRemoveProcessor`

---

Read it with the MCP server rather than by hand:

```
describe_type('TagsToRemoveProcessorDefinitionObjectBuilder')
search_content('', type_contains='TagsToRemoveProcessorDefinitionObjectBuilder')
```
