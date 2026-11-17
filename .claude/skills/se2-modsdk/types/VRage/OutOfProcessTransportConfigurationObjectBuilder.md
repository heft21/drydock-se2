# OutOfProcessTransportConfigurationObjectBuilder

`VRage:Keen.VRage.Multiplayer.Transport.OutOfProcess.OutOfProcessTransportConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Multiplayer.Transport.OutOfProcess`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\OutOfProcessTransportConfiguration.def`

```json
{
  "Guid": "9d4d4482-6793-4248-8b58-9e7cc1c1cd7f",
  "ManagementChannel": 0,
  "CommandBuffersChannel": 1,
  "EntityDataChannel": 2,
  "ReplicationChannels": {
    "VRage:Keen.VRage.DCS.Components.Entity": 3
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OutOfProcessTransportConfigurationObjectBuilder')
search_content('', type_contains='OutOfProcessTransportConfigurationObjectBuilder')
```
