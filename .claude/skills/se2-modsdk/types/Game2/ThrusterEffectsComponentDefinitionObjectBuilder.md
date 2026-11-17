# ThrusterEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.ThrusterEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FlameLength` | Length of thruster flame |
| `FlameRandomScale` | Random scaling for the flame length |
| `OnLandingParticleEffect` | Particle Effect to spawn when the block is landing |
| `OnThrustPoweredParticleEffect` | Particle Effect to spawn when the block is destroyed |
| `ThrustDummyType` | Specify the dummy to use as the thrust origin on the model |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\HydrogenThrusterEffectsComponent.def`

```json
{
  "Guid": "b06a9718-593b-4914-9986-48a6fd97aecd",
  "FlameLength": 2.5,
  "FlameRandomScale": 0,
  "ThrustDummyType": "051438a6-39b9-42bb-b34c-7c836e9fb7a8",
  "OnThrustPoweredParticleEffect": null,
  "OnLandingParticleEffect": "bdb84f6b-e365-49e2-a874-3a03f11ff555"
}
```

Others: `IonThruster100_ThrusterEffectsComponentDefinition`, `IonThruster150_ThrusterEffectsComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ThrusterEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='ThrusterEffectsComponentDefinitionObjectBuilder')
```
