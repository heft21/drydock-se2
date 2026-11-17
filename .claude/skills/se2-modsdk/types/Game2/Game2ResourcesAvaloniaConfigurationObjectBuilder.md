# Game2ResourcesAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Resources.Game2ResourcesAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Resources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BigKeenLogo` | Big Keen Logo |
| `BigKeenLogoShadow` | Big Keen Logo Shadow |
| `ButtonXLBackground` | Background for Extra Large Button in Game |
| `ButtonXLBackgroundDisabled` | Background for Extra Large Button in Game when disabled |
| `ButtonXLBackgroundHover` | Background for Extra Large Button in Game when pointer over it |
| `ButtonXLBackgroundPressed` | Background for Extra Large Button in Game when Pressed |
| `ExampleImage1` | Example image for Help Screen |
| `ExampleImage2` | Example image for Help Screen |
| `ExampleImage3` | Example image for Help Screen |
| `ExampleImage4` | Example image for Help Screen |
| `GameLogo` | Game Logo |
| `GameLogoShadow` | Game Logo Shadow |
| `KeenBadge` | Small Badge with Keen Logo |
| `KeenLogo` | Keen Logo |
| `PreciseControlButtonBackground` | Background for buttons of Precise Controls |
| `PreciseControlButtonBackgroundFlipped` | Flipped version of the Background for buttons of Precise Controls |
| `PreciseControlButtonFrame` | Frame for buttons of Precise Controls |
| `PreciseControlButtonFrameFlipped` | Flipped version of the Frame for buttons of Precise Controls |
| `PreciseControlMainBackground` | Background for Main part of Precise Controls |
| `PreciseControlMainFrame` | Frame for Main part of Precise Controls |
| `SearchBarBackground` | Background for the Search Bar |
| `SearchBarFrame` | Frame for the Search Bar |
| `SearchBarFrameActive` | Active Frame for the Search Bar |
| `SettingsWindowFrame` | Pre-Stretched Frame for Settings window, to allow placement of TabItem |
| `Signature` | Help Screen Signature Image |
| `SmallToggleButtonBackground` | Background for Small Toggle Button in Game |
| `SmallToggleButtonBackgroundActive` | Background for Small Toggle Button in Game when Active |
| `SmallToggleButtonBackgroundDisabled` | Background for Small Toggle Button in Game when disabled |
| `SmallToggleButtonBackgroundHover` | Background for Small Toggle Button in Game when pointer over it |
| `SmallToggleButtonBackgroundPressed` | Background for Small Toggle Button in Game when Pressed |
| `ToggleSwitchBackground` | Background for ToggleSwitches in Game |
| `TooltipDelay` | Value indicating the Time, in milliseconds, before a ToolTip opens. |
| `TrashCanDisabledIcon` | Icon of a disabled Trash-Can |
| `TrashCanIcon` | Icon of a Trash-Can |
| `Vignette` | Vignette for screens |
| `WindowFrame` | Frame for in Game Window |

## A real one

`Vanilla\Assets\MainMenuData\UI\Game2ResourcesAvaloniaConfiguration.def`

```json
{
  "Guid": "0d353e28-6913-4f4f-98b5-64429b536e80",
  "TooltipDelay": 500,
  "GameLogo": "{G}bcc1ab37-f3b2-45d7-b67b-08e7e17666b4",
  "GameLogoShadow": "{G}01dd490b-ba67-4324-ab86-71adeb865185",
  "KeenLogo": "{G}4e48c3a3-23bb-4bfe-86d4-6ec3595b79bc",
  "BigKeenLogo": "{G}8e263e6b-9a81-48f6-976c-1a9ed8f77707",
  "BigKeenLogoShadow": "{G}b1cffee0-8e6b-4cf0-96d9-c4a427f83791",
  "KeenBadge": "{G}e5d91627-3a2c-4de2-b752-48544f3710e0",
  "Signature": "{G}db5de3d2-afce-4704-91bf-2bd2a36b14a4",
  "Vignette": "{G}ea616e8c-5aa6-499e-b417-d69009447294",
  "WindowFrame": "{G}5d380d83-ee90-450d-a126-07825b37b605",
  "TrashCanIcon": "{G}709a035d-2036-4fb7-8fda-817fb8363a5a",
  "TrashCanDisabledIcon": "{G}8472e933-5cf8-4062-b615-1bc95b30a8db",
  "ExampleImage1": "{G}ab235b7b-275a-4bd4-8878-ec9f872f8ed6",
  "ExampleImage2": "{G}8d66aefb-db84-4c8a-9144-3ed355196061",
  "ExampleImage3": "{G}8a35a9a4-0d7f-46a4-b1cd-a686d50a9a8f",
  "ExampleImage4": "{G}0feaebbf-2e67-40db-9789-b02b80989214"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('Game2ResourcesAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='Game2ResourcesAvaloniaConfigurationObjectBuilder')
```
