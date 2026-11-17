# RecoilPatternDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Weapons.RecoilPatternDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Weapons`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\CharacterTools\Rifle\Rifle_RecoilPatternDefinition.def`

```json
{
  "Guid": "31e95ee3-455e-4c5c-8d6a-bf215b139386",
  "VerticalStep": 0.00698,
  "FirstShotVerticalMultiplier": 2.4,
  "HorizontalAmplitude": 0.00873,
  "PatternLengthShots": 30,
  "HorizontalStartsRight": true,
  "HorizontalNoiseAmplitude": 0.0012,
  "PatternResetSeconds": 0.15,
  "KickApplySeconds": 0.1,
  "ShakePowerPerRadian": 250
}
```

Others: `RecoilPatternDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('RecoilPatternDefinitionObjectBuilder')
search_content('', type_contains='RecoilPatternDefinitionObjectBuilder')
```
