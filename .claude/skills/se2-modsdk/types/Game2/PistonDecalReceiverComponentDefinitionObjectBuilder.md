# PistonDecalReceiverComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.PistonDecalReceiverComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DecalPlacementRatio` | How offset the decal from the hit position 0 - decal lower-Z side is flush with the hit point 1 - decal higher-Z side is flush with the hit point |
| `MaxSubpartDecalZSize` | When decal is applied to piston moving subpart it will have Z-size limited to this value |
| `MinBodyDecalZSize` | When decal is applied to the main piston body its Z-size will be increased |

## A real one

`Vanilla\Assets\Blocks\Pistons\150\Piston150_Client_PistonDecalReceiverComponentDefinition.def`

```json
{
  "Guid": "5fd7097b-adee-49db-a0ab-13fc4495f05e",
  "MaxSubpartDecalZSize": 0.15,
  "MinBodyDecalZSize": 0.3
}
```

Others: `Piston500_Client_PistonDecalReceiverComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PistonDecalReceiverComponentDefinitionObjectBuilder')
search_content('', type_contains='PistonDecalReceiverComponentDefinitionObjectBuilder')
```
