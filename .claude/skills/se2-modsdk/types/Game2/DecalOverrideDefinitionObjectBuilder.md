# DecalOverrideDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Decals.DecalOverrideDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Decals`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Decals\Overrides\GlassDecalOverrideDefinition.def`

```json
{
  "Guid": "ad803b2d-70ef-4810-ba76-6b3b378f5d5f",
  "Mapping": {
    "5c753183-9148-44e0-a1cc-9ac04af229b8": "374c389d-a44e-4864-81a0-5174166554da"
  }
}
```

Others: `DarkPlasticDecalOverrideDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalOverrideDefinitionObjectBuilder')
search_content('', type_contains='DecalOverrideDefinitionObjectBuilder')
```
