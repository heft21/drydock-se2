# DialogueModeScreenAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Dialogue.DialogueModeScreenAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Dialogue`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\DialogueModeScreenAvaloniaConfiguration.def`

```json
{
  "Guid": "50343914-04bf-4625-9e4a-6cfdea57000c",
  "ContinueText": "GenericDialogContinue",
  "ExitConversationText": "DialogueExitConversation"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DialogueModeScreenAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='DialogueModeScreenAvaloniaConfigurationObjectBuilder')
```
