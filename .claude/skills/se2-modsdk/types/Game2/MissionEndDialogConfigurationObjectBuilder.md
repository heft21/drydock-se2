# MissionEndDialogConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Missions.MissionEndDialogConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Missions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FailureDialog` | Dialog that opens when mission fails |

## A real one

`Vanilla\Assets\System\Configurations\MissionEndDialogConfiguration.def`

```json
{
  "Guid": "011bc4ef-8913-44c2-bb48-d4d73cd3d329",
  "FailureDialog": "78c79317-b8cc-4b57-af4c-a0daeda82179"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MissionEndDialogConfigurationObjectBuilder')
search_content('', type_contains='MissionEndDialogConfigurationObjectBuilder')
```
