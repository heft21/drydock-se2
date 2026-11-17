# FrameSettingsOverrideDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.FrameSettingsOverrideDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **6**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Environment\Planets\Kemik\Atmosphere\KemikEnvironmentRender_FrameSettingsOverrideDefinition.def`

```json
{
  "Guid": "9df94cbd-6bb6-423b-a87a-c9f5a3535522",
  "DirLightColor": null,
  "DirLightIntensity": 190,
  "DirLightDiffuseFactor": 1.8,
  "DirLightSpecularFactor": 0.8,
  "DirLightGlossFactor": 0.8,
  "IndirectLightDiffuseFactor": 0.55,
  "IndirectLightSpecularFactor": 0.55,
  "AOIndirectLight": 0.7
}
```

Others: `ByblosEnvironmentRender_FrameSettingsOverrideDefinition`, `VerdureEnvironmentRender_FrameSettingsOverrideDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('FrameSettingsOverrideDefinitionObjectBuilder')
search_content('', type_contains='FrameSettingsOverrideDefinitionObjectBuilder')
```
