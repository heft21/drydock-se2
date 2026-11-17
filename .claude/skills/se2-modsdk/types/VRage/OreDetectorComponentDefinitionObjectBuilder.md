# OreDetectorComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.OreDetectorComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectableOreMaterials` | List of all that can be detected by this detector. |
| `Range` | Maximum range of the detector. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\OreDetectorComponentDefinition.def`

```json
{
  "Guid": "c1106d29-c208-446f-8159-245db62db802",
  "Range": 130,
  "DetectableOreMaterials": [
    {
      "Key": "0909465f-41cc-4ce3-ba64-33f9dea0919d",
      "Value": "2aa5841a-6422-4e95-bb30-7f9822197759"
    },
    {
      "Key": "4fcd5f01-bf1e-4887-8b56-1754eda6b22d",
      "Value": "8ce42d81-0100-40f2-b37f-8ae519e8f0c0"
    },
    {
      "Key": "01f3a9cd-d853-4e56-a110-263767b9afe6",
      "Value": "99252318-6504-471b-a0ed-1dbc3ed4cf74"
    },
    {
      "Key": "26c35e19-33a1-4ee5-a37d-517660983ce1",
      "Value": "35f1586f-1355-4f29-a7c5-b4ac9cd5c9b3"
    },
    {
      "Key": "d08eeaca-3643-4c88-b8ac-f6fdac7074f3",
      "Value": "35aca48e-3a67-419e-8d1c-e53f12691dc2"
    },
    {
      "Key": "82755dce-6f8e-486c-8b50-6d807e559db7",
      "Value": "30ca48a2-d182-4892-8629-60433c18883f"
    },
    {
      "Key": "28b5d732-9089-4200-947a-18a1d2b98ef0",
      "Value": "92203377-1768-46d8-a37a-81546c65ca46"
    },
    {
      "Key": "d194f1c4-6fe3-4584-8d75-c143d04f8546",
      "Value": "d0eced28-90a4-4320-ade3-786c87ae3f5f"
    },
    {
      "Key": "d7a73b3e-49bf-4436-a9c8-24563fdbe2e1",
      "Value": "1f5d7d9b-9fe5-4fbc-8b88-42794e005137"
    },
    {
      "Key": "e9191b73-0125-4aec-b562-b7967e13c5aa",
      "Value": "e3886d85-0a72-404d-89f4-5bfeb47ce1a2"
    },
    {
      "Key": "beb1d039-ff3d-431a-b0c8-7cf040d80cf3",
      "Value": "b177cb28-26d2-4c2a-bbf9-1d327a469984"
    },
    {
      "Key": "a951b086-42ae-4e51-9b2c-1a8b97f8ff88",
      "Value": "68110eea-4d3d-4ab5-97ae-be03d75b4ec6"
    },
    {
      "Key": "821b4b59-8b21-4e74-89b8-2608e6fb4580",
      "Value": "4af460d1-5dd1-420d-af7b-be9c91409a8d"
    },
    {
      "Key": "8dbec2ba-d04b-476c-8174-5a1522d98481",
      "Value": "4c7d4cd3-ede4-430c-92fc-1a04eebf9077"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OreDetectorComponentDefinitionObjectBuilder')
search_content('', type_contains='OreDetectorComponentDefinitionObjectBuilder')
```
