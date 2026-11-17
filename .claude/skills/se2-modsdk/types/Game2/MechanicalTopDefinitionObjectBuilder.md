# MechanicalTopDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalTopDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Type` | Specifies what kind of top block it is. The counterpart must accept this type in order to allow connection. Allows to prevent Pistons from attaching to Rotor tops, but allows multiple different Rotor tops to attach to Rotor base. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\HingeHead_MechanicalTopDefinition.def`

```json
{
  "Guid": "c694cfe6-d7a0-4e50-9cfa-b892a97c0e4a",
  "ConnectionGroups": [
    {
      "Key": "a558bc45-f986-412a-94fd-1c2c2209b268",
      "Value": "262d50d2-7b5b-4939-a81b-70f731d0e252"
    },
    {
      "Key": "6af14aac-4de0-4a96-9016-34088ff65d1d",
      "Value": "2ed2d414-fedb-42a2-bc75-2b26417e1346"
    },
    {
      "Key": "4b653e8b-0289-4dbd-a9dd-44ecaffe6812",
      "Value": "a5bd777b-b184-41c9-af22-284d7178c267"
    }
  ],
  "Type": "1a87027d-8857-4cc8-9b16-bef26d04a1fd"
}
```

Others: `RotorHead_MechanicalTopDefinition`, `PistonHead_MechanicalTopDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalTopDefinitionObjectBuilder')
search_content('', type_contains='MechanicalTopDefinitionObjectBuilder')
```
