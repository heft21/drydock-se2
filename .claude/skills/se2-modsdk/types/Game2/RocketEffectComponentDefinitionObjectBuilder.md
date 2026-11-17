# RocketEffectComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.RocketEffectComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CruisingEffect` | Particle Effect to play while the rocket cruises through the air |
| `LaunchEffect` | Particle Effect to spawn when the rocket gets launched |

## A real one

`Vanilla\Assets\CharacterTools\RocketLauncher\RocketLauncherProjectile_Client_RocketEffectComponentDefinition.def`

```json
{
  "Guid": "3afe9020-b8f4-4e8d-afd6-4f4902d5765a",
  "LaunchEffect": {
    "ParticleEffect": "d7039b2f-191e-49c7-bec2-ed7c4d28cd52",
    "Dummy": "9df0b33c-68e2-4168-ad39-888f073b058e",
    "Scale": 1
  },
  "CruisingEffect": {
    "ParticleEffect": "8ef6504b-8e3e-4c21-b798-957b3691929a",
    "Dummy": "9df0b33c-68e2-4168-ad39-888f073b058e",
    "Scale": 1
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RocketEffectComponentDefinitionObjectBuilder')
search_content('', type_contains='RocketEffectComponentDefinitionObjectBuilder')
```
