# GunToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.GunToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BarrelDummyType` | Dummy that identifies where projectiles will spawn from. Optional |

## A real one

`Vanilla\Assets\CharacterTools\Rifle\Rifle_Client_GunToolControllableDefinition.def`

```json
{
  "Guid": "1f2f3f17-4b97-4b34-b70b-097891ea5dab",
  "BarrelDummyType": "6fc9829d-3ee4-4735-b229-e00157f67a42"
}
```

Others: `Pistol_Client_GunToolControllableDefinition`, `DebugGun_Client_GunToolControllableDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('GunToolControllableDefinitionObjectBuilder')
search_content('', type_contains='GunToolControllableDefinitionObjectBuilder')
```
