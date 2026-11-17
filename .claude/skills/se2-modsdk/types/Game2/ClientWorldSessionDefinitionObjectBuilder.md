# ClientWorldSessionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.CoreComponents.ClientWorldSessionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.CoreComponents`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockPlacerSessionDefinition` | to add to client on world init. |
| `DebugMenuSessionComponent` | to add to client session components on world init |
| `ExplosionVisualsDefinition` | to add to client session components on world init |
| `GPSMarkersSessionDefinition` | to add to client session components on world init |
| `HotKeySessionComponent` | to add to client session components on world init |
| `PlayerToolbarStateComponentDefinition` | to add to client session components on world init |
| `ProjectileVisualsDefinition` | to add to client session components on world init |
| `SessionInGameUIDefinition` | to add to client session components on world init |
| `SpectatorInputSessionComponent` | to add to client session components on world init |

## A real one

`Vanilla\Assets\System\WorldClient.def`

```json
{
  "Guid": "573837ee-0302-4880-9ab0-8af2da013a24",
  "ProjectileVisualsDefinition": "7ae481b5-af05-42c5-9241-6f2c2e5d6c50",
  "ExplosionVisualsDefinition": "01b1e1b9-cb92-4277-bf66-820d08da3387",
  "SpectatorInputSessionComponent": "af11e5fc-cddf-417d-a11c-32be80bb40c6",
  "BlockPlacerSessionDefinition": "1d1b914a-c610-41d3-a40d-718de5230d96",
  "DebugMenuSessionComponent": "c4e3d293-3c21-47a5-9be8-4e4cc9e54e4d",
  "HotKeySessionComponent": "392e0631-7559-4b07-9403-4151b7a9684b",
  "SessionInGameUIDefinition": "dd1d1cf4-ec81-44d6-99d2-42a827b9f8f1",
  "GPSMarkersSessionDefinition": "7346601e-d0be-49a0-8778-fa57dcb6017d",
  "PlayerToolbarStateComponentDefinition": "1a9a70d9-7842-4a9f-a790-a68eafc21c5e",
  "DecalSessionDefinition": "a30a2165-f655-4bfc-b5bd-6027286a7954"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ClientWorldSessionDefinitionObjectBuilder')
search_content('', type_contains='ClientWorldSessionDefinitionObjectBuilder')
```
