# DecalBudgetConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.DecalBudgetConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Budgets` | List of decal budgets. Corresponds to budget indexes in the decal system. Each group of the projected decals can have its own budget. E.g. Tire marks, shot and explosion marks. |

## A real one

`Engine\Assets\Configurations\Setup\DecalBudgetConfiguration.def`

```json
{
  "Guid": "0414127d-d8d5-4320-ae62-2fc83e6caf65",
  "Budgets": [
    {
      "Key": "5920ce42-594c-4f3b-89fe-d7048f80c23d",
      "Value": {
        "Name": "Infinite",
        "MaxCount": 1000000
      }
    },
    {
      "Key": "236ebdfb-ff41-4234-bf94-30e2423af125",
      "Value": {
        "Name": "Tiny",
        "MaxCount": 1
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalBudgetConfigurationObjectBuilder')
search_content('', type_contains='DecalBudgetConfigurationObjectBuilder')
```
