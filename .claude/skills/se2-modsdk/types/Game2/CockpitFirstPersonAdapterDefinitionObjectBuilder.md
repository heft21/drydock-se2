# CockpitFirstPersonAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Adapters.CockpitFirstPersonAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Adapters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyType` | Model dummy used for offsetting the camera. |

## A real one

`Vanilla\Assets\System\Camera\CockpitFirstPersonCamera\CockpitFirstPersonAdapterHead.def`

```json
{
  "Guid": "3b8b7d1d-916a-4595-bc6f-454a3db07a18",
  "CharacterHeadOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "CameraBone": null,
  "CameraBoneWeight": 1,
  "RiggedAnimatorTag": null,
  "DummyType": "2f0f6710-3dc2-4ecb-bcc6-0719ad23bd07"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitFirstPersonAdapterDefinitionObjectBuilder')
search_content('', type_contains='CockpitFirstPersonAdapterDefinitionObjectBuilder')
```
