# InputManagerConfigurationObjectBuilder

`VRage:Keen.VRage.UI.InputManagerConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.UI`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivationBackspace` | Action definition for Backspace activation. |
| `ActivationDelete` | Action definition for Delete activation. |
| `ActivationEnter` | Action definition for Enter activation. |
| `ActivationEscape` | Action definition for Escape activation by the keyboard. |
| `ActivationSpace` | Action definition for Space activation. |
| `CopyText` | Action to copy selected text. |
| `CursorButton1` | Action definition for left button click. |
| `CursorButton2` | Action definition for right button click. |
| `CursorButton3` | Action definition for middle button click. |
| `CursorButton4` | Action definition for button 4 click. |
| `CursorButton5` | Action definition for button 5 click. |
| `CursorMove` | Action definition for cursor move. |
| `CutText` | Action to cut selected text. |
| `DefaultScreenClosingAction` | Assigned as a default action to close any screen. |
| `FullScreenToggle` | F12 key used only to open developer tools with shift modifier. |
| `HorizontalWheel` | Action definition for horizontal wheel analog input. |
| `ModifierAlt` | Action definition for the Left Alt key by the keyboard. |
| `ModifierControl` | Action definition for the Left Ctrl key by the keyboard. |
| `ModifierShift` | Action definition for the Left Shift key by the keyboard. |
| `NavigationDown` | Action definition for down navigation. |
| `NavigationEnd` | Action definition for End navigation. |
| `NavigationHome` | Action definition for Home navigation. |
| `NavigationLeft` | Action definition for left navigation. |
| `NavigationPageDown` | Action definition for PageDown navigation. |
| `NavigationPageUp` | Action definition for PageUp navigation. |
| `NavigationRight` | Action definition for right navigation. |
| `NavigationTab` | Action definition for tab navigation. |
| `NavigationUp` | Action definition for up navigation. |
| `OpenDevTools` | F12 key used only to open developer tools with shift modifier. |
| `PasteText` | Action to paste selected text. |
| `Redo` | Action to redo. |
| `SelectAllText` | Action to select all text in a textbox. |
| `TextBoxContext` | Input Context Definition for editable text boxes. |
| `Undo` | Action to undo. |
| `VerticalWheel` | Action definition for vertical wheel analog input. |

## A real one

`Engine\Assets\Configurations\Input\InputManagerConfiguration.def`

```json
{
  "Guid": "43d80c58-1c67-4156-afde-906af33795aa",
  "DefaultScreenClosingAction": "9cda2d89-202c-458e-bd48-32b7cf4a621f",
  "CursorMove": "daeab155-fd20-45c7-80c1-fa404e0b1259",
  "CursorButton1": "7866c6f7-9b4a-4e19-ab7b-4ebf445ead8a",
  "CursorButton2": "e295f1b1-b181-4cae-90cd-1f4f610e94c5",
  "CursorButton3": "ef782e4b-460c-4840-9d64-73fb078f32de",
  "CursorButton4": "ba6c0b60-2466-49d7-8aa7-455ef0252be6",
  "CursorButton5": "59451b35-915e-4257-84cf-dbee56e82a62",
  "VerticalWheel": "3129e85d-6f77-41f5-80b2-d4f93217797b",
  "HorizontalWheel": "bdd29ab4-2662-4377-8c5c-4581c045b63c",
  "NavigationUp": "eb1197bb-92fa-46af-98ee-d822504e241e",
  "NavigationDown": "8c13b974-2979-4936-9811-21810a677cdb",
  "NavigationLeft": "234928bc-b370-4103-8410-37da935f3581",
  "NavigationRight": "30ce4e7c-a4b6-4c1e-b4fa-d4fdfa8109b9",
  "NavigationTab": "0a982688-b711-43d5-9b3e-84f8f85bc647",
  "ActivationEnter": "8bc6ef33-831c-450b-bfba-7a6f9f41e324",
  "ActivationSpace": "c66646dc-46fe-411a-bdb4-03511ef9d6b3",
  "ActivationDelete": "375d522a-61cb-42b5-afa6-27e8f5855f05",
  "ActivationBackspace": "8b29050d-5ee8-4eb6-b11e-0a2c5b47d98c",
  "NavigationHome": "6592cb26-5015-445d-858a-f691f2dc4166",
  "NavigationEnd": "23f97a30-5b04-4262-822b-dbbcccee1f02",
  "NavigationPageDown": "76d6018e-be13-4361-b821-c5a9ae9a2486",
  "NavigationPageUp": "9ff13619-7fbf-4ddd-8564-9cc15a7af938",
  "ActivationEscape": "ea74a6d3-4fc2-40ca-9380-f07cd0ced386",
  "ModifierShift": "07464f61-6601-4a2b-859f-750b85933a60",
  "ModifierControl": "8efdd058-d2f0-457a-b12d-3f1104d5f7bf",
  "ModifierAlt": "c298d102-c4a2-4faf-9694-41cd7acf1f00",
  "OpenDevTools": "370e6000-7bf5-4d46-b919-ca2b31b02d55",
  "FullScreenToggle": "4ab5ff06-a25d-4647-a9fb-be9050d39a50",
  "SelectAllText": "e12b26dc-253e-41d4-91f7-4ee4a0434ff3",
  "CopyText": "3a3f2142-806e-4838-b779-efdbaf0c9ecc",
  "PasteText": "86fc3d07-ac0e-4193-bfa8-c427c050d50b",
  "CutText": "b424f2da-277c-44fc-99bc-535a25c1703b",
  "Undo": "358c4e38-4d8f-42f4-ad29-062a27612edf",
  "Redo": "4dfedf4a-4c00-43ad-867e-66afd8294393",
  "TextBoxContext": "077647ca-ac76-4a35-aa2f-0891610cba93"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InputManagerConfigurationObjectBuilder')
search_content('', type_contains='InputManagerConfigurationObjectBuilder')
```
