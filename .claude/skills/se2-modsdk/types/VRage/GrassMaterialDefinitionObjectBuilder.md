# GrassMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.GrassMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **26**

## What it is

Builder for the Grass

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BillboardEntries` | Billboards used when rendering grass. Picked randomly to have some variation. |
| `Density` | The density of grass in instance count per sq meter. |
| `MaxInclination` | Inclination factor that affects how much the billboard instance is randomly bend towards the terrain. Helps to break the pattern, as without this billboards just use the terrain normal; |

## A real one

`Vanilla\Assets\Environment\Foliage\Underwater\Corals.def`

```json
{
  "Guid": "6a046dcc-0a83-44b6-8f20-3c301a474640",
  "Density": 3,
  "BillboardEntries": [
    {
      "Key": "03e4aaf0-aa50-460d-9dd6-776f719abc4c",
      "Value": {
        "GrassBillboard": "6ca800a3-bb70-4116-9a6b-b41ebfdd335e",
        "Probability": 0.6,
        "ClusterTexture": null,
        "TextureScale": 100,
        "TexturePower": 1,
        "MinClusterHeightFactor": 0,
        "Width": 0.68,
        "Height": 0.68,
        "WidthVariation": 0.6,
        "HeightVariation": 0.6
      }
    },
    {
      "Key": "6e7c0d4a-30a8-489b-8085-8de35a4cfd72",
      "Value": {
        "GrassBillboard": "938eb21a-5f6f-4a7e-b68e-bb3efd4f9088",
        "Probability": 0.13,
        "ClusterTexture": null,
        "TextureScale": 100,
        "TexturePower": 1,
        "MinClusterHeightFactor": 0,
        "Width": 0.7,
        "Height": 0.7,
        "WidthVariation": 0.7,
        "HeightVariation": 0.7
      }
    },
    {
      "Key": "cd7c1011-9b66-4dce-9adf-8dd6de570345",
      "Value": {
        "GrassBillboard": "c3144c07-fbb5-402f-8a53-f03fab6622fd",
        "Probability": 0.13,
        "ClusterTexture": null,
        "TextureScale": 100,
        "TexturePower": 1,
        "MinClusterHeightFactor": 0,
        "Width": 0.7,
        "Height": 0.7,
        "WidthVariation": 0.7,
        "HeightVariation": 0.7
      }
    },
    {
      "Key": "5c3eed5a-6312-402a-925b-6c2666341a33",
      "Value": {
        "GrassBillboard": "a1166118-7340-48cc-b93e-412380984532",
        "Probability": 0.18,
        "ClusterTexture": null,
        "TextureScale": 100,
        "TexturePower": 1,
        "MinClusterHeightFactor": 0,
        "Width": 0.7,
        "Height": 0.6,
        "WidthVariation": 0.45,
        "HeightVariation": 0.45
      }
    }
  ],
  "MaxInclination": 0.4
}
```

Others: `Seabed`, `Corals2`

---

Read it with the MCP server rather than by hand:

```
describe_type('GrassMaterialDefinitionObjectBuilder')
search_content('', type_contains='GrassMaterialDefinitionObjectBuilder')
```
