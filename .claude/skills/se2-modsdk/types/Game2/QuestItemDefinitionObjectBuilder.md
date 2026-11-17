# QuestItemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.QuestItems.QuestItemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.QuestItems`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Items\Quest\System\QuestItemBase.def`

```json
{
  "Guid": "023cc015-31bf-42dd-a604-ead10e0e217e",
  "DisplayName": "QuestItem",
  "Description": "",
  "Icon": "{G}1ab68b43-15d0-4bf4-b0c9-c7020229936e",
  "MassPerUnit": 1e-05,
  "Flags": 0,
  "Type": "Quest",
  "DefaultMetaData": null,
  "IsRareLoot": false,
  "ExplosiveRisk": 0,
  "Subject": "",
  "Content": "",
  "Image": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('QuestItemDefinitionObjectBuilder')
search_content('', type_contains='QuestItemDefinitionObjectBuilder')
```
