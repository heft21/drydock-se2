# ProjectilesDebugScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.Debugging.Screens.Projectiles.ProjectilesDebugScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Debugging.Screens.Projectiles`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultDecal` | Default decal that will be showed on all objects hit by the debug projectile. |
| `DefaultRocketPrefab` | Default rocket prefab that will be shown when shooting a simulated projectile with model. |
| `ShowTraces` | Whether tracers should be shown. |
| `TracesTimeoutInSeconds` | How long will tracers stay on the screen. In seconds. |

## A real one

`Vanilla\Assets\UI\Screens\ProjectilesDebugScreenConfiguration.def`

```json
{
  "Guid": "a1d7467f-4077-4d55-be59-5bf26db4d3f6",
  "ShowTraces": false,
  "TracesTimeoutInSeconds": 2,
  "DefaultDecal": "5c753183-9148-44e0-a1cc-9ac04af229b8",
  "DefaultRocketPrefab": null,
  "BlockDamageType": "235c92de-c788-46f2-aab0-972b2e305115",
  "CharacterCriticalDamageType": "086749bf-91d2-4089-b62e-71764eb54fc2",
  "CharacterDamageType": "a28e367b-9919-4601-99f6-d333fcbdb0ba"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectilesDebugScreenConfigurationObjectBuilder')
search_content('', type_contains='ProjectilesDebugScreenConfigurationObjectBuilder')
```
