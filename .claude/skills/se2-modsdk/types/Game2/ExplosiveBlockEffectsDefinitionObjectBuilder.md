# ExplosiveBlockEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Weapons.ExplosiveBlockEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Weapons`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Armed` | Effects when the block is armed |
| `Disarmed` | Effects when the block is disarmed |

## A real one

`Vanilla\Assets\Blocks\Warheads\50\Warhead50_Client_ExplosiveBlockEffectsDefinition.def`

```json
{
  "Guid": "41c5d031-7647-4330-aaef-c8dd3620f3b6",
  "ExplosionEffects": "1a1c74a8-a7b7-4178-b0e9-afdb49cd24a4",
  "Disarmed": {
    "PlayRigidAnimations": false,
    "Effects": "7ee8eb53-7a4b-4eff-81ca-e1e4f60c96a8"
  },
  "Armed": {
    "PlayRigidAnimations": true,
    "Effects": "258e34ee-2a63-4ccd-853e-4b40074782b6"
  }
}
```

Others: `Warhead250_Client_ExplosiveBlockEffectsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ExplosiveBlockEffectsDefinitionObjectBuilder')
search_content('', type_contains='ExplosiveBlockEffectsDefinitionObjectBuilder')
```
