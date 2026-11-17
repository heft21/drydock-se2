# CockpitAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit.CockpitAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InsideSnapshot` | Snapshot path of the event that is played when the cockpit is inside |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\CockpitAudioMixerDefinition.def`

```json
{
  "Guid": "58c13a40-cc06-4d50-a12d-8154d3faccc7",
  "InsideSnapshot": "snapshot:/InCockpit"
}
```

Others: `ControllableSeatMixerAudioDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitAudioDefinitionObjectBuilder')
search_content('', type_contains='CockpitAudioDefinitionObjectBuilder')
```
