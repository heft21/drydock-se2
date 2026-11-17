# EmoteDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Emotes.EmoteDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Emotes`
- definitions using it: **30**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `IsAllowedWhileSitting` | If true, emote will be activable while sitting in any seat and won't cancel when entering/exiting it. |
| `IsCancelledByMovement` | If true, any movement will cancel the emote. |
| `IsCancelledByToolEquip` | If true, emote will cancel when tool is equipped. |
| `Props` | Props used by the emote. |
| `Reactions` | Other actor reactions for Multicharacter emote. They identify other actors by name and specify which emote they will play. |
| `UnequipTool` | If true, emote will remove tool from hand, if tool was equipped. |

## A real one

`Vanilla\Assets\Characters\Shared\Animations\Male\Emotes\Definitions\Punch.def`

```json
{
  "Guid": "a5ee20b1-605e-4bdf-95d2-0fa0f1eac02e",
  "Animation": "{G}d959a783-ca1f-4a74-a095-e975de3ba298",
  "FirstPersonAnimation": null,
  "BonesMask": "32cd3841-ab42-46bb-82be-6c4275d885ce",
  "DisableRagdollWhenPlaying": {
    "DisableLegs": true,
    "DisableLeftArm": true,
    "DisableRightArm": true
  },
  "Loop": false,
  "BlendInDuration": 1000000,
  "BlendOutDuration": 1000000,
  "IsAllowedWhileSitting": false,
  "UnequipTool": true,
  "IsCancelledByMovement": false,
  "IsCancelledByToolEquip": true,
  "Props": [],
  "Reactions": []
}
```

Others: `NPC_CheckbodyEmote`, `NPC_SuspiciousEmote`

---

Read it with the MCP server rather than by hand:

```
describe_type('EmoteDefinitionObjectBuilder')
search_content('', type_contains='EmoteDefinitionObjectBuilder')
```
