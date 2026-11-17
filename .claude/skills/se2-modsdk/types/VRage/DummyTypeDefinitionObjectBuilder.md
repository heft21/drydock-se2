# DummyTypeDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Model.DummyTypeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Model`
- definitions using it: **154**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\DummyTypes\Head.def`

```json
{
  "Guid": "2f0f6710-3dc2-4ecb-bcc6-0719ad23bd07"
}
```

Others: `Pump`, `Seat`

---

Read it with the MCP server rather than by hand:

```
describe_type('DummyTypeDefinitionObjectBuilder')
search_content('', type_contains='DummyTypeDefinitionObjectBuilder')
```
