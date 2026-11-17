# ProceduralGenerationDataDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.ProceduralGeneration.ProceduralGenerationDataDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.ProceduralGeneration`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EllipsoidFields` | A list of all ellipsoid fields that can be procedurally generated. |
| `Encounters` | Contains setup for possible encounters that can appear in space. |
| `InfiniteArea` | Defines a list of entities that can be procedurally spawned without spatial constraints. These entities are valid candidates for spawning throughout the entire space. |
| `MaxEntitiesPerSector` | Determines how many points will be sampled in a sector to try and find suitable spawn positions for the entities. Note: This is the upper limit for the number of procedural entities a single sector can have. Actual amount of spawned entities depends on the density settings for the volume inside the sector. |
| `ProceduralEntityConfigurator` | An optional entity configurator prefab. Enhances the procedural generation system by adding variation to generated entities. The effect on a procedural entity depends on its type and the configurator's setup. Example: Adding a `ProceduralVoxelStorageRandomSeedProcessorComponent` to the configurator enables each procedural asteroid to be assigned a unique random seed, creating variation. Without the configurator or that processor, all procedural asteroids would share the same seed. |
| `ProceduralEntitySizeEstimator` | An optional entity size estimator prefab. Enhances the procedural generation system by providing the ability to estimate collision sizes for procedural candidates. |
| `ProceduralFieldsDensity` | The target number of ellipsoid fields to spawn, if conditions allow for it. IMPORTANT: The value is expressed in fields per cubic megameter. |
| `VolumeSampleFactorMultiplier` | The maximum samples in each sector will be increased by this value when the sector overlaps a volume. This is to make sure that the sample number can accomodate volumes that are smaller than a sector in some dimensions. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\ProceduralGenerationDataDefinition-2-0.def`

```json
{
  "Guid": "02ccaa2d-1648-4d7e-a1f8-e472ba09d5bf",
  "InfiniteArea": "82da5c8f-3871-4ef6-bb33-c539b5539e9d",
  "MaxEntitiesPerSector": 8,
  "VolumeSampleFactorMultiplier": 1,
  "ProceduralFieldsDensity": 2,
  "EllipsoidFields": [
    {
      "Key": "0b02baee-7fb3-4a24-bdcf-f210dc228536",
      "Value": {
        "Probability": 1,
        "MinRadii": {
          "X": 20,
          "Y": 20,
          "Z": 20
        },
        "MaxRadii": {
          "X": 50,
          "Y": 50,
          "Z": 50
        },
        "Definition": "89005723-ccc6-4cc1-a687-05b10d2a30c4"
      }
    }
  ],
  "Encounters": "680501d2-bc43-417c-8f49-0ab209e3a982",
  "ProceduralEntityConfigurator": "dfadcada-34f4-49e4-a9ee-ff3bd623579a",
  "ProceduralEntitySizeEstimator": "7360c2ee-d629-4798-a00c-21730bc867ac"
}
```

Others: `ProceduralGenerationDataDefinition-1-5`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProceduralGenerationDataDefinitionObjectBuilder')
search_content('', type_contains='ProceduralGenerationDataDefinitionObjectBuilder')
```
