# BlockSchematicItemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.BlockSchematics.BlockSchematicItemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.BlockSchematics`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Items\BlockSchematics\System\BlockSchematicBase.def`

```json
{
  "Guid": "bb0a1acc-12fe-497b-864e-af9ba24d269c",
  "DisplayName": "BlockSchematic",
  "Description": "",
  "Icon": "{G}819ebdf9-6f7d-4755-b04c-0de430e8715f",
  "MassPerUnit": 1e-05,
  "Flags": 0,
  "Type": "BlockSchematic",
  "DefaultMetaData": null,
  "IsRareLoot": false,
  "ExplosiveRisk": 0,
  "Effects": [],
  "CooldownCategory": "49b3654b-f58e-4d23-8f8e-994705986714",
  "AutoUseThresholds": [],
  "Cooldown": 10000000,
  "StatsMaxLocKey": "",
  "MissingItemLocKey": "",
  "ConsumableUsedAudio": null,
  "Reward": "bf7de12a-bdc3-4612-a893-f315f5ba527e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockSchematicItemDefinitionObjectBuilder')
search_content('', type_contains='BlockSchematicItemDefinitionObjectBuilder')
```
