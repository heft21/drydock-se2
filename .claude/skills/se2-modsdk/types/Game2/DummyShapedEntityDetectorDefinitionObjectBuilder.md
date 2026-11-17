# DummyShapedEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityDetection.DummyShapedEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityDetection`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DummyShapedEntityDetectorDefinition.def`

```json
{
  "Guid": "bca112ea-f058-441b-bcce-4a1367e1af1a",
  "QueryDummy": "eb7869c7-2636-435b-8b86-bdda145f4737",
  "MaxSeparatingDistance": 0
}
```

Others: `LandingGearDummyShapedEntityDetectorDefinitionLock`, `LandingGearCooldownDummyShapedEntityDetectorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DummyShapedEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='DummyShapedEntityDetectorDefinitionObjectBuilder')
```
