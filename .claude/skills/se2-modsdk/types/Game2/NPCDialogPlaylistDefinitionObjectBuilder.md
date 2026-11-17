# NPCDialogPlaylistDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.AI.NPC.NPCDialogPlaylistDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.AI.NPC`
- definitions using it: **18**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\BarkDialogs\Male01\Male01_SusBarks.def`

```json
{
  "Guid": "d0ddce13-1bab-4bab-be62-0338a9d0a48c",
  "Dialogs": [
    {
      "Key": "17d31ad8-4910-4669-89ec-355551c9dfa6",
      "Value": {
        "Text": "DialogBlank",
        "ContinueTextOverride": null,
        "TextColorOverride": null,
        "AudioOverride": "event:/Dialog/NPCBarks/SusBarks/AnyoneThere_Male01",
        "Duration": 20000000
      }
    },
    {
      "Key": "806de00b-06a0-4b2a-ad3f-6294f37b0e35",
      "Value": {
        "Text": "DialogBlank",
        "ContinueTextOverride": null,
        "TextColorOverride": null,
        "AudioOverride": "event:/Dialog/NPCBarks/SusBarks/HuhWhatwasThat_Male01",
        "Duration": 30000000
      }
    },
    {
      "Key": "8f56524c-d30e-42b0-a623-39776dc9b4b7",
      "Value": {
        "Text": "DialogBlank",
        "ContinueTextOverride": null,
        "TextColorOverride": null,
        "AudioOverride": "event:/Dialog/NPCBarks/SusBarks/ShowYourself_Male01",
        "Duration": 20000000
      }
    },
    {
      "Key": "03edb74c-b876-485d-b721-06665ca4cc93",
      "Value": {
        "Text": "DialogBlank",
        "ContinueTextOverride": null,
        "TextColorOverride": null,
        "AudioOverride": "event:/Dialog/NPCBarks/SusBarks/ThoughtISawSomething_Male01",
        "Duration": 30000000
      }
    }
  ]
}
```

Others: `Male04_SusBarks`, `Male01_AlertBarks`

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCDialogPlaylistDefinitionObjectBuilder')
search_content('', type_contains='NPCDialogPlaylistDefinitionObjectBuilder')
```
