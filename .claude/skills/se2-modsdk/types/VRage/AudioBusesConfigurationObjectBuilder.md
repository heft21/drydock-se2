# AudioBusesConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.AudioBusesConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Engine\Assets\Core\Audio\AudioBusesConfiguration.def`

```json
{
  "Guid": "a3315a70-f5b8-4b1d-87ee-4540a6f373a0",
  "MusicBusPath": "bus:/Music",
  "SfxBusPath": "bus:/SFX",
  "UiBusPath": "bus:/UI",
  "ToolsBusPath": "bus:/SFX/Tools"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioBusesConfigurationObjectBuilder')
search_content('', type_contains='AudioBusesConfigurationObjectBuilder')
```
