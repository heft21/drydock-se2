# GravitySetDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.Gravity.GravitySetDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.Gravity`
- definitions using it: **11**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GravityTypes` | List of the the different gravity types that can affect the entity |

## A real one

`Vanilla\Assets\System\Grid\GridAffectedByGravity.def`

```json
{
  "Guid": "50a299de-baac-4fcc-a917-106e22eb53a4",
  "GravityTypes": [
    {
      "Key": "428e852b-5512-4033-be08-01bb2850ca4d",
      "Value": "5e06c1f9-3087-4611-b075-3188a6785d95"
    }
  ]
}
```

Others: `FloatingObjectAffectedByGravity`, `DeathRagdollGravitySet`

---

Read it with the MCP server rather than by hand:

```
describe_type('GravitySetDefinitionObjectBuilder')
search_content('', type_contains='GravitySetDefinitionObjectBuilder')
```
