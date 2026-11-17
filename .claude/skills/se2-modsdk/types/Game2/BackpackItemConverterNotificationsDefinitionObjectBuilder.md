# BackpackItemConverterNotificationsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.BackpackItemConverterNotificationsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MissingIngredientsFallbackNotification` | Notification shown when an item required can't be crafted due to missing ingredients in raw mode |
| `MissingIngredientsNotification` | Notification shown when an item required can't be crafted due to missing ingredients in components mode |
| `OnMissingIngredientsAudio` | Audio event to play when an item required can't be crafted due to missing ingredients |
| `RecipeCompleteCooldown` | Amount of time the backpack crafting screen will remain visible after crafting stops. Used to prevent the screen from flashing between recipes |
| `UncraftableNotification` | Notification shown when an item required can't be crafted due to the recipe not existing |
| `UncraftableSolutionNotification` | Notification shown when an item required can't be crafted due to the recipe not existing, but a progression-based solution exists. |

## A real one

`Vanilla\Assets\CharacterTools\HandWelders\Shared\HandWelder_Client_BackpackItemConverterNotificationsDefinition.def`

```json
{
  "Guid": "4fe7baf1-6e9c-4588-8a8a-16f2ba5900fb",
  "MissingIngredientsNotification": "222645c0-0512-4830-8092-48c34b94a508",
  "MissingIngredientsFallbackNotification": "b4723c2c-4869-44aa-b881-2975a1fd7408",
  "UncraftableNotification": "d797c5f5-95a3-4475-8732-77a6136c3a3d",
  "UncraftableSolutionNotification": "26246a9d-8a8d-44a3-a618-ac1ebdf710cf",
  "RecipeCompleteCooldown": 10000000,
  "OnMissingIngredientsAudio": "event:/UI/HudUnable"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BackpackItemConverterNotificationsDefinitionObjectBuilder')
search_content('', type_contains='BackpackItemConverterNotificationsDefinitionObjectBuilder')
```
