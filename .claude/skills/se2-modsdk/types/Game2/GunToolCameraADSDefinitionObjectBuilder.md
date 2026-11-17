# GunToolCameraADSDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.GunToolCameraADSDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ADSEnterTime` | How much time the camera should take to zoom in when aiming down sights |
| `ADSExitTime` | How much time the camera should take to zoom in when exiting ADS |
| `FieldOfViewMultiplier` | How much the camera FoV should be zoomed in when aiming down sights |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\GunToolCameraADSDefinition.def`

```json
{
  "Guid": "84f771be-af7e-4fcf-8502-0f62553afece",
  "FieldOfViewMultiplier": 1.5,
  "ADSEnterTime": 1500000,
  "ADSExitTime": 500000
}
```

Others: `GunToolCameraADSDefinition_RocketLauncher`

---

Read it with the MCP server rather than by hand:

```
describe_type('GunToolCameraADSDefinitionObjectBuilder')
search_content('', type_contains='GunToolCameraADSDefinitionObjectBuilder')
```
