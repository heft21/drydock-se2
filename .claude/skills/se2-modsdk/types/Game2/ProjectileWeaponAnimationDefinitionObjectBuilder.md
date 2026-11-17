# ProjectileWeaponAnimationDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Weapons.ProjectileWeaponAnimationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Weapons`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Magazine` | Prefab to spawn at |
| `MagazineBoneName` | Name of the bone to bind magazine to during reload |
| `MagazineBoneOffset` | Optional offset that will be applied from the bone position. |
| `MagazineDummy` | The dummy for the weapon magazine |
| `ReloadEndEvent` | Animation event to listen to to show |
| `ReloadStartEvent` | Animation event to listen to to hide |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\ProjectileWeaponAnimationDefinition.def`

```json
{
  "Guid": "b552e12a-d8fe-4655-b14c-b305e5670259",
  "MagazineDummy": "ff0fbd63-71f7-4c26-9d0e-163f8c7f3897",
  "Magazine": null,
  "ReloadStartEvent": "ReloadStart",
  "ReloadEndEvent": "ReloadEnd",
  "MagazineBoneName": "",
  "MagazineBoneOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  }
}
```

Others: `RocketLauncher_Client_ProjectileWeaponAnimationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileWeaponAnimationDefinitionObjectBuilder')
search_content('', type_contains='ProjectileWeaponAnimationDefinitionObjectBuilder')
```
