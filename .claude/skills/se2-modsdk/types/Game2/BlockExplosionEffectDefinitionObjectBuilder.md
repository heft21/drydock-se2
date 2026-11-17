# BlockExplosionEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.BlockExplosionEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\Tanks_BlockExplosionEffectDefinition.def`

```json
{
  "Guid": "44ff4ff4-01be-4a32-82c7-ec434974d552",
  "ExplosionEffects": "e31b7409-8ac5-450e-a041-4df185736ce1"
}
```

Others: `Reactors_BlockExplosionEffectDefinition`, `CargoContainers_BlockExplosionEffectDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockExplosionEffectDefinitionObjectBuilder')
search_content('', type_contains='BlockExplosionEffectDefinitionObjectBuilder')
```
