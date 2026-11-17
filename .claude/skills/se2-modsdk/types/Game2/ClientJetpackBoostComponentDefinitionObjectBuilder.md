# ClientJetpackBoostComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.ClientJetpackBoostComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoostActiveAudioParameter` | Audio event parameter to control if the boost audio loop is played. |
| `BoostActiveAudioParameterOffValue` | Value sent to FMOD Studio to stop the boost audio loop. |
| `BoostActiveAudioParameterOnValue` | Value sent to FMOD Studio to play the boost audio loop. |
| `BoostChargeAudio` | Audio event to play when boost mode is charging. This is launched as soon as boost mode starts charging and stops when it is interrupted or finished. |
| `BoostChargePlayAudioParameter` | Audio event parameter to control if boost charge loop is played or not. |
| `BoostChargePlayAudioParameterOffValue` | Value sent to FMOD Studio to stop boost charge loop. |
| `BoostChargePlayAudioParameterOnValue` | Value sent to FMOD Studio to play boost charge loop. |
| `OnBoostActivationAudio` | Audio event to start playing when boost mode has finished charging. |
| `OnCannotBoostAudio` | Audio event to start playing when cannot start boost mode. One shot |

## A real one

`Vanilla\Assets\Characters\System\ClientJetpackBoostComponentDefinition.def`

```json
{
  "Guid": "c7e81c57-d5e8-4e8c-9a6b-9fe0fe91a7c8",
  "BoostChargePlayAudioParameter": "TravelChargeEnd",
  "BoostChargePlayAudioParameterOnValue": 0,
  "BoostChargePlayAudioParameterOffValue": 1,
  "BoostChargeAudio": "event:/SFX/Character/JetpackCharge",
  "BoostActiveAudioParameter": "JetpackRunEnd",
  "BoostActiveAudioParameterOnValue": 0,
  "BoostActiveAudioParameterOffValue": 1,
  "OnBoostActivationAudio": "event:/SFX/Character/JetpackPush",
  "OnCannotBoostAudio": "event:/SFX/Character/JetpackPusherror"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ClientJetpackBoostComponentDefinitionObjectBuilder')
search_content('', type_contains='ClientJetpackBoostComponentDefinitionObjectBuilder')
```
