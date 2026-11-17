# LcdRenderBudgetConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.Lcd.LcdRenderBudgetConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render.Lcd`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MemoryBudgetRatio` | Fraction of the adapter's dedicated VRAM that LCD offscreen render targets may collectively occupy. Multiplied once at session init against CurrentAdapter.DedicatedRAM to derive the absolute byte ceiling used by the admission cutoff. Expressed in VRAM, not system RAM. |
| `ObserverTag` | Tag used to resolve the main-camera transform from . |
| `VisibleHysteresisThreshold` | Consecutive ticks a panel must remain admitted before its offscreen render target is actually allocated. Prevents thrashing at the budget boundary. |

## A real one

`Vanilla\Assets\System\Configurations\LcdRenderBudgetConfiguration.def`

```json
{
  "Guid": "d6a9a5f3-b3a1-4aea-b820-065e4cf0a4a9",
  "ObserverTag": "VisualEffectsObserver",
  "MemoryBudgetRatio": 0.03,
  "VisibleHysteresisThreshold": 5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LcdRenderBudgetConfigurationObjectBuilder')
search_content('', type_contains='LcdRenderBudgetConfigurationObjectBuilder')
```
