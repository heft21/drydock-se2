# EnabledByStatsDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Stats.EnabledByStatsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Stats`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllStatsRequired` | Determines whether combining one or more stats is done in OR or AND fashion |
| `Stats` | Stats that make given Entity enabled/disabled |

## A real one

`Vanilla\Assets\Characters\System\CharacterHeadlightsEnabledByStatsDefinition.def`

```json
{
  "Guid": "3f6906df-c0ed-4516-80ad-3b10bf04cfd9",
  "Stats": [
    {
      "Key": "4b590971-58d0-4030-9438-50ebc876482a",
      "Value": "b4de981d-1ed7-4603-95c8-e76f6281a928"
    },
    {
      "Key": "ee454eb1-ab66-4d6b-85a8-bbc361eacfb9",
      "Value": "675206d7-7a7a-445c-946c-e0a74bbcd862"
    }
  ],
  "AllStatsRequired": true
}
```

Others: `EnabledByStatsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('EnabledByStatsDefinitionObjectBuilder')
search_content('', type_contains='EnabledByStatsDefinitionObjectBuilder')
```
