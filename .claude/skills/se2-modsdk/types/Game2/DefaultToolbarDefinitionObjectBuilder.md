# DefaultToolbarDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Toolbars.DefaultToolbarDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Toolbars`
- definitions using it: **1**

## What it is

Object builder for the PlayerToolbarServerConfigurationObjectBuilder, required to convert the serialized List-of-List to ImmutableArray

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\PlayerToolbarServerConfiguration_DefaultToolbarDefinition.def`

Too large to inline. Fields present:

`Guid`, `Tiles`

---

Read it with the MCP server rather than by hand:

```
describe_type('DefaultToolbarDefinitionObjectBuilder')
search_content('', type_contains='DefaultToolbarDefinitionObjectBuilder')
```
