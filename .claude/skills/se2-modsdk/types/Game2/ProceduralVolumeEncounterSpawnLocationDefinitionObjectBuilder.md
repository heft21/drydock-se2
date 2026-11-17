# ProceduralVolumeEncounterSpawnLocationDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.ProceduralVolumeEncounterSpawnLocationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxFieldDistance` | Maximum distance to consider when searching for nearby fields to match the encounter. |
| `MaxSpawnDistance` | Maximum distance at which the encounter will attempt to spawn. If the algorithm gives up - it can spawn further away but it will try to be as close as possible. |
| `Target` | Used to target specific areas in the world that are marked with a contract target. If set the > is ignored and the closest tagged area be taken instead. The > is still respected. |

## A real one

`Vanilla\Assets\Templates\Contracts\BaseDefinitions\ProceduralVolumeEncounterSpawnLocationDefinition.def`

```json
{
  "Guid": "f04204a3-a0b4-4644-9546-00bea79b62d1",
  "Locations": [
    {
      "Key": "89085bcf-09b1-4668-ad3f-ecf63c8f0c95",
      "Value": "LocationSpace"
    }
  ],
  "MaxFieldDistance": 10000,
  "MaxSpawnDistance": 40000
}
```

Others: `SpaceVerdureIndustrialFootHold_ProceduralVolumeEncounterSpawnLocationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProceduralVolumeEncounterSpawnLocationDefinitionObjectBuilder')
search_content('', type_contains='ProceduralVolumeEncounterSpawnLocationDefinitionObjectBuilder')
```
