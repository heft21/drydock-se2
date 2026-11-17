# AntennaDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Antennas.AntennaDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Antennas`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HUDMarker` | HUD marker used. When null, no marker will be shown |
| `MaxBroadcastRange` | Distance around the entity that the message will be visible/connections will be made |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\AntennaDefinition.def`

```json
{
  "Guid": "eec6401d-8e51-44d9-9d77-423d64cee4e0",
  "HUDMarker": "e24c6ba6-061d-4ebc-80c2-66b20c43db0b",
  "MaxBroadcastRange": 10000
}
```

Others: `PrefabCharacter_AntennaDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AntennaDefinitionObjectBuilder')
search_content('', type_contains='AntennaDefinitionObjectBuilder')
```
