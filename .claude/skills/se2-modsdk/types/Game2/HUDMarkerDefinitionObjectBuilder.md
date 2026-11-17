# HUDMarkerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GPS.HUDMarkerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GPS`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\AntennaHUDMarker.def`

```json
{
  "Guid": "e24c6ba6-061d-4ebc-80c2-66b20c43db0b",
  "Type": "d648e558-2e34-4b80-9d58-5bd678c4db18",
  "Icon": "{G}c6b1e572-cf52-4d4e-bf43-01f814816709",
  "Color": {
    "PackedValue": 4283472718
  }
}
```

Others: `BlockHUDMarkerDefinition`, `ContractMarkerTrackerConfiguration_HUDMarkerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('HUDMarkerDefinitionObjectBuilder')
search_content('', type_contains='HUDMarkerDefinitionObjectBuilder')
```
