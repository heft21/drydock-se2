# DrivingWheelEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.DrivingWheelEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DecalSideDriftMultiplier` | If contact point is not directly under the wheel center, allows decal center move towards the contact point. 0 - decal is always placed under the wheel center. 1 - decal center will be placed at contact point |
| `MaterialsMapping` | Mapping for effects to play when wheel drives over the given materials. |
| `SlidingVelocityThreshold` | If wheel sliding velocity relative to the surface is greater than this, the wheel is considered to be sliding. When the wheel is sliding is played and is displayed |
| `WheelFootprint` | Dummy of wheel footprint. It is expected to be placed in the center of the wheel and have X and Z size represent size of the wheel decals. Doesn't have to match decal size exactly if decals should intersect or have gaps between them. |
| `WheelSlipDecal` | Decal to be placed by wheels when they are slipping |
| `WheelTracksDecal` | Decal to be placed by wheels when they are rolling normally |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\DrivingWheel\DrivingWheelEffectsDefinition.def`

```json
{
  "Guid": "36a99650-3d80-4395-9115-4860d5f74d99",
  "MaterialsMapping": {
    "6dadf3ac-aa96-4b1b-a4c5-891633a0b48a": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "2cd1ac9d-c356-44ab-bd8c-156fc04df396": "dcc04071-7f2c-4410-86eb-448e1be73034",
    "0707bc4d-5d81-4880-a5c6-aa73c5a6130f": "e52c5285-6046-437c-abfc-27aeea7f666e",
    "1f9d1544-20d5-4d61-bc50-871b80f4102a": "6c300747-22cc-496e-aa13-3fed49daf3d4",
    "4d3e85f3-82e4-4cd2-bc8f-51fdc945159d": "5d2838d1-3a4c-43b2-b215-2baeb6830a0d",
    "6760ebeb-99fe-4a50-8bd6-f295b5fe204d": "bcccd34c-08de-469c-8e90-862efded0228",
    "45d9dca6-ce11-4ffb-b051-f0c537294a82": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "1d51ff66-4fd8-4ad3-a765-dfc79a2cd943": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "8fabb5be-014a-4c11-a16d-8bd2dc293d9f": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "c6657d3b-e7db-4871-bfc5-441932ffc022": "bcccd34c-08de-469c-8e90-862efded0228",
    "2b7b0f1a-9bf2-469b-8656-d91eab97dacf": "e52c5285-6046-437c-abfc-27aeea7f666e",
    "c84e1c39-dc07-49f7-8f65-3e8402a9afe0": "6c300747-22cc-496e-aa13-3fed49daf3d4",
    "b8ed6fe3-9a73-4cb8-be3d-685a8e49acca": "826cd30b-77a9-49ee-86a9-21560e399801",
    "600d89e3-5cfe-4fce-871c-5b6bfbf24920": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "198a4f21-696a-44b5-8f0f-2532aa4b6b6d": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "c758008a-cbc6-4cdc-8e03-afab8b2f1e8a": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "fd1b5a0f-88e2-45e9-9141-5b43ed950cee": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "91303a5e-44ed-497e-9133-93bf00deb618": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "ebe00296-f624-4e9a-b21c-d29aa2e5bb35": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "62033b00-7e83-45c1-aad1-55797fe7b654": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "56dc5dd4-2a6a-4bb7-9a0e-f2acd01516e8": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1",
    "b5dd83e5-e8a1-4428-8f83-aa0de5a33d8b": "5d2838d1-3a4c-43b2-b215-2baeb6830a0d",
    "2299bdfa-40dd-4c62-be2f-fa4404319829": "db5e9851-87e9-4c7d-aec5-9c5f45a120c1"
  },
  "SlidingVelocityThreshold": 0.5,
  "WheelTracksDecal": null,
  "WheelSlipDecal": null,
  "WheelFootprint": "6eb13cdf-a649-4720-947a-1578165a7cb3",
  "DecalSideDriftMultiplier": 0.1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrivingWheelEffectsDefinitionObjectBuilder')
search_content('', type_contains='DrivingWheelEffectsDefinitionObjectBuilder')
```
