# FloraDebrisDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.FloraDebrisDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxPenetrationDistanceForGravityBoost` | In case a debris cannot be static, this value is the absolute maximum planet voxel penetration distance for the debris to have inverse gravity applied to it |
| `StaticEntityLayer` | What physics entity layer should static fractures be part of |

## A real one

`Vanilla\Assets\System\FractureDebris\FloraDebrisDefinition_Client.def`

```json
{
  "Guid": "d2052fc6-3f47-4a99-9c89-8c44dca5149e",
  "StaticEntityLayer": "Flora"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraDebrisDefinitionObjectBuilder')
search_content('', type_contains='FloraDebrisDefinitionObjectBuilder')
```
