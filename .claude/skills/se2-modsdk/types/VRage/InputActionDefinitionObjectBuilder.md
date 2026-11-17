# InputActionDefinitionObjectBuilder

`VRage:Keen.VRage.Input.InputActionDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **252**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Category` | Customization category for this action. |
| `DefaultAnalogValue` | Default analog value assigned when an analog action is mapped to a digital input. |
| `DefaultInputControls` | Default input controls associated with this action. Used when no custom controls are defined. |
| `DisplayName` | A user-friendly name for this action. |
| `ExpectedInputType` | Input type that is expected for this action. Determines how input values are interpreted and matched to the action. Analog inputs to be bound to digital and vice versa. Pointer inputs are never converted. |
| `Name` | The unique identifier for this input action. Used to reference input actions in screens or other contexts where direct object references are unavailable. |
| `Reactivate` | Allows input controls bound to this action to reset and reactivate immediately when the input context changes. When disabled, controls bound to keys remain active as long as the key is held down, even if the input context is deactivated, potentially blocking other inputs. Enabling this forces controls to re-activate immediately after context deactivation, as if the key were momentarily released, allowing quick response to new input contexts. Typically useful for pointer controls to ensure seamless responsiveness. |
| `Unfiltered` | Indicates whether control filtering is skipped for input controls bound to this action. Enabling this will make the bound controls bypass the filtering. |

## A real one

`Engine\Assets\Data\Input\UI\Keyboard\Redo.def`

```json
{
  "Guid": "4dfedf4a-4c00-43ad-867e-66afd8294393",
  "Name": "Redo",
  "DisplayName": "Redo",
  "ExpectedInputType": "Digital",
  "DefaultAnalogValue": 1,
  "Unfiltered": false,
  "Reactivate": false,
  "Category": "5e15cdd3-26f1-49ef-b608-9cd9db938903",
  "DefaultInputControls": [
    {
      "$Type": "VRage:Keen.VRage.Input.DigitalCompositeInputControlBuilder",
      "MainInput": {
        "$Type": "VRage:Keen.VRage.Input.DigitalControlBuilder",
        "InputId": "Keyboard::Y"
      },
      "Modifiers": [
        {
          "$Type": "VRage:Keen.VRage.Input.DigitalControlBuilder",
          "InputId": "Keyboard::Control"
        }
      ]
    }
  ]
}
```

Others: `Undo`, `CycleTabs`

---

Read it with the MCP server rather than by hand:

```
describe_type('InputActionDefinitionObjectBuilder')
search_content('', type_contains='InputActionDefinitionObjectBuilder')
```
