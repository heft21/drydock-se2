# GravityGeneratorConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Terminal.ControlPanel.BlockDetails.GravityGeneratorConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Terminal.ControlPanel.BlockDetails`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CylinderRadiusKey` | Represents a localization key for cylinder radius |
| `CylinderShapeDownKey` | Represents a localization key for cylinder shape down |
| `CylinderShapeUpKey` | Represents a localization key for cylinder shape up |
| `FieldKey` | Represents a localization key for field |
| `SphericalKey` | Represents a localization key for spherical |

## A real one

`Vanilla\Assets\UI\GravityGeneratorConfiguration.def`

```json
{
  "Guid": "806378d5-0352-4d74-b3db-238e8a42e1e6",
  "FieldKey": "TerminalScreenGravityGeneratorFieldGravityShapeFieldExtension",
  "CylinderRadiusKey": "TerminalScreenGravityGeneratorCylinderGravityShapeRadius",
  "CylinderShapeUpKey": "TerminalScreenGravityGeneratorCylinderGravityShapeUpExtension",
  "CylinderShapeDownKey": "TerminalScreenGravityGeneratorCylinderGravityShapeDownExtension",
  "SphericalKey": "TerminalScreenGravityGeneratorSphereGravityShapeRadius"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GravityGeneratorConfigurationObjectBuilder')
search_content('', type_contains='GravityGeneratorConfigurationObjectBuilder')
```
