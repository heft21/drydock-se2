# ContactCollectorDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Systems.ContactCollectorDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Systems`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HandleAllContacts` | When true this collector blocks other contact collectors from also handling the same contacts. |
| `ImpulseThreshold` | Minimum impulse for contact propagation. |
| `VelocityDifferenceThreshold` | Minimum absolute velocity difference for contact propagation. |

## A real one

`Vanilla\Assets\System\Grid\Grid_Client_ContactCollectorDefinition.def`

```json
{
  "Guid": "2cf247e6-2077-4e24-a816-dbd8aa4e2c1e",
  "ImpulseThreshold": 30,
  "VelocityDifferenceThreshold": 0.1
}
```

Others: `PrefabCharacterServer_ContactCollectorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ContactCollectorDefinitionObjectBuilder')
search_content('', type_contains='ContactCollectorDefinitionObjectBuilder')
```
