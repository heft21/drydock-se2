# MinimumHardwareRequirementsConfigurationObjectBuilder

`VRage:Keen.VRage.Core.Definitions.MinimumHardwareRequirementsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ClockSpeedCPU` | Minimum clock speed of the CPU |
| `MainMemoryBytes` | Minimum amount of RAM |
| `MinCoreCount` | Minumum CPU core count |
| `TeraFlopsGPU` | Minimum amount GPU TeraFlops |
| `VideoMemoryBytes` | Minimum amount of VRAM |

## A real one

`Engine\Assets\Core\DefaultMinimumHardwareRequirementsConfiguration.def`

```json
{
  "Guid": "894d193e-5f3b-4ebf-a172-3a659f721438",
  "MainMemoryBytes": 0,
  "VideoMemoryBytes": 0,
  "TeraFlopsGPU": 0,
  "ClockSpeedCPU": 0,
  "MinCoreCount": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MinimumHardwareRequirementsConfigurationObjectBuilder')
search_content('', type_contains='MinimumHardwareRequirementsConfigurationObjectBuilder')
```
