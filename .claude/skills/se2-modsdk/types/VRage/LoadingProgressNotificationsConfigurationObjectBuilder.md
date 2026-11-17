# LoadingProgressNotificationsConfigurationObjectBuilder

`VRage:Keen.VRage.Core.CoreConfigurations.LoadingProgressNotificationsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.CoreConfigurations`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Engine\Assets\Configurations\Setup\LoadingProgressNotificationsConfiguration.def`

```json
{
  "Guid": "dfa5401d-1176-41da-a22a-393d67c6336f",
  "InitializingRendererMessage": "Initializing renderer",
  "ProcessingDefinitionsMessage": "Processing definitions",
  "CompilingPSOsMessage": "Compiling shaders",
  "CompilingRayTracingPSOsMessage": "Compiling raytracing shaders",
  "LoadingTexturesMessage": "Loading textures"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LoadingProgressNotificationsConfigurationObjectBuilder')
search_content('', type_contains='LoadingProgressNotificationsConfigurationObjectBuilder')
```
