# InputAliasGroupsDefinitionObjectBuilder

`VRage:Keen.VRage.Input.InputAliasGroupsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AliasGroups` | A collection of grouped input actions, defining alias relationships between them. |

## A real one

`Vanilla\Assets\MainMenuData\Input\AliasGroups.def`

```json
{
  "Guid": "8077dd92-4d77-4f6a-97a0-a3c12db87f76",
  "AliasGroups": [
    {
      "$Key": "AliasJump",
      "$Value": [
        "fc7128fe-2609-4e1d-b501-e8c5051777d1",
        "383e31b2-7c33-45bb-8e6d-60505e3b1602"
      ]
    },
    {
      "$Key": "SpectatorSprint",
      "$Value": [
        "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
        "247b11d0-741a-4fd6-ad61-cb8684047def"
      ]
    },
    {
      "$Key": "ThirdPersonAliasGroup",
      "$Value": [
        "b03bdab2-0082-4c38-b272-c2156ab765f2",
        "6bdf56ee-2e25-43a0-9411-390abca020fa"
      ]
    },
    {
      "$Key": "BlockPlacerAliasGroup",
      "$Value": [
        "f4228ad4-ae27-42a8-8226-5e7143c404d2",
        "0d35492d-bac7-43a7-a174-85e62a5f163b",
        "a7bf55e2-53ed-420e-815b-0997ef423919",
        "c7703644-5f99-45fa-8efa-9ea3f07bd940",
        "0f354a10-4836-4810-a5e5-ee15a919522e",
        "fe1757c5-9882-4c68-88ab-bce9b2a2eead",
        "09ca1c38-5f67-4b2f-9ff1-bd6864a231a6",
        "24fcc4f0-0f90-4a2d-86bb-088de21c9ec4",
        "ddf51265-4f72-47cf-83e8-d57cf2d7d44e",
        "53fddb20-40d1-4cff-9388-ac3ef81ebd5c",
        "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
        "247b11d0-741a-4fd6-ad61-cb8684047def",
        "f5b943d0-ea84-4748-ac3c-6bf59da48a55",
        "ac46bf53-71ae-42e1-adf9-84f53a22adf4"
      ]
    },
    {
      "$Key": "AliasBlockRotationGamepad",
      "$Value": [
        "c7703644-5f99-45fa-8efa-9ea3f07bd940",
        "0f354a10-4836-4810-a5e5-ee15a919522e",
        "fe1757c5-9882-4c68-88ab-bce9b2a2eead",
        "09ca1c38-5f67-4b2f-9ff1-bd6864a231a6",
        "24fcc4f0-0f90-4a2d-86bb-088de21c9ec4",
        "ddf51265-4f72-47cf-83e8-d57cf2d7d44e"
      ]
    },
    {
      "$Key": "AliasCrouchDown",
      "$Value": [
        "5e4ea1d9-1ccb-4227-8a76-f54f384c2295",
        "d5ad431e-2d93-4570-937e-6388e2b42387"
      ]
    },
    {
      "$Key": "AliasBoost",
      "$Value": [
        "f4893db3-3a7c-415a-8b69-6aee4283515a",
        "70e8a38b-ee2b-4fc1-8edf-6da0e27607e0",
        "314f02e6-f6d4-4cc5-9497-4e175b3d2f50"
      ]
    },
    {
      "$Key": "BlockPlacerAliasGroup2",
      "$Value": [
        "f4228ad4-ae27-42a8-8226-5e7143c404d2",
        "0d35492d-bac7-43a7-a174-85e62a5f163b",
        "a7bf55e2-53ed-420e-815b-0997ef423919",
        "c7703644-5f99-45fa-8efa-9ea3f07bd940",
        "0f354a10-4836-4810-a5e5-ee15a919522e",
        "fe1757c5-9882-4c68-88ab-bce9b2a2eead",
        "09ca1c38-5f67-4b2f-9ff1-bd6864a231a6",
        "24fcc4f0-0f90-4a2d-86bb-088de21c9ec4",
        "ddf51265-4f72-47cf-83e8-d57cf2d7d44e",
        "53fddb20-40d1-4cff-9388-ac3ef81ebd5c",
        "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
        "247b11d0-741a-4fd6-ad61-cb8684047def",
        "f5b943d0-ea84-4748-ac3c-6bf59da48a55"
      ]
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InputAliasGroupsDefinitionObjectBuilder')
search_content('', type_contains='InputAliasGroupsDefinitionObjectBuilder')
```
