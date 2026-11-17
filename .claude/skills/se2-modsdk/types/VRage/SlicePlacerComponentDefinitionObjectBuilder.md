# SlicePlacerComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Client.Components.SlicePlacerComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Client.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CancelAction` | The action definition for cancelling the slice placer |
| `ChangeDistanceAction` | The action definition for changing the distance of the slice placer |
| `InputContext` | The input context for the slice placer |
| `PlaceAction` | The action definition for confirming a slice and extracting the data |

## A real one

`Vanilla\Assets\System\Creative Tools\Water Slice Placer\SlicePlacerComponentDefinition.def`

```json
{
  "Guid": "9861cba9-2977-4541-be58-313d2297b427",
  "InputContext": "f7fc8994-1515-4f04-95b8-732a0273952d",
  "PlaceAction": "685ddb6c-c9c0-4b93-9d5b-b49d7fa08afc",
  "CancelAction": "d3b4c943-6020-4134-bb91-5d91f59709b0",
  "ChangeDistanceAction": "d0306c1e-d696-4b15-8b63-89678e68bde3"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SlicePlacerComponentDefinitionObjectBuilder')
search_content('', type_contains='SlicePlacerComponentDefinitionObjectBuilder')
```
