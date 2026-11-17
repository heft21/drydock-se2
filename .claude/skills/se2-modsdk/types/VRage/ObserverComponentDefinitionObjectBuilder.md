# ObserverComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.Observers.ObserverComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.Observers`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InfluenceRadius` | Our intereset radius, centered around observer position |
| `Tags` | Tags we should use when registering as an observer |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\CameraObserver.def`

```json
{
  "Guid": "60baa8b2-89b4-4e10-a4c4-81d82ecb6fa3",
  "Tags": [
    {
      "Key": "0ab790b1-8481-44c4-b2d3-a3b116bb0217",
      "Value": "VoxelObserver"
    },
    {
      "Key": "edda5119-04a3-4f59-b3e0-01ab2fc4d028",
      "Value": "PhysicsObserver"
    },
    {
      "Key": "d9f21622-ef9f-4aa7-b223-b15dc619f2b5",
      "Value": "AICameraObserver"
    },
    {
      "Key": "d89c8341-c2a3-4d0b-8587-590603227d33",
      "Value": "AnimationObserver"
    },
    {
      "Key": "9a315688-de6c-45a3-971c-645839a74389",
      "Value": "VisualEffectsObserver"
    },
    {
      "Key": "f31de150-739b-41aa-b673-a0102e828cd8",
      "Value": "ClosestPlanetObserver"
    },
    {
      "Key": "4bc59fa9-c7ee-45ff-8fa1-e18c2ed1340b",
      "Value": "TrashRemovalObserver"
    },
    {
      "Key": "24611e2e-dce7-4d9d-9dcd-9553ea15c432",
      "Value": "MissionObserver"
    },
    {
      "Key": "43dd6162-1aee-4d4b-a5b0-6ddfae85bee2",
      "Value": "DebugMenuObserver"
    },
    {
      "Key": "74df2653-be8c-4dbd-8d69-e925ba074443",
      "Value": "ProjectileObserver"
    },
    {
      "Key": "b5dfc1d1-5b0b-491e-9cf5-3e107b148334",
      "Value": "SensorObserver"
    }
  ],
  "InfluenceRadius": 200
}
```

Others: `PlanetWithAtmosphere_Client_ObserverComponentDefinition`, `PlanetWithoutAtmosphere_Client_ObserverComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ObserverComponentDefinitionObjectBuilder')
search_content('', type_contains='ObserverComponentDefinitionObjectBuilder')
```
