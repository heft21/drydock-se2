# DLCDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Services.DLCDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Services`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Id` | Non-platform specific identifier for the DLC, used by |

## A real one

`Vanilla\Assets\MainMenuData\DLC\ModSDKDLC.def`

```json
{
  "Guid": "8c740842-ce15-4295-a678-89f9ae6bc9db",
  "Id": "50320137-3eda-40cb-9028-53b2609b451e"
}
```

Others: `PioneerEditionDLC`, `SpaceEngineersVeteranDLC`

---

Read it with the MCP server rather than by hand:

```
describe_type('DLCDefinitionObjectBuilder')
search_content('', type_contains='DLCDefinitionObjectBuilder')
```
