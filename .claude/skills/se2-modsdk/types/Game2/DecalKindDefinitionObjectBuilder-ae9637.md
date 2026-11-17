# DecalKindDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalKindDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultValue` | Default value to be used, when is not found it |

## A real one

`Vanilla\Assets\Decals\Drill350DecalKind.def`

```json
{
  "Guid": "24844669-f70a-4827-8354-9e192e1d7153",
  "DefaultValue": "90032e9d-2e6f-4f44-9697-b0077cc008ab"
}
```

Others: `WheelTrack_DecalKind`, `WheelTrack100_DecalKind`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalKindDefinitionObjectBuilder')
search_content('', type_contains='DecalKindDefinitionObjectBuilder')
```
