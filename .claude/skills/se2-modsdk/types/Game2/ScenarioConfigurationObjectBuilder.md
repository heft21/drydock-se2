# ScenarioConfigurationObjectBuilder

`Game2:Keen.Game2.Client.RuntimeSystems.ScenarioConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.RuntimeSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ScenarioEmptyWorld` | Empty world |
| `ScenarioSaveClassicSurvival` | World to load for scenario Classic Survival |
| `ScenarioSaveRedShip` | World to load for scenario Red Ship |
| `ScenarioSaveSurvival` | World to load for scenario Survival |
| `ScenarioSaveSurvivalNoFTUE` | World to load for scenario Survival but from space station |
| `Scenarios` | List of scenarios |

## A real one

`Vanilla\Assets\MainMenuData\Scenarios\ScenarioConfiguration.def`

```json
{
  "Guid": "65f33a58-b3e5-4e92-8dff-77520fdf58ee",
  "ScenarioSaveRedShip": {
    "SaveName": "CRF"
  },
  "ScenarioSaveSurvival": {
    "SaveName": "Survival"
  },
  "ScenarioSaveClassicSurvival": {
    "SaveName": "ClassicSurvival"
  },
  "ScenarioSaveSurvivalNoFTUE": {
    "SaveName": "SurvivalNOFTUE"
  },
  "ScenarioEmptyWorld": {
    "SaveName": "EmptyWorld"
  },
  "Scenarios": [
    {
      "Key": "97cf42cd-fd7c-4ee5-980c-134ab58d3fd9",
      "Value": {
        "Name": "ScenarioNameCRF",
        "Save": {
          "SaveName": "CRF"
        },
        "Description": "ScenarioDescriptionCRF",
        "Author": "KeenSoftwareHouse",
        "Background": "{G}2fe80f7d-3f23-4ca4-8358-f9b114fb33be"
      }
    },
    {
      "Key": "28070e5b-7f7a-4383-b59f-87d3ef58df8f",
      "Value": {
        "Name": "ScenarioNameEmptyWorld",
        "Save": {
          "SaveName": "EmptyWorld"
        },
        "Description": "ScenarioDescriptionEmptyWorld",
        "Author": "KeenSoftwareHouse",
        "Background": "{G}875054e0-1b31-4210-aa86-8b957d64b5a0"
      }
    },
    {
      "Key": "6fe24a9e-3736-41f2-b7a4-f17721fd21de",
      "Value": {
        "Name": "ScenarioNameWTV",
        "Save": {
          "SaveName": "Survival"
        },
        "Description": "ScenarioDescriptionWTV",
        "Author": "KeenSoftwareHouse",
        "Background": "{G}43b8eda8-6f3a-4b6a-909f-b3b0029aee01"
      }
    },
    {
      "Key": "99266ca1-1784-4f20-aa8c-3f852b304f45",
      "Value": {
        "Name": "ScenarioNameNoFTUE",
        "Save": {
          "SaveName": "SurvivalNOFTUE"
        },
        "Description": "NewGameQuickStartDescription",
        "Author": "KeenSoftwareHouse",
        "Background": "{G}9c9077d5-c222-4543-a516-6c478adba9d6"
      }
    },
    {
      "Key": "f3d21f92-e674-4f68-82be-b07517300ea5",
      "Value": {
        "Name": "ScenarioNameCS",
        "Save": {
          "SaveName": "ClassicSurvival"
        },
        "Description": "ScenarioDescriptionCS",
        "Author": "KeenSoftwareHouse",
        "Background": "{G}8e80d5c7-0d70-4f15-93f7-b58bd8aa51d5"
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ScenarioConfigurationObjectBuilder')
search_content('', type_contains='ScenarioConfigurationObjectBuilder')
```
