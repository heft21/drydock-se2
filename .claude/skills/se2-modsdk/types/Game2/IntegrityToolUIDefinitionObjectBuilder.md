# IntegrityToolUIDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.IntegrityToolUIDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AreaOccupiedError` | Error text to display on client when the area targeted by welder is occupied |
| `CantMaterializeProjectionNotification` | Fallback Notification that will show when can't build, but there is no better reason to give |
| `FloatingObjectDestroyedNotification` | Notification showed when a floating object is destroyed as a result of block materialization |
| `MissingMountPointNotification` | Notification that will show when can't build Block cos there is nothing to attach it to |
| `ModeOverride` | Override of the tool mode used for only the UI. |
| `NotMaterializableOpacity` | Opacity to set when target Block Projection can't be materialized |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\IntegrityToolInputAdapter\WelderToolUIDefinition.def`

```json
{
  "Guid": "674fd817-d996-467b-83d3-8424b6c59ead",
  "AreaOccupiedError": "AreaOccupiedMessage",
  "ModeOverride": null,
  "MissingMountPointNotification": "776d08cc-618a-447c-aefe-20c1bdd93520",
  "CantMaterializeProjectionNotification": "092bc126-c80f-4c5c-ab4e-c974b4d58255",
  "FloatingObjectDestroyedNotification": "4457e44c-b342-4def-9588-aa818965962e",
  "NotMaterializableOpacity": 0.3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('IntegrityToolUIDefinitionObjectBuilder')
search_content('', type_contains='IntegrityToolUIDefinitionObjectBuilder')
```
