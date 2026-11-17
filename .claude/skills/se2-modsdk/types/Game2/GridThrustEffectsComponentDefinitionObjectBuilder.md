# GridThrustEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Movement.Effects.GridThrustEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Movement.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphericThrustClass` | value that represents atmospheric thrusters |
| `DefaultThrustClass` | value that represents default thruster type |
| `GridDistance` | Audio event parameter to transfer grid velocity to the thrust event for sound modulation. |
| `GridMassAudioParameter` | Audio event parameter to transfer grid mass to the thrust event for sound modulation. |
| `GridVelocityParam` | Audio event parameter to transfer grid velocity to the thrust event for sound modulation. |
| `IonThrustClass` | value that represents ion thrusters |
| `LoadAudioParameter` | Audio event parameter to indicate thrust load, as in the grid is actively accelerating |
| `LoadAudioParameterValueAccelerating` | Value to send to when accelerating |
| `LoadAudioParameterValueStable` | Value to send to when stable or decelerating |
| `OnPushAudio` | Second audio event to play while thrusters are accelerating. Will continue once acceleration stops One shot sound, used for light grids |
| `OnPushAudioHeavy` | Second audio event to play while thrusters are accelerating. Will continue once acceleration stops One shot sound, used for heavy grids |
| `OnSpeedDownAudio` | Audio event to play while thrusters are decelerating. Will stop as soon as acceleration stops decreasing One shot sound, used for light grids |
| `OnSpeedDownHeavyAudio` | Audio event to play while thrusters are decelerating. Will stop as soon as acceleration stops decreasing One shot sound, used for heavy grids |
| `OnSpeedUpAudio` | Audio event to play while thrusters are accelerating. Will stop as soon as acceleration stops increasing One shot sound, used for light grids |
| `OnSpeedUpHeavyAudio` | Audio event to play while thrusters are accelerating. Will stop as soon as acceleration stops increasing One shot sound, used for heavy grids |
| `OutOfEnvironmentAudio` | One-shot sound that is played when any thrusters on the user-controlled grid are out of their working environment. |
| `SpeedAudioVolume` | What volume is applied to or when played |
| `ThrustClassAudioParameter` | Audio event parameter to transfer thruster class to to signify which kind of thrust class is out of environment |
| `ThrustEndAudioParameterValueOff` | Value sent to FMOD Studio to disable grid thrust audio. |
| `ThrustEndAudioParameterValueOn` | Value sent to FMOD Studio to enable grid thrust audio. |
| `ThrusterClassAudioParameter` | Audio event parameter to transfer thruster class to the thrust event for sound modulation. |
| `ThrusterClassToShipTypeParameterValues` | Values to send to when we sync |
| `TimeToPlaySpeedAudio` | How much time accelerating/decelerating is needed before or is played |

## A real one

`Vanilla\Assets\System\Grid\GridThrustEffectsComponentDefinition.def`

```json
{
  "Guid": "126d5865-6e0d-4669-ac9b-c735d227db78",
  "MaxThrust": 10,
  "ThrustEndAudioParameter": "OnOff",
  "ThrustEndAudioParameterValue": 1,
  "OnActivationAudio": "event:/SFX/Ship/ShipMain",
  "OnBoostActivationAudio": null,
  "AudioPlaysWhenNoThrust": true,
  "GridMassAudioParameter": "Mass",
  "ThrusterClassAudioParameter": "ShipType",
  "GridVelocityParam": "Velocity",
  "GridDistance": "Distance",
  "OnSpeedUpAudio": "event:/SFX/Ship/ShipSmallSpeedUp",
  "OnSpeedDownAudio": "event:/SFX/Ship/ShipSmallSpeedDown",
  "OnSpeedUpHeavyAudio": "event:/SFX/Ship/ShipLargeSpeedUp",
  "OnSpeedDownHeavyAudio": "event:/SFX/Ship/ShipLargeSpeedDown",
  "OnPushAudioHeavy": "event:/SFX/Ship/ShipLargeIonPush",
  "OnPushAudio": "event:/SFX/Ship/ShipSmallIonPush",
  "TimeToPlaySpeedAudio": 2499993,
  "SpeedAudioVolume": 0,
  "LoadAudioParameter": "Load",
  "LoadAudioParameterValueAccelerating": 1,
  "LoadAudioParameterValueStable": 0,
  "ThrusterClassToShipTypeParameterValues": {
    "Hydrogen": "Hydrogenic"
  },
  "DefaultThrustClass": "None",
  "IonThrustClass": "Ion",
  "AtmosphericThrustClass": "Atmospheric",
  "OutOfEnvironmentAudio": "event:/SFX/Ship/ThrusterOutOfEnviroment",
  "ThrustClassAudioParameter": "ShipThrusterOff"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridThrustEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='GridThrustEffectsComponentDefinitionObjectBuilder')
```
