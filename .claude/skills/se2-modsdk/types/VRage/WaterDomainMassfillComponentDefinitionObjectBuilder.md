# WaterDomainMassfillComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.WaterDomainMassfillComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxCells` | The maximum number of cells to fill |
| `Radius` | The maximum radius to fill |

## A real one

`Vanilla\Assets\System\Water\WaterDomain\WaterDomainMassfill.def`

```json
{
  "Guid": "cf3912bf-92e0-4d31-8744-542cf8cde1ca",
  "Radius": 100000,
  "MaxCells": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterDomainMassfillComponentDefinitionObjectBuilder')
search_content('', type_contains='WaterDomainMassfillComponentDefinitionObjectBuilder')
```
