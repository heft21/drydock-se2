# ContainerBlockEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.ContainerBlockEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ContainerSizeParameter` | Parameter name to send container size to audio event |
| `ContainerSizeParameterValue` | Parameter value to send with |
| `EmptyFullParameter` | Parameter name to send container fullness to audio event |
| `EmptyFullParameterEmptyValue` | Parameter value to send with when container is empty |
| `EmptyFullParameterFullValue` | Parameter value to send with when container is full |
| `FullnessRatio` | Ratio of container mass/max mass, will be considered full if above this value |
| `IsResourceContainer` | If true, depends on , otherwise depends on |
| `OnDestroyedAudio` | Audio event to play when block is fully destroyed. One shot sound. |
| `OnTankFillingAudio` | Audio event to play when tank block is filling. One shot sound. |
| `OnTankReleasingAudio` | Audio event to play when tank block is releasing/leaking. One shot sound. |
| `TankEventOffValue` | Parameter value to send to when inactive |
| `TankEventOnOffParameter` | Parameter name to send to and when active |
| `TankEventOnValue` | Parameter value to send to when active |

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\Tanks_ContainerBlockEffectsDefinition.def`

```json
{
  "Guid": "a26c350d-b3cd-45bd-b036-e21690cc2f47",
  "IsResourceContainer": true,
  "OnDestroyedAudio": "event:/SFX/Explosions/ExplosionHydroTank1250",
  "ContainerSizeParameter": "",
  "ContainerSizeParameterValue": "",
  "EmptyFullParameter": "EmptyFull",
  "EmptyFullParameterEmptyValue": 0,
  "EmptyFullParameterFullValue": 1,
  "FullnessRatio": 0.5,
  "OnTankFillingAudio": "event:/SFX/Block/HydrogenTank",
  "OnTankReleasingAudio": "event:/SFX/Block/OxygenTank",
  "TankEventOnOffParameter": "OnOff",
  "TankEventOnValue": "On",
  "TankEventOffValue": "Off"
}
```

Others: `CargoContainers_ContainerBlockEffectsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ContainerBlockEffectsDefinitionObjectBuilder')
search_content('', type_contains='ContainerBlockEffectsDefinitionObjectBuilder')
```
