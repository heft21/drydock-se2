# NPCDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.Dialog.NPCDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC.Dialog`
- definitions using it: **10**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\GenericNPCConversation.def`

```json
{
  "Guid": "39f5c7c2-93f7-4bf1-b893-ade74349df53",
  "Dialogs": [
    {
      "Key": "172833fb-fcd3-4549-8ced-9375b28b9525",
      "Value": {
        "Text": "GenericSocialDialog1",
        "ContinueTextOverride": "GenericSocialDialog1Continue",
        "TextColorOverride": null,
        "AudioOverride": null
      }
    },
    {
      "Key": "6c639954-34eb-4f09-b01b-9945d522ad30",
      "Value": {
        "Text": "GenericSocialDialog2",
        "ContinueTextOverride": "GenericSocialDialog2Continue",
        "TextColorOverride": null,
        "AudioOverride": null
      }
    }
  ],
  "Random": false,
  "GenericAudio": "event:/SFX/Character/VocPain",
  "TextColor": {
    "PackedValue": 4294967295
  }
}
```

Others: `FTUENPC_Bark`, `GenericNPCDialogDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCDialogDefinitionObjectBuilder')
search_content('', type_contains='NPCDialogDefinitionObjectBuilder')
```
