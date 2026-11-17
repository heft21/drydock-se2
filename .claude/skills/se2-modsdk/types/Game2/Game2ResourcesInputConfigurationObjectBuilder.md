# Game2ResourcesInputConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Resources.Game2ResourcesInputConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Resources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `NextScreen` | Input to switch to next available Tier 1 tabs on () |
| `NextTab` | Input to switch to next available Tier 2 tabs on () |
| `PreviousScreen` | Input to switch to next available Tier 1 tabs on () |
| `PreviousTab` | Input to switch to previous available Tier 2 tabs on () |
| `SelectTile` | Select specific tile in the active toolbar (e.g. 1, 2, 3, 4...) |
| `SelectToolbar` | Select specific toolbar index |

## A real one

`Vanilla\Assets\MainMenuData\UI\Screens\Game2ResourcesInputConfiguration.def`

```json
{
  "Guid": "e8cbfc72-aaac-414f-92c2-8ff4c05e737a",
  "NextTab": "fa223179-bcf2-4659-a62a-a52fc6604bd9",
  "PreviousTab": "b572184c-a32e-48ea-b9e8-41795ed0a56c",
  "NextScreen": "1d2497e3-fc76-4471-a9e6-9742d64d4849",
  "PreviousScreen": "968480f4-fb2a-4e57-8a13-e46e456733d9",
  "SelectTile": [
    {
      "Key": "391ab319-1de0-4bf6-b48d-185d8b5ae363",
      "Value": "29f5de7c-d264-4515-943d-c51234a6b4c7"
    },
    {
      "Key": "6dce8dbd-70a7-4f3d-ac5b-68af85029c1c",
      "Value": "21a291b2-5b04-4c38-9923-1293d1f1643f"
    },
    {
      "Key": "e4e5fce3-6817-432e-8484-f5a0952e04f3",
      "Value": "3ba7e14c-73d1-4460-b338-0f36464da1a1"
    },
    {
      "Key": "4ace00dc-35ea-4dcd-8eab-82b6a1b5e4b9",
      "Value": "e0c48586-05b7-4bc3-8c7c-73d9267cfadc"
    },
    {
      "Key": "89bd397f-e490-41f5-afe2-07278ecc8b60",
      "Value": "83e36ff2-83af-46eb-82df-43f0c782a9ed"
    },
    {
      "Key": "d5b8a216-96c0-4f53-b56b-e6e1a7a04408",
      "Value": "827b4567-a4eb-48a9-bfc6-9843c164e7fb"
    },
    {
      "Key": "1dbff17a-5039-4b96-a79a-f0700057e8cc",
      "Value": "0bd3fbcb-f528-4fdd-8ec8-2446303ded8b"
    },
    {
      "Key": "7a57abbc-60c5-4491-b97b-67caaaa7c282",
      "Value": "bf70b74c-29cb-4f51-8332-b61b2f94b170"
    },
    {
      "Key": "57dedb98-8e5a-4011-bb28-a5279b31f8bf",
      "Value": "34ab5f98-f36f-4220-8d5f-7ae1d65b0e03"
    },
    {
      "Key": "c16db72b-683a-4cbf-a3b2-e5c8456d5bf4",
      "Value": "70a43f30-6724-4fc4-ad71-3994602a176b"
    }
  ],
  "SelectToolbar": [
    {
      "Key": "c0de2c83-31ee-42ea-87cb-cc09049bd1e5",
      "Value": "81e8de19-5e7e-47b4-9f1b-1e7451416c70"
    },
    {
      "Key": "8b2ec944-e245-474b-8950-63fd9727a0d1",
      "Value": "cf4585e0-02e9-4867-b7c5-afe4783988ff"
    },
    {
      "Key": "3ff9dde5-0274-47fc-aeba-7e558f65f4ce",
      "Value": "c7b89e9d-be8b-4695-b709-bf878690dfb3"
    },
    {
      "Key": "ada021ca-8c40-4756-8135-f0f20bd479be",
      "Value": "1499e456-d417-43ac-8518-aca55553b3db"
    },
    {
      "Key": "fc0f47f6-d9a7-499a-97b9-d0045e47b520",
      "Value": "845b8149-fe0c-4892-9ec1-e63bfb635d82"
    },
    {
      "Key": "02df41d5-c52e-496f-bb4e-b33bc5cf686f",
      "Value": "e6762652-48b8-48db-8014-5dc293b6ea5b"
    },
    {
      "Key": "a277ddd9-5c31-49b3-817c-736cd02a74cd",
      "Value": "b284b8c6-40d9-4c09-bb5e-2b8067093080"
    },
    {
      "Key": "a02e318b-0800-43fc-b666-efc7085bdeff",
      "Value": "f979d728-ecdd-4cd8-b2ab-0c1389f562e0"
    },
    {
      "Key": "f700fa2a-7b51-45a3-ac2a-bf02da62c02a",
      "Value": "05629f4a-2a2c-4ce4-b46b-2f93bcd9afc9"
    },
    {
      "Key": "a563a089-3d17-40a1-8130-428a95aaa9e0",
      "Value": "8c107209-e7a5-4843-9455-9804011200e0"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('Game2ResourcesInputConfigurationObjectBuilder')
search_content('', type_contains='Game2ResourcesInputConfigurationObjectBuilder')
```
