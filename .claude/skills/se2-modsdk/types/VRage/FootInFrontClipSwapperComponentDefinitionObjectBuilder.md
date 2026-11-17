# FootInFrontClipSwapperComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.Client.GameObjects.RequestConfigurator.FootInFrontClipSwapperComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Client.GameObjects.RequestConfigurator`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LeftFoot` | Left foot bone information. |
| `RightFoot` | Right foot bone information. |
| `RightToLeftClipMap` | Mapping from right foot in front version of the animation clip to left foot in front version. |

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_FootInFrontClipSwapperComponentDefinition (3).def`

```json
{
  "Guid": "1cdd18ec-d578-4dff-b1ba-ac9b77480134",
  "LeftFoot": {
    "BoneName": "Ankle_L"
  },
  "RightFoot": {
    "BoneName": "Ankle_R"
  },
  "RightToLeftClipMap": [
    {
      "$Key": "{G}e63489dd-5824-4a9f-a564-65bc440e2ef4",
      "$Value": "{G}8c3ca867-323b-408d-8c2c-a79fc341be5e"
    },
    {
      "$Key": "{G}412748ab-10d2-42df-8e88-c5535a82e89c",
      "$Value": "{G}d4321a78-84ef-46b8-b2cd-9479e3f0ba55"
    },
    {
      "$Key": "{G}5e34359b-50f8-43b9-ad30-4076e30b5a5f",
      "$Value": "{G}543bc0bf-4db0-498d-b49e-a61574ec7994"
    },
    {
      "$Key": "{G}a31b969d-33f1-443b-84ca-a8d791fe3030",
      "$Value": "{G}1b987122-ba17-447d-9c29-7451e7d0533a"
    },
    {
      "$Key": "{G}caf75571-c2c6-4ac4-aa72-c50d5431c190",
      "$Value": "{G}92b05f54-7b85-422e-a49a-f8b2c863900b"
    },
    {
      "$Key": "{G}ca1be53c-e7fc-42bd-83be-93388d7cd1c3",
      "$Value": "{G}bd04c5c6-9af5-4d7b-a976-0c86abec7cf5"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FootInFrontClipSwapperComponentDefinitionObjectBuilder')
search_content('', type_contains='FootInFrontClipSwapperComponentDefinitionObjectBuilder')
```
