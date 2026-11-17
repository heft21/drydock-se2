# MeteorEffectsRenderComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Weather.MeteorEffectsRenderComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InAtmosphereParticleEffects` | Looping meteor particle/audio effects used when the meteor is inside a non-zero atmosphere (e.g., entry burn, smoke trail, sparks). One effect is randomly selected at init time. |
| `InSpaceParticleEffects` | Looping meteor particle/audio effects used when the meteor is in vacuum / no atmosphere (e.g., space trail / glow without atmospheric burn). One effect is randomly selected at init time. |

## A real one

`Vanilla\Assets\System\Weather\MeteorEffectsRenderComponentDefinition.def`

```json
{
  "Guid": "f6d4d4f3-6963-40c3-b7e7-a6879d75877b",
  "InAtmosphereParticleEffects": {
    "_data": [
      {
        "Key": "36132b10-49fd-4292-a934-110946bea99c",
        "Value": "9e32f394-4a94-4c14-a3c8-3ac419d4cde5"
      },
      {
        "Key": "7ffb32e2-bb6c-4121-af1f-9d2931427092",
        "Value": "7a710048-91d4-4472-914b-60d474729103"
      },
      {
        "Key": "dc7af492-b832-472a-ada1-68131b219941",
        "Value": "f0bf87f8-e638-459b-ade3-9317bf8fec48"
      },
      {
        "Key": "af3d514f-ef2a-4348-9685-826ee2a9f677",
        "Value": "42f40cff-ba3a-49da-b1ea-a2bd97445752"
      }
    ]
  },
  "InSpaceParticleEffects": {
    "_data": [
      {
        "Key": "3fe5f9db-4aeb-44bc-855f-8d489d287263",
        "Value": "b3e20d3b-d93e-4193-a222-b2f9af00c787"
      },
      {
        "Key": "7676b909-3e38-4ca4-b2fc-19220b6b7221",
        "Value": "2a9fb4a0-c38f-4d4c-a42c-db051c110a5e"
      },
      {
        "Key": "59646479-55d8-44ea-a39d-a14b2995f941",
        "Value": "2fe8aeaf-e027-481f-ad83-46dbded464a2"
      },
      {
        "Key": "65dbcc1e-dffa-4b04-8a06-17251d8ec0cd",
        "Value": "b734d195-84ba-4b48-93ea-f61452704acb"
      }
    ]
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MeteorEffectsRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='MeteorEffectsRenderComponentDefinitionObjectBuilder')
```
