# GravityTypeDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.Gravity.GravityTypeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.Gravity`
- definitions using it: **4**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\GravityTypes\NoGravity.def`

```json
{
  "Guid": "106e9dbf-fa79-4805-9a32-a243d07938bd"
}
```

Others: `NaturalGravity`, `ArtificialGravity`

---

Read it with the MCP server rather than by hand:

```
describe_type('GravityTypeDefinitionObjectBuilder')
search_content('', type_contains='GravityTypeDefinitionObjectBuilder')
```
