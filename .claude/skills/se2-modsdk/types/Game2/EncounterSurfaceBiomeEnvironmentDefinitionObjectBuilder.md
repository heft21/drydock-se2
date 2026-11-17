# EncounterSurfaceBiomeEnvironmentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters.EncounterSurfaceBiomeEnvironmentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SpawnBiome` | The surface biome within which the environment items listed below can spawn. |
| `SpawnItems` | List of encounter items available for spawning within the specified surface biome. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\Verdure_BiomeEncounters.def`

```json
{
  "Guid": "6b3e8f1e-8727-4da8-9661-008b854ff24f",
  "SpawnBiome": null,
  "SpawnItems": [
    {
      "Key": "2427ca44-eb07-4ddc-ab21-20c3bea6bbe8",
      "Value": "0fce64c6-19d3-41a7-b017-528c79f789d7"
    },
    {
      "Key": "db45e27e-6643-4337-a421-0085a78f5259",
      "Value": "9ccb3faa-9a63-4bab-a4a1-85d5830411e1"
    },
    {
      "Key": "dea552b9-33cf-408a-b44b-2253b5a349bf",
      "Value": "6b743fc5-a8ce-404f-af74-acf3cd48ce7d"
    },
    {
      "Key": "3436298d-568f-4e0d-a3e5-3b7dccaca1dd",
      "Value": "d61c202a-f393-4a5e-9ff2-e9642cc03023"
    },
    {
      "Key": "b5a7d4fb-ade0-41ab-ae59-54f69bf536a3",
      "Value": "da5f4cbe-4b42-4cb6-b767-757c21bf510f"
    },
    {
      "Key": "d6b4c6f0-d492-45b9-8510-eb224a5258c2",
      "Value": "687ef83a-1f24-4295-aa40-0e1865e05bfb"
    },
    {
      "Key": "23158fd4-9d01-4321-8944-b7e99ddaac15",
      "Value": "cca18a52-fb04-4576-b34c-1088aa142f1a"
    },
    {
      "Key": "0072f8e4-55f6-4c7c-9f21-f5d50aebf16c",
      "Value": "28aeba56-575f-458c-b913-d6b1b5e4136a"
    }
  ]
}
```

Others: `KemikDesertEncounterSurfaceBiomeEnvironmentDefinition`, `KemikSavannaEncounterSurfaceBiomeEnvironmentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterSurfaceBiomeEnvironmentDefinitionObjectBuilder')
search_content('', type_contains='EncounterSurfaceBiomeEnvironmentDefinitionObjectBuilder')
```
