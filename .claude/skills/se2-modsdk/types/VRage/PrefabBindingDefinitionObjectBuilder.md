# PrefabBindingDefinitionObjectBuilder

`VRage:Keen.VRage.Multiplayer.Data.PrefabBindingDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Multiplayer.Data`
- definitions using it: **48**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ClientPrefab` | A paired prefab that contains object builders which will receive the server composition. |
| `ReplicatedData` | The types that are set to the client entity from the server Data Entity. |
| `ServerComposite` | The server composite definition to pair to a client. |

## A real one

`Vanilla\Assets\Templates\BasePrefab.def`

```json
{
  "Guid": "f0432bc1-240f-4844-a540-afa38546a6af",
  "ServerComposite": "f995c1b7-10bc-48d4-9937-fb129a6fc897",
  "ClientPrefab": "fa9f6916-d8bb-4c3b-884a-433275f0e836",
  "ReplicatedData": null
}
```

Others: `ModelBlock`, `DebugGunBase`

---

Read it with the MCP server rather than by hand:

```
describe_type('PrefabBindingDefinitionObjectBuilder')
search_content('', type_contains='PrefabBindingDefinitionObjectBuilder')
```
