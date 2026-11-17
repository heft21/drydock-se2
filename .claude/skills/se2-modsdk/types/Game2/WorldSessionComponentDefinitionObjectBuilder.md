# WorldSessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.CoreComponents.WorldSessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.CoreComponents`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ClientWaterSessionDefinition` | to add to client session components on world init |
| `GridPrefabProviderDefinition` | to add to both server and client session components on world init |
| `OwnershipSessionDefinition` | to add to both server and client session components on world init |
| `ProjectileSystemDefinition` | to add to server session components on world init |
| `SaveSessionDefinition` | to add to server session on world init. |
| `ServerWaterSessionDefinition` | to add to server session components on world init |

## A real one

`Vanilla\Assets\System\World.def`

```json
{
  "Guid": "9a129741-96d4-45fa-8b34-60707317cc8a",
  "ProjectileSystemDefinition": "111a97db-1f47-4e93-aaef-724296e369c7",
  "ServerWaterSessionDefinition": "ade20776-5f2d-4f9b-9bf4-598c4fa0fc16",
  "ClientWaterSessionDefinition": "ade20776-5f2d-4f9b-9bf4-598c4fa0fc17",
  "OwnershipSessionDefinition": "986b2519-39ac-42df-9e9b-3beb361eb8cb",
  "GridPrefabProviderDefinition": "60565856-1ca1-41fb-b231-32fdd7f4d757",
  "SaveSessionDefinition": "7688f750-e775-4433-99b2-511e57078f6c"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WorldSessionComponentDefinitionObjectBuilder')
search_content('', type_contains='WorldSessionComponentDefinitionObjectBuilder')
```
