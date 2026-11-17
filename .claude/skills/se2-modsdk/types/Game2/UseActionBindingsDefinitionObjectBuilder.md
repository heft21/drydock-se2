# UseActionBindingsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseActionBindingsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyTypesMap` | Defines the use action associated to each dummy type |

## A real one

`Vanilla\Assets\System\UseActions\UseActionBindings.def`

```json
{
  "Guid": "67f792fb-986f-4e77-a7cb-effcbb91f24e",
  "DummyTypesMap": {
    "d3851495-11ad-4c70-a2e0-f77259b4d1a0": "f49a9b10-fe13-42f5-8bd8-dc32f98c4333",
    "b15d441f-88d0-4722-a377-7adfd75579e7": "9b5f3902-6c3c-401a-b715-3873b4a63ab3",
    "2193fd9c-28c1-4e86-b5c3-e4c695ecefe4": "a3412971-c399-4aac-a1c0-51318f411c7f",
    "504d93cd-9f8f-47b5-9be6-6fb633b93ee1": "a514581d-b771-4d51-9f37-abf0130000f1",
    "ec312376-e391-4426-8df3-1a894d5a305c": "9a797703-5cab-43bb-840a-8fb9aa4a4013",
    "29d45e5b-2ddf-4ba5-9031-885260550947": "d3f7336c-2ed2-4903-ac01-1aacbcfd931f",
    "18ebca70-b1ac-46e0-9965-a3dc257a21b4": "d3f7336c-2ed2-4903-ac01-1aacbcfd931f",
    "4511a2ef-912d-4980-adf2-47b1e8898190": "40de9e71-2e4c-4251-a27a-9e5c3448b718",
    "7645543e-1fd2-4076-842a-aa67433a38e0": "58383da5-f2ca-499c-a11d-b6d2809ae6fc",
    "7a0571aa-92bd-458a-a62f-718e5fd9838d": "72e1ac31-615e-47fe-aa63-35a0aea66a25",
    "27b943d5-f9e5-44d2-9c7e-8390c593e288": "7f2face5-7cac-4c07-87ad-dd6fc5def50b",
    "93e59227-2a9d-434e-8685-a94af2b2a04d": "44345673-e425-4347-80ab-4acfdeea716f",
    "267d0d3b-a684-4d5c-91a4-d910b9887a32": "32dcafce-fc08-4661-84da-b874a2afba9d",
    "3ff92195-75d4-4072-bb81-2a55d5e30119": "be2867f3-78b8-4a8d-95cc-9d35d788b68b",
    "c39b2ab3-7191-4279-82f8-d9dcd5271b84": "b6d0ee99-2dfe-443c-9e2d-63799cd3abb6",
    "a7594bb4-e821-4c38-bbb5-0d5c8926854b": "0414ed0a-fb59-495c-b138-8524768ebc34",
    "fc1624b3-2db3-4670-8202-d72a526cd958": "e576b9ea-e6cf-4447-92ab-edd56b5d25d3",
    "25e5525b-ad06-487f-b585-96c7a550c64e": "0a6bafe2-5acc-4757-91a5-a7466909e485",
    "51c3b94d-e1fa-4d52-8dd9-2acd162f2c9c": "58014378-278e-45b8-b386-d0d3257cab26",
    "cfbad847-947f-47f3-a910-fdbd432dbda8": "48f189e1-94fb-4005-9350-37afb5384015",
    "1268bd97-943d-4f5c-b679-10038cfc4f3b": "9b5f3902-6c3c-401a-b715-3873b4a63ab3",
    "f11a8a74-97a4-4e8c-a00f-1136e7f670bb": "8179c15b-3760-4e0d-98b2-b32204daab72"
  }
}
```

Others: `MapUseActionBindings`

---

Read it with the MCP server rather than by hand:

```
describe_type('UseActionBindingsDefinitionObjectBuilder')
search_content('', type_contains='UseActionBindingsDefinitionObjectBuilder')
```
