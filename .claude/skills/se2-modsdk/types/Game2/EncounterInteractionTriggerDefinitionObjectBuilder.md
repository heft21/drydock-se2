# EncounterInteractionTriggerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.Interactions.EncounterInteractionTriggerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.Interactions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InteractionDistance` | Distance at which the encounter may be interacted by the player and should be turning into manual entity handled by trash removal. |
| `PlayerTriggerTagTypes` | Entity tag that mark the player. |

## A real one

`Vanilla\Assets\Templates\Encounters\BaseDefinitions\SpaceBasedEncounter_EncounterInteractionTriggerDefinition.def`

```json
{
  "Guid": "9c16d801-3e8a-4079-93d8-35d053a4f954",
  "InteractionDistance": 100,
  "PlayerTriggerTagTypes": [
    {
      "Key": "71d534e9-54dd-465f-803a-3af563ae7abd",
      "Value": "Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterComponent"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterInteractionTriggerDefinitionObjectBuilder')
search_content('', type_contains='EncounterInteractionTriggerDefinitionObjectBuilder')
```
