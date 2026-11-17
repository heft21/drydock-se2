# ParametrizedDecalKindDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.ParametrizedDecalKindDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FalloffOverride` | if not null overrides of the resulting decal instance |
| `FlagsOverride` | if not null overrides of the resulting decal instance |
| `Kind` | the definition is related to |
| `SizeOverride` | if not null overrides XY components of |
| `ZSizeOverride` | if not null overrides Z component of |

## A real one

`Vanilla\Assets\Blocks\Drills\Drills\500\Drill500DecalKind.def`

```json
{
  "Guid": "35a7ace4-c959-4e86-a37f-a66d92afd35b",
  "Kind": "24844669-f70a-4827-8354-9e192e1d7153",
  "SizeOverride": {
    "X": 8,
    "Y": 8
  },
  "ZSizeOverride": 4,
  "FlagsOverride": null,
  "FalloffOverride": {
    "FalloffZ": 0.1,
    "FalloffAngle": 1.5707964
  }
}
```

Others: `Drill350OverrideDecalKind`, `Wheel100TracksDecalKind`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParametrizedDecalKindDefinitionObjectBuilder')
search_content('', type_contains='ParametrizedDecalKindDefinitionObjectBuilder')
```
