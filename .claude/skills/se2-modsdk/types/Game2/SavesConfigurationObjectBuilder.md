# SavesConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Saves.SavesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Saves`
- definitions using it: **1**

## What it is

Migrations for saves configuration object builder

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InaccessibleFilesFailureMessage` | Localization id of text message shown when saving failed due to inaccessible files |
| `InvalidCharactersNameFailureMessage` | Localization id of text message shown when saving failed due to invalid characters in name |
| `LoadCompletedTimeOut` | How long the re/loading completed message is shown |
| `LoadStartedTimeOut` | How long the re/loading started message is shown |
| `LoadingBackupCompletedMessage` | Localization id of text message shown when loading completes |
| `LoadingCompletedMessage` | Localization id of text message shown when loading completes |
| `LoadingStartedMessage` | Localization id of text message shown when loading starts |
| `LostDataMessage` | Localization id of text message shown when issues happened during loading |
| `LostGridMessage` | Localization id of text message shown when issues happened during Grid loading |
| `LostTilesMessage` | Localization id of text message shown when issues happened during Toolbar loading |
| `MaxThumbnailSize` | Max size of the thumbnail for the save screenshot |
| `PrefixedNameFailureMessage` | Localization id of text message shown when saving failed due to use of reserved prefix |
| `ReloadingCompletedMessage` | Localization id of text message shown when reloading completes |
| `ReloadingStartedMessage` | Localization id of text message shown when reloading starts |
| `ReservedNameFailureMessage` | Localization id of text message shown when saving failed due to name being reserved |
| `SaveCompleteMessage` | Localization id of text message shown when saving is completed |
| `SaveCompleteTimeOut` | How long the save complete message is shown |
| `SaveFailedTimeOut` | How long the failure message is shown |
| `SaveNameCollisionResolutionSuffix` | Localization id of text that should be appended to the end of save name in case the colliding names. |
| `SavesMessageTitle` | Localization id of text message title shown when the player is notified about saving state |
| `SavingAlreadyInProgressMessage` | Localization id of text message shown when trying to save while already saving game |
| `SavingFailureMessage` | Localization id of text message shown when saving failed for unknown reason |
| `SavingMessage` | Localization id of text message shown when saving |
| `SavingTimeOut` | How long the saving message is shown. Deleted when saving is completed |

## A real one

`Vanilla\Assets\UI\SavesConfiguration.def`

```json
{
  "Guid": "dae3b120-c4b6-421c-bfa5-371448435c82",
  "SavesMessageTitle": "SavesMessageTitle",
  "SavingMessage": "SavesSaving",
  "SaveCompleteMessage": "SavesSaveComplete",
  "SavingFailureMessage": "SavesGeneralFailure",
  "PrefixedNameFailureMessage": "SavesPrefixedNameFailure",
  "ReservedNameFailureMessage": "SavesReservedNameFailure",
  "InvalidCharactersNameFailureMessage": "SavesInvalidCharacterNameFailure",
  "InaccessibleFilesFailureMessage": "SavesInacessibleFilesFailure",
  "DiskFullFailureMessage": "SavesDiskFullFailure",
  "SaveInterruptedMessage": "SavesInterrupted",
  "SavingTimeOut": 600000000,
  "SaveCompleteTimeOut": 50000000,
  "SaveFailedTimeOut": 150000000,
  "LoadingStartedMessage": "SavesLoadingStarted",
  "ReloadingStartedMessage": "SavesReloadingStarted",
  "LoadingCompletedMessage": "SavesLoadingCompleted",
  "LoadingBackupCompletedMessage": "SavesLoadingBackupCompleted",
  "ReloadingCompletedMessage": "SavesReloadingCompleted",
  "LostDataMessage": "SaveLoadedWithIssues",
  "LostGridMessage": "LostGridBlocksMessage",
  "LostTilesMessage": "LostToolbarTilesMessage",
  "LoadStartedTimeOut": 600000000,
  "LoadCompletedTimeOut": 100000000,
  "SavingAlreadyInProgressMessage": "SavesSavingInProgress",
  "SaveNameCollisionResolutionSuffix": "SaveNameCollisionResolutionSuffix",
  "MaxThumbnailSize": {
    "X": 1920,
    "Y": 1080
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SavesConfigurationObjectBuilder')
search_content('', type_contains='SavesConfigurationObjectBuilder')
```
