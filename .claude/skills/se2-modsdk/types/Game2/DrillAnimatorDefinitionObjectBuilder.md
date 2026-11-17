# DrillAnimatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Render.Drills.DrillAnimatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Render.Drills`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Blocks\Grinder\350\Grinder350DrillAnimatorDefinition.def`

```json
{
  "Guid": "c5bef786-c5e4-4673-9f10-317c6d57338c",
  "AnimationDummy": "fb621cb9-438c-4141-9751-f4a59196658f",
  "SphereRadius": 0,
  "CameraShakePower": 0.25,
  "MaxCameraShakePower": 1
}
```

Others: `DrillAnimatorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillAnimatorDefinitionObjectBuilder')
search_content('', type_contains='DrillAnimatorDefinitionObjectBuilder')
```
