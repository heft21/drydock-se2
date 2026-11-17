# DummyHUDMarkerPositionOffsetDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GPS.DummyHUDMarkerPositionOffsetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GPS`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\HUD\GPS\HUDMarkerPositionDefinition.def`

```json
{
  "Guid": "7e6a9cf0-f72e-45c1-a63e-c271f2894697",
  "Dummy": "e6295f9b-77e6-48c5-8f15-9dc3afd840df"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DummyHUDMarkerPositionOffsetDefinitionObjectBuilder')
search_content('', type_contains='DummyHUDMarkerPositionOffsetDefinitionObjectBuilder')
```
