# BlockToolbarNotificationsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar.BlockToolbarNotificationsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GenericFailureNotification` | Notification shown when the action does not activate successfully (for any reason) |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CockpitInputAdapter\CockpitBlockToolbarNotificationsComponentDefinition.def`

```json
{
  "Guid": "ba8954cb-2e24-41da-88aa-70acacb96729",
  "GenericFailureNotification": "d9bf14a7-b54a-4c21-afff-dfbb5d1415fd"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockToolbarNotificationsComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockToolbarNotificationsComponentDefinitionObjectBuilder')
```
