# ParticleEffectGravityProbeDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Components.ParticleEffectGravityProbeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GravityType` | Type of gravity that affects the probe |
| `SizeOfGravityProbe` | Type of gravity that affects the probe |

## A real one

`Vanilla\Assets\System\Configurations\Effects\ParticleEffectGravityProbe_Client_ParticleEffectGravityProbeDefinition.def`

```json
{
  "Guid": "40773f2e-1445-489a-98f2-b32d5c83401e",
  "GravityType": "6290b4c6-99f6-42dd-9425-bcd72170e6bc",
  "SizeOfGravityProbe": 0.5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectGravityProbeDefinitionObjectBuilder')
search_content('', type_contains='ParticleEffectGravityProbeDefinitionObjectBuilder')
```
