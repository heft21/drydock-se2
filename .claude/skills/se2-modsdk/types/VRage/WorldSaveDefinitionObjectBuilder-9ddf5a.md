# WorldSaveDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Worlds.WorldSaveDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Worlds`
- definitions using it: **135**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `World` | Identifier of a world save. |

## A real one

`Vanilla\Assets\Procedural\VS4_0\Space\Encounters\NPCDemo\NPCDemoWorldSaveDefinition.def`

```json
{
  "Guid": "21234133-d890-48d2-ade7-e861d52a4719",
  "World": {
    "SaveName": "SpaceEncounter_NPCDemo"
  }
}
```

Others: `Bounty8_WorldSaveDefinition`, `Bounty9_WorldSaveDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('WorldSaveDefinitionObjectBuilder')
search_content('', type_contains='WorldSaveDefinitionObjectBuilder')
```
