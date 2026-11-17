# ComponentMigrationsDefinitionObjectBuilder

`VRage:Keen.VRage.DCS.Definitions.ComponentMigrationsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.DCS.Definitions`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Migrations` | Key = From, Value = To |
| `Version` | The maximum version these migrations will be applied. When the save's version is less than this version, the changes will apply. |

## A real one

`Vanilla\Assets\System\Migrations\EditorComponentMigrations.def`

Others: `TemplateComponentMigrations`, `PlanetTemplateComponentMigrations`

---

Read it with the MCP server rather than by hand:

```
describe_type('ComponentMigrationsDefinitionObjectBuilder')
search_content('', type_contains='ComponentMigrationsDefinitionObjectBuilder')
```
