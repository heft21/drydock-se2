# CharacterDecalReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.CharacterDecalReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_CharacterDecalReceiverDefinition.def`

```json
{
  "Guid": "5f2b1636-b2cf-454d-9ba4-3ded2faf471c",
  "RagdollLayers": [
    {
      "Key": "2314ed86-8647-4279-af21-c95e6495537e",
      "Value": "Ragdolls"
    }
  ],
  "RayBackoffDistance": 1,
  "RayDistance": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDecalReceiverDefinitionObjectBuilder')
search_content('', type_contains='CharacterDecalReceiverDefinitionObjectBuilder')
```
