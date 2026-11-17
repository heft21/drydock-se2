# MaterialEffectAssociationDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Definitions.MaterialEffectAssociationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Definitions`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Associations` | List of materials belonging to the same effect group. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\OnVoxelMinedEffectAssociations.def`

Too large to inline. Fields present:

`Associations`, `Guid`

Others: `HandDrill_MaterialEffectAssociationDefinition`, `LandingPrefabCharacterClient_CharacterMovementEffectsComponentDefinition_MaterialEffectAssociationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialEffectAssociationDefinitionObjectBuilder')
search_content('', type_contains='MaterialEffectAssociationDefinitionObjectBuilder')
```
