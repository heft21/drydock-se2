# InteractorEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.InteractorEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectionArgs` | Detector settings for finding/sensing this interactor such as settings for proximity, radius, or filtering conditions. |
| `InputKind` | The InputKind this interactor belongs to. It specifies the input category (such as movement, interaction, or tools) associated with this interactor. |
| `InteractionDistanceMax` | Maximum distance between player and interactor for the interaction to be possible |
| `UseActionBindings` | Action bindings to use for dummy interactions. Defines which actions are triggered when interacting with dummies in the game world. |

## A real one

`Vanilla\Assets\Characters\System\Interactor.def`

```json
{
  "Guid": "3ca72a22-63af-40c5-a02a-392d8052ef56",
  "InteractionDistanceMax": 5,
  "UseActionBindings": "67f792fb-986f-4e77-a7cb-effcbb91f24e",
  "InputKind": "Interaction",
  "DetectionArgs": {
    "DetectDummies": true,
    "UsePreciseColliderForBlocks": true,
    "DetectChildEntities": false,
    "DetectTopMostEntities": false,
    "Frequency": 1,
    "Occlusion": true,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0,
    "LayerFilter": "83c2cb5a-ba63-4b96-8d83-fb28d7eb2b93"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InteractorEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='InteractorEntityComponentDefinitionObjectBuilder')
```
