# TutorialDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Tutorial.TutorialDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Tutorial`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Steps` | The individual steps of this tutorial |
| `Title` | Title of the instruction panel |

## A real one

`Vanilla\Assets\UI\Tutorials\SampleTutorial.def`

Too large to inline. Fields present:

`Guid`, `Steps`, `Title`

Others: `DatapadTutorialDefinition`, `GscreenTutorialDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('TutorialDefinitionObjectBuilder')
search_content('', type_contains='TutorialDefinitionObjectBuilder')
```
