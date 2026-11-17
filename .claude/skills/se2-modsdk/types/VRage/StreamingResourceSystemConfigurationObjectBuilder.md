# StreamingResourceSystemConfigurationObjectBuilder

`VRage:Keen.VRage.Core.StreamingResources.StreamingResourceSystemConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.StreamingResources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MainMemoryBudget` | Default budget for main system memory. |
| `Subsystems` | Complete map of resource subsystems to their memory definitions. |

## A real one

`Engine\Assets\Configurations\Setup\StreamingResourceSystemConfiguration.def`

```json
{
  "Guid": "3de10ef2-8766-4afa-872c-fbba4324a4d1",
  "Subsystems": {
    "AnimationResourcesSubsystem": {
      "MinimumBudget": {
        "MainMemory": 0,
        "GraphicsMemory": 0
      },
      "ExcessBudgetWeight": {
        "MainMemory": 1,
        "GraphicsMemory": 0
      }
    },
    "Textures": {
      "MinimumBudget": {
        "MainMemory": 0,
        "GraphicsMemory": 0
      },
      "ExcessBudgetWeight": {
        "MainMemory": 0,
        "GraphicsMemory": 1
      }
    },
    "OctreeRegionSubSystem": {
      "MinimumBudget": {
        "MainMemory": 0,
        "GraphicsMemory": 0
      },
      "ExcessBudgetWeight": {
        "MainMemory": 1,
        "GraphicsMemory": 0
      }
    },
    "PlanetBitmapSubSystem": {
      "MinimumBudget": {
        "MainMemory": 0,
        "GraphicsMemory": 0
      },
      "ExcessBudgetWeight": {
        "MainMemory": 1,
        "GraphicsMemory": 0
      }
    },
    "PlanetCubemapSubSystem": {
      "MinimumBudget": {
        "MainMemory": 0,
        "GraphicsMemory": 0
      },
      "ExcessBudgetWeight": {
        "MainMemory": 1,
        "GraphicsMemory": 0
      }
    }
  },
  "MainMemoryBudget": {
    "MinimumBudget": 1073741824,
    "ExtraSystemMemoryRatio": 0.0625
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('StreamingResourceSystemConfigurationObjectBuilder')
search_content('', type_contains='StreamingResourceSystemConfigurationObjectBuilder')
```
