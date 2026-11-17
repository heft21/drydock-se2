# LcdImageCatalogConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd.LcdImageCatalogConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Images` | Ordered list of GUI asset handles available for selection in the LCD terminal UI. |

## A real one

`Vanilla\Assets\System\Configurations\LcdImageCatalogConfiguration.def`

```json
{
  "Guid": "c0a85b0b-9c2a-4079-a7ae-95a255597395",
  "Images": [
    {
      "Key": "e8e79910-1713-428c-8e1f-8c3dedce77a6",
      "Value": "{G}0c37e2cf-7215-4cd4-b4ba-82843e903051"
    },
    {
      "Key": "1e2c4081-a533-4814-870e-250d7bba75e9",
      "Value": "{G}6f7b8023-bc20-4ff3-b289-392552a16a07"
    },
    {
      "Key": "4ebf7d3a-a18d-4c84-ac88-5c31591406d5",
      "Value": "{G}3028b8a5-ea46-402a-9317-ee0cadc8a87d"
    },
    {
      "Key": "53372cc6-7fa9-4d5f-b70a-4359eda73394",
      "Value": "{G}d5af2a12-1508-4046-944f-fccf44723e9e"
    },
    {
      "Key": "71501b5d-685e-43cf-b17c-7d7e1b0a1e62",
      "Value": "{G}b64ff0bd-e0c0-4141-9eb8-39e36b83fff8"
    },
    {
      "Key": "ed0933b3-b0ee-4221-bb7c-cd0519fd0705",
      "Value": "{G}4577e525-7cad-4224-90d9-0188e2dfc44c"
    },
    {
      "Key": "293a7229-e6f9-4cde-959e-87d45ccbc2ce",
      "Value": "{G}c6b1e572-cf52-4d4e-bf43-01f814816709"
    },
    {
      "Key": "15cb4313-4371-49f1-b256-e53dc3a82327",
      "Value": "{G}e5d91627-3a2c-4de2-b752-48544f3710e0"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LcdImageCatalogConfigurationObjectBuilder')
search_content('', type_contains='LcdImageCatalogConfigurationObjectBuilder')
```
