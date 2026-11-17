# PhysicsMaterialAdvancedDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.PhysicsMaterialAdvancedDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FrictionCombinePolicy` | Determines how friction values from two colliding materials are combined. Affects how sliding resistance is calculated during collisions. |
| `MassChangerCategory` | Determines how the material's mass is scaled upon impact to adjust its influence on the colliding body. Setting this value to disables scaling. |
| `MassChangerHeavyObjectFactor` | A factor used to scale the material's mass property. Only applied if the is set to . |
| `MaxImpulse` | The maximum impulse allowed on contacts per sub-step. Impulses exceeding this value will be clipped, and the excess reported via . |
| `RestitutionCombinePolicy` | Determines how restitution values from two colliding materials are combined. Affects how energy absorption is calculated during collisions. |
| `WeldingTolerance` | Tolerance for smoothing internal edge collisions, such as steps or misaligned triangles in landscapes. Effective only when the body quality supports welding (e.g., characters). Higher tolerance reduces sensitivity to small vertical differences but may decrease precision. Note: The final welding tolerance depends on other body materials and collider settings. Cannot exceed the maximum allowed penetration for the collider. |

## A real one

`Vanilla\Assets\Characters\System\CharacterPhysicsMaterialInAir.def`

```json
{
  "Guid": "661e0887-54b7-42d2-8b71-d24534e57576",
  "StaticFriction": 0,
  "DynamicFriction": 0,
  "Restitution": 0.15,
  "MaxImpulse": 7.922816e+27,
  "WeldingTolerance": 0.1,
  "MassChangerHeavyObjectFactor": 3.4028235e+38,
  "RestitutionCombinePolicy": "GeometricMean",
  "FrictionCombinePolicy": "Min",
  "MassChangerCategory": "Heavy"
}
```

Others: `CharacterPhysicsMaterialAdvanced`, `DebrisPhysicsMaterialAdvancedDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsMaterialAdvancedDefinitionObjectBuilder')
search_content('', type_contains='PhysicsMaterialAdvancedDefinitionObjectBuilder')
```
