# FloraEntityEffectsDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Components.FloraEntityEffectsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnDestroyedParticles` | Particles to play when the flora entity is destroyed |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\FloraEntityEffectsDefinition.def`

```json
{
  "Guid": "89ffc50d-d53d-45f0-b23c-db5c17bb50f4",
  "OnDestroyedParticles": "e61030fb-5c3f-4e40-8711-961901240e04"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraEntityEffectsDefinitionObjectBuilder')
search_content('', type_contains='FloraEntityEffectsDefinitionObjectBuilder')
```
