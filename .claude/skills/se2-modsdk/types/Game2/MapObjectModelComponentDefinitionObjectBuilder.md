# MapObjectModelComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.ColonizationMap.MapObjectModelComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.ColonizationMap`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ParticleEffects` | Optional list of particle effects attached to the map object |

## A real one

`Vanilla\Assets\Templates\ColonizationMap\MapObjectModelComponentDefinition.def`

```json
{
  "Guid": "4c39dab4-5b53-443e-816e-0ed91ced3f04",
  "Model": "{G}cb345be6-fa58-4001-843b-bc2100fe4e37",
  "Dummies": [],
  "ParticleEffects": null
}
```

Others: `PalatineMapVisualPrefab_MapObjectModelComponentDefinition`, `Geomeles_ColonizationMapPlanetVisual_MapObjectModelComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MapObjectModelComponentDefinitionObjectBuilder')
search_content('', type_contains='MapObjectModelComponentDefinitionObjectBuilder')
```
