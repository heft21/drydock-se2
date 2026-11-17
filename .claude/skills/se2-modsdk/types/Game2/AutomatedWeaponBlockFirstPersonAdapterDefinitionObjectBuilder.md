# AutomatedWeaponBlockFirstPersonAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Adapters.AutomatedWeaponBlockFirstPersonAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Adapters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyType` | Model dummy used for offsetting the camera. |

## A real one

`Vanilla\Assets\System\Camera\TurretPrefabFirstPersonCamera\TurretPrefabFirstPersonCamera_AutomatedWeaponBlockFirstPersonAdapterDefinition.def`

```json
{
  "Guid": "78b03f14-eb26-4ac0-a000-62ec2e879251",
  "DummyType": "6fc9829d-3ee4-4735-b229-e00157f67a42"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AutomatedWeaponBlockFirstPersonAdapterDefinitionObjectBuilder')
search_content('', type_contains='AutomatedWeaponBlockFirstPersonAdapterDefinitionObjectBuilder')
```
