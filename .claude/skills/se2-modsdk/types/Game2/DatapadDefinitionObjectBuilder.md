# DatapadDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Datapads.DatapadDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Datapads`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Content` | Main content/body of the datapad message |
| `Date` | Date when the datapad was created (generic text for flexibility) |
| `Encrypted` | Whether this datapad's content is encrypted |
| `Image` | Optional image for the datapad UI |
| `Recipient` | Name of the recipient |
| `Sender` | Name of the originator/sender of the message |
| `Subject` | Kind of a subtitle |
| `Title` | Title - shown at top of the datapad UI screen |

## A real one

`Vanilla\Assets\Items\Datapads\System\DatapadBase.def`

```json
{
  "Guid": "879dee46-3e17-449a-a7fb-3eeb0864077a",
  "DisplayName": "Datapad",
  "Description": "",
  "Icon": "{G}4d4ab18b-8303-4fd4-9a46-df5a815c913a",
  "MassPerUnit": 0.01,
  "Flags": "Stackable",
  "Type": "Datapad",
  "DefaultMetaData": null,
  "IsRareLoot": false,
  "ExplosiveRisk": 0,
  "Sender": "DPSenderNameBase",
  "Recipient": "DPRecipentBase",
  "Date": "DPDateBase",
  "Title": "DPTitleBase",
  "Subject": "DPSubjectBase",
  "Content": "DPContentAA0000",
  "Image": null,
  "Encrypted": false
}
```

Others: `Booklet001`, `Booklet002`

---

Read it with the MCP server rather than by hand:

```
describe_type('DatapadDefinitionObjectBuilder')
search_content('', type_contains='DatapadDefinitionObjectBuilder')
```
