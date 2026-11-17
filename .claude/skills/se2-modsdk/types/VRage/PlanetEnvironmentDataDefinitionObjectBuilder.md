# PlanetEnvironmentDataDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.PlanetEnvironmentDataDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **12**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SurfaceEnvironments` | A list of environment details for the planet's surface biomes. |
| `UndergroundEnvironments` | A list of environment details for the planet's underground biomes. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\EnvironmentData.def`

```json
{
  "Guid": "30798a88-bcd1-4e2f-91cc-3ae6cbe07023",
  "SurfaceEnvironments": [
    {
      "Key": "2ebca57e-d78f-4a28-9e09-8079c1234b69",
      "Value": "331742ae-28e3-424e-a1c3-c27c2a17a8f9"
    },
    {
      "Key": "220c3b17-d241-49ec-8f29-dd55b5fc207a",
      "Value": "009d9914-a316-4d77-af54-a5cf63142c01"
    }
  ],
  "UndergroundEnvironments": []
}
```

Others: `Kemik_SpawnDataDefinition`, `ByblosSpawnDataDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetEnvironmentDataDefinitionObjectBuilder')
search_content('', type_contains='PlanetEnvironmentDataDefinitionObjectBuilder')
```
