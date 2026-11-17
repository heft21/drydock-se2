# ExternalToolOriginProviderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ExternalToolOriginProviderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Tag` | Tag of component that will provide the origin on the tagged entity |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\ExternalToolOriginProviderDefinition.def`

```json
{
  "Guid": "fd0676c8-c034-47b6-a4b2-ec7af7500403",
  "Tag": "ToolOriginProvider"
}
```

Others: `IntegrityToolExactExternalToolOriginProviderDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ExternalToolOriginProviderDefinitionObjectBuilder')
search_content('', type_contains='ExternalToolOriginProviderDefinitionObjectBuilder')
```
