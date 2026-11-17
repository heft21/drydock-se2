# EntityMigrationsDefinitionObjectBuilder

`VRage:Keen.VRage.DCS.Definitions.EntityMigrationsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.DCS.Definitions`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Migrations` | Key = From, Value = To GUIDs of s |
| `Version` | The maximum version these migrations will be applied. When the save's version is less than this version, the changes will apply. |

## A real one

`Vanilla\Assets\System\Migrations\EntityMigrations_0_10_93.def`

```json
{
  "Guid": "5c7250a1-28be-443a-9bdc-3e75f187848f",
  "Migrations": {
    "362e7bad-e89d-4f5c-a5e1-2291da473986": "2e81ca26-3a7c-464f-b272-7749713bb36c",
    "630c8170-73b9-4328-8c57-6cab3c8a8386": "7f8c0f48-75b6-4bae-a5f9-3fdb1ea0a9ab",
    "1e33c409-0100-4a68-a6ab-7f9b6f764fc8": "dab2500d-1deb-4298-a9d8-bacaa7da62f9",
    "999f0403-aa64-4d63-acf1-4f4e12d62098": "ab1b563b-1615-4288-95f9-9bcc1183bc6d",
    "d55fcb4d-8fdc-4060-ba5e-bc9471ed1840": "35c0fbcc-4ee9-465c-9b01-411a4c5bac28",
    "97eeea7b-a1ad-4daf-9e85-33008e9571e9": "550799ee-27b4-4492-86dd-56c551ed7293",
    "34f5e113-bcae-484a-a6d0-34bd985de293": "a5bfb503-be82-4fff-9c2c-935d64e1d228",
    "dbf0f0cb-4d64-492e-b960-34d95af76734": "49113e4b-17b8-4122-8db0-d9dcfdb87e9c"
  },
  "Version": "0.10.0.93"
}
```

Others: `EntityMigrations_0_10_0_2`, `EntityMigrations_0_10_0_5`

---

Read it with the MCP server rather than by hand:

```
describe_type('EntityMigrationsDefinitionObjectBuilder')
search_content('', type_contains='EntityMigrationsDefinitionObjectBuilder')
```
