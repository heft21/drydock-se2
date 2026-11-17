# PlanetMaterialDefinition+PlanetMaterialPlacementRuleDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetMaterialDefinition+PlanetMaterialPlacementRuleDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **127**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\EarthLike\Biomes\MaterialMaps\DryRock.def`

```json
{
  "Guid": "28dd8a28-f310-4130-954f-2ec900e0845f",
  "Layers": [
    {
      "Key": "97c031a7-9387-468f-90fc-a0d128355541",
      "Value": {
        "Material": "dd82e401-023d-4fa2-9865-69d9ddb8bb26",
        "Depth": 10
      }
    }
  ],
  "Slope": {
    "Min": 45,
    "Max": 90
  }
}
```

Others: `IceLake`, `RockCliff`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetMaterialDefinition+PlanetMaterialPlacementRuleDefinitionObjectBuilder')
search_content('', type_contains='PlanetMaterialDefinition+PlanetMaterialPlacementRuleDefinitionObjectBuilder')
```
