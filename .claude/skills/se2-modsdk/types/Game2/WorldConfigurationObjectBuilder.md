# WorldConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Worlds.WorldConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Worlds`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultThumbnail` | Default thumbnail to display on worlds without or with invalid thumbnails |

## A real one

`Vanilla\Assets\MainMenuData\UGC\Worlds\WorldConfiguration.def`

```json
{
  "Guid": "11b3dbd9-bce3-4af4-a108-3993f1d0cf5c",
  "DefaultThumbnail": "{G}0a64974e-ec95-4fea-89fd-63aff36e43c9"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WorldConfigurationObjectBuilder')
search_content('', type_contains='WorldConfigurationObjectBuilder')
```
