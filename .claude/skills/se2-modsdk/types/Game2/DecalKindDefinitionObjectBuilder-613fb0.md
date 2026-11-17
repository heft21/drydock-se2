# DecalKindDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Decals.DecalKindDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Decals`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Decals\DrillDecalKind.def`

```json
{
  "Guid": "00e7ba7f-a60f-42f5-9b1c-74cc1d6605ef",
  "DefaultValue": null
}
```

Others: `BulletHitDecalKind`, `ExplosionDecalKind`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalKindDefinitionObjectBuilder')
search_content('', type_contains='DecalKindDefinitionObjectBuilder')
```
