# CharacterRagdollComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterRagdollComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DeathRagdollEntityLayer` | The entity layer that the ragdoll uses after the character dies. If null, original layer is used. |

## A real one

`Vanilla\Assets\Characters\System\CharacterRagdollComponentDefinition.def`

```json
{
  "Guid": "490581fd-2a00-46b6-8100-0198c1bfcb62",
  "RagdollAsset": "{G}c0ecbec5-ebf9-4bbf-af3e-5d5d8ee07575",
  "EntityLayer": "Ragdolls",
  "RagdollBoneTags": "98ef7258-5e90-460c-b7e0-e791cb099f08",
  "PhysicsMaterial": "ffc8f65b-bc97-45d5-a8dd-a9a6706b671a",
  "MinTeleportVelocity": 350,
  "PoweredMotorsParameters": {
    "MaxForceLowerLimit": 10,
    "MaxForceUpperLimit": 100,
    "TauLowerLimit": 0,
    "TauUpperLimit": 0.05,
    "DampingLowerLimit": 0,
    "DampingUpperLimit": 1.2,
    "ProportionalRecoveryVelocity": 2,
    "ConstantRecoveryVelocity": 0.5,
    "MaxFrictionTorque": 5
  },
  "BlendingDuration": 1666666,
  "PostProjectionSettings": {
    "ShockPropagationFactor": 1,
    "IterationLimit": 8,
    "PositionErrorThreshold": 10000000000.0,
    "AngularErrorThreshold": 3.1415927,
    "PositionalTau": 1,
    "AngularTau": 1,
    "PositionalAlpha": 1,
    "AngularAlpha": 1,
    "MaxMassAndInertiaRatio": 1.8446726e+19,
    "LinearTolerance": 0.05,
    "AngularTolerance": 0.17453
  },
  "DeathRagdollEntityLayer": "DeadRagdolls"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterRagdollComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterRagdollComponentDefinitionObjectBuilder')
```
