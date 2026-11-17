# CharacterSkinColorConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterSkinColorConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ColorsLabel` | Label of the colors button in the quick menu |
| `DefaultColors` | Default color palette that can be selected. |
| `QuickMenu` | Definition for the skin color selection quick menu. |
| `SkinsLabel` | Label of the skins button in the quick menu |

## A real one

`Vanilla\Assets\Characters\System\CharacterSkinColorConfiguration.def`

```json
{
  "Guid": "d83c93b9-4313-489e-aa45-daed7f1a6a06",
  "DefaultColors": [
    {
      "Key": "e181f074-1d18-4a45-a1f2-3e69d1474337",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 1,
          "Z": 0,
          "W": 1
        }
      }
    },
    {
      "Key": "15d2ac03-a8b7-402c-8e8c-e9e2250a93fe",
      "Value": {
        "Values": {
          "X": 0.33333334,
          "Y": 0,
          "Z": 0.14901961,
          "W": 1
        }
      }
    },
    {
      "Key": "84b63b1f-31dc-4e5d-ac47-0fa4620ba976",
      "Value": {
        "Values": {
          "X": 0.8333333,
          "Y": 0,
          "Z": 0.4509804,
          "W": 1
        }
      }
    },
    {
      "Key": "e517eb13-a08d-4d11-9795-494c6003e2df",
      "Value": {
        "Values": {
          "X": 0.8333333,
          "Y": 0,
          "Z": 0.8509804,
          "W": 1
        }
      }
    },
    {
      "Key": "26a27360-c1cf-4b8a-a271-426adf726645",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 1,
          "W": 1
        }
      }
    },
    {
      "Key": "cf2674cd-8bca-4e6d-b660-ab6751294045",
      "Value": {
        "Values": {
          "X": 0.122047246,
          "Y": 0.7016574,
          "Z": 0.70980394,
          "W": 1
        }
      }
    },
    {
      "Key": "1ee48f83-0ddf-482e-8ce3-4cd3d59246a8",
      "Value": {
        "Values": {
          "X": 0.12182741,
          "Y": 0.8491379,
          "Z": 0.9098039,
          "W": 1
        }
      }
    },
    {
      "Key": "9ab555ed-f25a-47f6-9513-88163078a9e9",
      "Value": {
        "Values": {
          "X": 0.576087,
          "Y": 0.8,
          "Z": 0.4509804,
          "W": 1
        }
      }
    },
    {
      "Key": "d1037b0f-f211-4578-baed-c390591794ca",
      "Value": {
        "Values": {
          "X": 0.5748945,
          "Y": 0.95180726,
          "Z": 0.6509804,
          "W": 1
        }
      }
    },
    {
      "Key": "d52de688-7731-46cc-94a7-dfdcdee8ed75",
      "Value": {
        "Values": {
          "X": 0.33333334,
          "Y": 0.31372547,
          "Z": 0.2,
          "W": 1
        }
      }
    },
    {
      "Key": "d0d9ddd4-5262-4fac-8ef7-eadff8a73242",
      "Value": {
        "Values": {
          "X": 0.33333334,
          "Y": 0.4705882,
          "Z": 0.4,
          "W": 1
        }
      }
    },
    {
      "Key": "4fb7b8ba-c8fa-484c-86e0-50074cf2a675",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0.8046875,
          "Z": 0.5019608,
          "W": 1
        }
      }
    },
    {
      "Key": "59949386-f263-4fa8-9e52-a88491bbf0b3",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0.9494382,
          "Z": 0.69803923,
          "W": 1
        }
      }
    }
  ],
  "QuickMenu": "183da096-9d49-4d8c-9954-7c00153ed90e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterSkinColorConfigurationObjectBuilder')
search_content('', type_contains='CharacterSkinColorConfigurationObjectBuilder')
```
