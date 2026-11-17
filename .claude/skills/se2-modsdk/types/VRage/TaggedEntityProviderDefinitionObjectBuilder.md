# TaggedEntityProviderDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.EntityProvider.TaggedEntityProviderDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.EntityProvider`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FallbackTag` | Incase the entity with the first tag is not found, an entity with this tag will be found instead |
| `Tag` | The tag the entity adapter will search for |

## A real one

`Vanilla\Assets\System\Spectator\Spectator_Client_TaggedEntityProviderDefinition.def`

```json
{
  "Guid": "a8c622b1-5c2b-4ecb-9430-bab404f7eabf",
  "Tag": "ToolOrigin",
  "FallbackTag": "ToolOriginFallback"
}
```

Others: `PrefabCharacterToolOrigin_TaggedEntityProviderDefinition`, `OriginEntity_TaggedEntityProviderDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('TaggedEntityProviderDefinitionObjectBuilder')
search_content('', type_contains='TaggedEntityProviderDefinitionObjectBuilder')
```
