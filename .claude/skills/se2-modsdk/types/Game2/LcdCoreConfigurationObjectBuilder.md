# LcdCoreConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd.LcdCoreConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Fonts` | Ordered list of font asset handles available for selection in the LCD terminal UI. |
| `Images` | Ordered list of GUI asset handles available for selection in the LCD terminal UI. |
| `SurfaceActiveLoop` | Looped while at least one LCD surface on a block is actively displaying content. |

## A real one

`Vanilla\Assets\System\Configurations\LcdCoreConfiguration.def`

```json
{
  "Guid": "17ac0b3d-3615-4a13-ac77-79d2f16c3f5f",
  "SurfaceActiveLoop": "event:/SFX/Block/LCD",
  "Fonts": [
    {
      "Key": "f41914a7-22de-42a0-8dea-f8adb2a58bc7",
      "Value": "{G}984b5200-190a-456a-bcf0-5c1c7afe0028"
    },
    {
      "Key": "a7ecabb6-0f3a-4ebe-aed1-9d5c78dfd668",
      "Value": "{G}4ed348c9-9863-4497-b0ed-79005909447b"
    }
  ],
  "Images": [
    {
      "Key": "419d5e03-f47b-4e3e-9f3e-237837269f03",
      "Value": "{G}f6b6762f-b7c6-430b-a13c-7c110c3b4b81"
    },
    {
      "Key": "87bf42bc-8851-465a-92ba-d87b2c3ccd55",
      "Value": "{G}622bb465-8ca5-498a-93a1-a270e11998b1"
    },
    {
      "Key": "d9b28f6a-3a04-4b67-ba26-ab6b1e2c64b6",
      "Value": "{G}fb681f01-7676-4d35-8839-69e2ae1f1531"
    },
    {
      "Key": "f609c2b3-ae50-4db8-9456-e70f2108d3c2",
      "Value": "{G}588887b2-550b-43d7-800e-4c9053d76e3f"
    },
    {
      "Key": "212361c7-c8cd-4308-ad7f-9cdc27ff2a35",
      "Value": "{G}e53b4599-0643-44c4-bba8-040906c584f8"
    },
    {
      "Key": "8fe6990f-91c4-48b7-94cb-b6da4b754e29",
      "Value": "{G}537273e9-5fad-439b-92f2-99d1a9c6fdbe"
    },
    {
      "Key": "e9deed43-9967-4f76-8aac-620b8ad485d6",
      "Value": "{G}f2b8bc51-4ace-41c2-8f9a-e538bdd969c6"
    },
    {
      "Key": "10aa9767-9b97-4c50-a3e9-cb4c46ac3985",
      "Value": "{G}ecd9191c-2f68-40a0-ab5f-ce83ad1d2c90"
    },
    {
      "Key": "707d991f-574e-4877-83a6-d77abf98118c",
      "Value": "{G}64a8b555-b24f-4dc3-88d4-dc8d746a886f"
    },
    {
      "Key": "d8b233f0-7a1c-4dec-a7e4-d599985d59f6",
      "Value": "{G}4bce2bf1-f4be-4c24-beec-76025f058d3c"
    },
    {
      "Key": "fad39f7e-ee45-4c4e-bd76-8762250cbc8f",
      "Value": "{G}7c15d987-0259-4c30-975b-8539d37d9105"
    },
    {
      "Key": "57c4d775-6830-4ffa-bfbe-d17f965edaa8",
      "Value": "{G}00df8c27-0d9a-4c24-af13-4bb8bbc76a99"
    },
    {
      "Key": "9dba6939-d892-42d7-b288-72d9e41550c8",
      "Value": "{G}522eac9a-de65-47be-9943-becef0c8fd9e"
    },
    {
      "Key": "07971fab-ef46-4763-9b73-072e60838f49",
      "Value": "{G}c10bda85-21fe-4719-9920-64d4648ad0a4"
    },
    {
      "Key": "0e13d91d-493b-40c6-83bb-799983db8562",
      "Value": "{G}b6fe643b-6da1-4ef4-92b4-d3757e6d3056"
    },
    {
      "Key": "8d7826cb-0661-4b17-b3ee-44aa7c5e264f",
      "Value": "{G}a8a70ae4-5c42-4e35-802f-60ffd674ac5a"
    },
    {
      "Key": "7d55b77a-4fd2-4134-af12-a127b12fc31f",
      "Value": "{G}c1b5b4d8-915f-40a9-90d8-566e2182bd72"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LcdCoreConfigurationObjectBuilder')
search_content('', type_contains='LcdCoreConfigurationObjectBuilder')
```
