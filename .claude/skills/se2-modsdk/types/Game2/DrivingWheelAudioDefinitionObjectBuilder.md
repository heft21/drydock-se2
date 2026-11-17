# DrivingWheelAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.DrivingWheelAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaterialsMapping` | Mapping of audio events played for each material group that the wheel rolls over. |
| `RollingSpeedParameter` | Parameter for that specifies how fast the wheel is rolling over the surface. |
| `SkidRatioParameter` | Parameter for that specifies how much the wheel is skidding (loss of traction). Value between 0 and 1. |
| `WheelRadiusParameter` | Parameter for representing radius of the wheel. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\DrivingWheel\DrivingWheelAudioDefinition.def`

```json
{
  "Guid": "5df17388-4a58-4b7b-a5c1-b724887949b5",
  "MaterialsMapping": {
    "39c1cfce-31fa-4503-b99a-50511d73ab64": "47753f38-2c54-4a72-aed1-29802d63c123",
    "44ac27b1-7c39-4a2b-bc71-6a31b80db2c1": "62c3fee4-9eb0-4275-9bb3-b024ad5e9f1b",
    "e2431cdd-c4d1-4455-a303-06fde11a922c": "ba16a3d8-95ef-422f-a9c9-809c5ca28861",
    "d14e99db-54fc-411a-91f9-3d3db7212c76": "62c3fee4-9eb0-4275-9bb3-b024ad5e9f1b",
    "56dd2b0b-15d2-479f-a33e-f49129afe00a": "b70d586f-08d8-4238-a643-183539f990ff",
    "2a32e418-fe92-43bd-9379-15e346f2d49d": "cd8668c2-14a3-4594-8ed5-7a8546368f89",
    "bdcb6026-d19e-49ba-a98c-9a51c2cb5d21": "47753f38-2c54-4a72-aed1-29802d63c123",
    "79499795-d863-4b42-8ba4-535848247fd8": "ba16a3d8-95ef-422f-a9c9-809c5ca28861",
    "b0daa08e-c571-4d3f-bdc6-7b25dcc5baea": "ba16a3d8-95ef-422f-a9c9-809c5ca28861",
    "cb39081f-c52d-4a0e-ae5f-106e218f76eb": "67f8e8dd-e048-4f92-b9c8-601a588047c2",
    "ef4babe2-f6c6-4446-8318-f818528b065b": "ba16a3d8-95ef-422f-a9c9-809c5ca28861"
  },
  "RollingSpeedParameter": "RollingSpeed",
  "SkidRatioParameter": "SkidRatio",
  "WheelRadiusParameter": "WheelRadius"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrivingWheelAudioDefinitionObjectBuilder')
search_content('', type_contains='DrivingWheelAudioDefinitionObjectBuilder')
```
