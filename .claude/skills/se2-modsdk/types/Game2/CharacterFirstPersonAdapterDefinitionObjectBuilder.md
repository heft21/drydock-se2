# CharacterFirstPersonAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Adapters.CharacterFirstPersonAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Adapters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraBone` | Name of the character model bone to attach the camera to |
| `CameraBoneWeight` | Influence of the camera bone on the relative camera position |
| `CharacterHeadOffset` | Character head offset relative to character origin or camera bone (if specified) |
| `RiggedAnimatorTag` | Tag of the component whose rig will be used to position the camera. Whole entity hierarchy will be searched for this component. If none is specified, first compatible component will be used. |

## A real one

`Vanilla\Assets\System\Camera\CharacterFirstPersonCamera\CharacterFirstPersonAdapter.def`

```json
{
  "Guid": "61ab743f-29cc-4790-a7b4-2cb34c979db2",
  "CharacterHeadOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "CameraBone": "CameraBoneParent",
  "CameraBoneWeight": 1,
  "RiggedAnimatorTag": "DefaultRiggedAnimator"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterFirstPersonAdapterDefinitionObjectBuilder')
search_content('', type_contains='CharacterFirstPersonAdapterDefinitionObjectBuilder')
```
