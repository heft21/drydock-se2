# IntegrityToolDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.IntegrityToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivationDelay` | Amount of time the tool should be active before it starts working |
| `AllowParentTarget` | Whether it is possible for the tool to affect its parent. For block tools it means whether it can affect other blocks on the grid. |
| `CanAffectProjections` | Can the tool interact with projections? |
| `CanDeformBones` | Can the tool affect block's bone-based deformation? |
| `IntegrityChange` | Multiplies with to make final speed |
| `IntegrityChangeFrequency` | How often the integrity changes will be happening (in frames) |
| `IsAreaTool` | Should tool apply effect in area |
| `MaxInteractionDistance` | How far can the tool reach. Measured from Tool center to interaction point. |
| `ReactivationDelay` | Amount of time the tool to start working again after switching to a new block with the tool already active |

## A real one

`Vanilla\Assets\Blocks\Welder\350\Welder350IntegrityToolDefinition.def`

```json
{
  "Guid": "313efe73-d976-4a6e-bf5e-dfb2bd4088f8",
  "IntegrityChange": 1,
  "CanDeformBones": true,
  "CanAffectProjections": true,
  "MaxInteractionDistance": 100,
  "ActivationDelay": 0,
  "ReactivationDelay": 0,
  "IsAreaTool": true,
  "AllowParentTarget": true,
  "IntegrityChangeFrequency": 10
}
```

Others: `Welder400IntegrityToolDefinition`, `Grinder350IntegrityToolDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('IntegrityToolDefinitionObjectBuilder')
search_content('', type_contains='IntegrityToolDefinitionObjectBuilder')
```
