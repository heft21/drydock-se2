# UserMessageConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.UserMessages.UserMessageConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.UserMessages`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `UserMessageFanfare` | Configurable fanfare that will be displaying fanfare messages. |

## A real one

`Vanilla\Assets\System\Configurations\UserMessageConfiguration.def`

```json
{
  "Guid": "9bd4ce7d-ac3d-40e8-9464-9cfb3edfb8dd",
  "UserMessageFanfare": "2c7dfcb6-aa00-4fcf-bede-693c0d565b1a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UserMessageConfigurationObjectBuilder')
search_content('', type_contains='UserMessageConfigurationObjectBuilder')
```
