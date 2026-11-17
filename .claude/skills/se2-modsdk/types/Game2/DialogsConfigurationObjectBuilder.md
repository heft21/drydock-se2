# DialogsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.DialogsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs`
- definitions using it: **1**

## What it is

Dialogs Configuration Object Builder

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AdapterChangedDialog` | Confirm adapter changed dialog |
| `AdapterDriverOutOfDateDialog` | Notify the user that the selected adapter doesn't have an up to date driver and can't be used |
| `AddMarkerDialog` | Dialog that opens when adding a marker on colonization map |
| `ApplyingChangesToSave` | Preparing blueprint for placing |
| `AudioNotLoadedConfirmationDialog` | Confirm pending changes in options |
| `BatteryPowerWarningDialog` | Warn the player that the device is on battery power, where GPU performance is usually reduced |
| `BestAdapterNotPickedDialog` | Notify the user that he's not using the best adapter |
| `BlueprintLoadingFailedDialog` | Blueprint could not load |
| `BlueprintMaxPCUDialog` | Blueprint exceeds the maximum world PCU |
| `BlueprintNotFoundDialog` | Blueprint not found |
| `BlueprintScreenshotSavingFailureDialog` | Blueprint screenshot failed to save |
| `CharacterRespawnConfirmationDialog` | Confirm manual respawning of the character |
| `CloseBlueprintDetailsDialog` | Confirm back from blueprint details |
| `ConfirmDeleteAsteroidDialog` | Confirmation of manual deletion of an asteroid. |
| `ConfirmDeleteBlueprintDialog` | Confirm deleting of blueprint |
| `ConfirmDeleteSaveDialog` | Confirm deleting of save |
| `ConfirmDiscardBlueprintDialog` | Confirm discarding of blueprint |
| `ConfirmDiscardNewBackupDialog` | Confirmation of discarding new backup |
| `ConfirmDiscardWorldSettingsDialog` | Confirmation of discarding world setting |
| `ConfirmExitDialog` | Confirm exit dialog |
| `ConfirmLoadBackupWithoutSaving` | Confirmation of discarding new backup |
| `ConfirmQuickLoadDialog` | Confirm quick-load game dialog |
| `ConfirmSaveOverwriteDialog` | Confirm overwriting of existing save |
| `ConfirmUnsubscribeBlueprintDialog` | Confirm unsubscribing from blueprint |
| `ConfirmWithoutSavingNewModsDialog` | Confirmation of discarding new mods |
| `DatapadDialogDefinition` | Definition for a datapad dialog |
| `DebugMenuConfirmationDialog` | Confirm dialog when enabling Debug Menu |
| `DeleteMarkerDialog` | Dialog that opens when deleting a marker on the colonization map |
| `DeleteMarkersDialog` | Dialog that opens when deleting markers on the colonization map |
| `DiscardModsChangesDialog` | Confirmation of discarding new mods |
| `DisplaySettingsChangeFailedDialog` | Notify that display settings change could not be applied due to overlay software preventing swapchain recreation |
| `DisplaySettingsChangedDialog` | Confirm resolution changed dialog |
| `ErrorLoadingModsDialog` | Error loading mods dialog |
| `GameServiceNotAvailableDialog` | Inform about a game service (e.g. Steam) being unavailable. |
| `GpuRequirementsNotMet` | Notify GPU is below requirements |
| `InputCompositionDialog` | Dialog for rebinding input controls |
| `LoadGameWithDebugMenuConfirmationDialog` | Confirmation dialog shown when loading a game with Debug Menu enabled |
| `LoadGameWithUpdatedMods` | Dialog for confirmation whether to load game with updated mods |
| `LoadingFailedCorruptedFilesDialog` | Failed to load the world dialog but when corrupted is detected |
| `LoadingFailedDialog` | Failed to load the world dialog |
| `LoadingFileCorruptedDialog` | Corrupted file on load dialog |
| `LoadingNewerSaveCofirmationDialog` | Confirmation whether continuing to load save from more recent version. |
| `LoadingNewerSaveDialog` | Warning that a save from newer version is being loaded |
| `LoadingNewerSaveFailedDialog` | Failed to load the world due to it being from newer version dialog |
| `MinimumHardwareRequirementsWarningDialog` | Confirm not meeting minimum hardware requirements |
| `MissingSaveDialog` | Save cannot be loaded due to it missing |
| `NonSSDDriveDetectedWarningDialog` | Inform the player about using a non-SSD drive |
| `NumericInputDialog` | Dialog for numeric input via Ctrl+LMB on a slider in the Control Panel. |
| `PendingChangesConfirmationDialog` | Confirm pending changes in options |
| `PreparingForPlaceBlueprintDialog` | Preparing blueprint for placing |
| `PreparingWorldForPublishDialog` | Preparing Local World for publishing |
| `RatingDialog` | Rating dialog |
| `RenameMarkerDialog` | Dialog that opens when renaming a marker on the colonization map |
| `SaveBeforeLoadDialog` | Save before load another game dialog |
| `SaveBeforeQuitDialog` | Save before quit game dialog |
| `SaveFailureAlreadyInProgressDialog` | Failure on a manual save due to save being already in progress |
| `SaveFailureDialog` | Failure on a manual save |
| `SaveFailureExternalSaveDialog` | Failure on a manual save due to save being read only |
| `SaveFailureInaccessibleFilesDialog` | Failure on a manual save due to files being inaccessible |
| `SaveFailureInvalidCharactersDialog` | Failure on a manual save due to invalid characters in name |
| `SaveFailurePrefixedNameDialog` | Failure on a manual save due to name containing reserved prefix |
| `SaveSuccessfullyDialog` | Confirmation of a manual save |
| `SavingDialog` | A loading dialog displayed during saving processes |
| `TextPanelEditDialog` | Dialog for editing LCD panel title and text content. |
| `ToolbarActionDialog` | Dialog shown when entering Edit Actions mode in Control Panel, explaining how to assign actions to toolbar slots. |
| `UGCDeleteConfirmationDialog` | Confirmation for deleting a UGC item |
| `UGCDeletingDialog` | Dialog for deleting content from workshop |
| `UGCPublishConfirmationDialog` | Confirm publishing of UGC Item |
| `UGCPublishFailureDialog` | Failure in publishing UGC item |
| `UGCPublishFailureEulaNotAcceptedDialog` | Failure in publishing UGC item, due to eula not being accepted. |
| `UGCPublishFailureInvalidRequestDialog` | Failure in publishing UGC item, due to an invalid request. |
| `UGCPublishFailureLimitExceededDialog` | Failure in publishing UGC item, due to exceeding the limit. |
| `UGCPublishFailureNotFoundDialog` | Failure in publishing UGC item, due to file not found. |
| `UGCPublishFailureServiceInactiveDialog` | Failure in publishing UGC item, due to service being inactive. |
| `UGCPublishFailureWorldSavingFailedDialog` | Failure in publishing UGC item, due to world saving failure. |
| `UGCPublishSuccessDialog` | Success in publishing UGC item |
| `UGCRepublishConfirmationDialog` | Confirmation for replacing an existing UGC item |
| `UGCUploadingDialog` | Dialog for uploading content for workshop |
| `UnspecifiedDriveWarningDialog` | Inform the player about being unable to detect a disk drive they are using. |
| `UrlWarningDialog` | Confirm opening of url in an external browser |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\DialogsConfiguration.def`

Too large to inline. Fields present:

`AdapterChangedDialog`, `AdapterDriverOutOfDateDialog`, `AddMarkerDialog`, `ApplyingChangesToSave`, `AudioNotLoadedConfirmationDialog`, `BatteryPowerWarningDialog`, `BestAdapterNotPickedDialog`, `BlueprintLoadingFailedDialog`, `BlueprintMaxPCUDialog`, `BlueprintNotFoundDialog`, `BlueprintScreenshotSavingFailureDialog`, `CharacterRespawnConfirmationDialog`, `CloseBlueprintDetailsDialog`, `ConfirmConsumeBlockSchematicPartiallyUnlockedDialog`, `ConfirmDeleteAsteroidDialog`, `ConfirmDeleteBlueprintDialog`, `ConfirmDeleteSaveDialog`, `ConfirmDiscardBlueprintDialog`, `ConfirmDiscardNewBackupDialog`, `ConfirmDiscardWorldSettingsDialog`, `ConfirmExitDialog`, `ConfirmLoadBackupWithoutSaving`, `ConfirmQuickLoadDialog`, `ConfirmSaveOverwriteDialog`, `ConfirmUnsubscribeBlueprintDialog`, `ConfirmWithoutSavingNewModsDialog`, `DatapadDialogDefinition`, `DebugMenuConfirmationDialog`, `DeleteMarkerDialog`, `DeleteMarkersDialog`, `DiscardModsChangesDialog`, `DisplaySettingsChangeFailedDialog`, `DisplaySettingsChangedDialog`, `ErrorLoadingModsDialog`, `GameServiceNotAvailableDialog`, `GpuRequirementsNotMet`, `Guid`, `InputCompositionDialog`, `LastSessionFileCorruptedDialog`, `LoadGameWithDebugMenuConfirmationDialog`, `LoadGameWithUpdatedMods`, `LoadingFailedCorruptedFilesDialog`, `LoadingFailedDialog`, `LoadingFileCorruptedDialog`, `LoadingNewerSaveCofirmationDialog`, `LoadingNewerSaveDialog`, `LoadingNewerSaveFailedDialog`, `LowMemoryWarningDialog`, `MinimumHardwareRequirementsWarningDialog`, `MissingSaveDialog`, `NonSSDDriveDetectedWarningDialog`, `NumericInputDialog`, `PendingChangesConfirmationDialog`, `PreparingForPlaceBlueprintDialog`, `PreparingWorldForPublishDialog`, `PresetPerformanceWarningDialog`, `RatingDialog`, `ReconnectConfirmDialog`, `ReconnectStatusDialog`, `RenameMarkerDialog`, `ResetGraphicsPresetDialog`, `SaveBeforeExitDialog`, `SaveBeforeLoadDialog`, `SaveBeforeQuitDialog`, `SaveFailureAlreadyInProgressDialog`, `SaveFailureDialog`, `SaveFailureDiskFullDialog`, `SaveFailureExternalSaveDialog`, `SaveFailureInaccessibleFilesDialog`, `SaveFailureInvalidCharactersDialog`, `SaveFailurePrefixedNameDialog`, `SaveSuccessfullyDialog`, `SavingDialog`, `ScalingPerformanceWarningDialog`, `SwapConfigurationHowToFixDialog`, `TextPanelEditDialog`, `ToolbarActionDialog`, `UGCDeleteConfirmationDialog`, `UGCDeletingDialog`, `UGCFailureDiskFullDialog`, `UGCPublishConfirmationDialog`, `UGCPublishFailureDialog`, `UGCPublishFailureEulaNotAcceptedDialog`, `UGCPublishFailureInvalidRequestDialog`, `UGCPublishFailureLimitExceededDialog`, `UGCPublishFailureNotFoundDialog`, `UGCPublishFailureServiceInactiveDialog`, `UGCPublishFailureWorldSavingFailedDialog`, `UGCPublishSuccessDialog`, `UGCRepublishConfirmationDialog`, `UGCUploadingDialog`, `UnspecifiedDriveWarningDialog`, `UnstableGpuDriverDialog`, `UrlWarningDialog`, `VersionMismatchDialog`

---

Read it with the MCP server rather than by hand:

```
describe_type('DialogsConfigurationObjectBuilder')
search_content('', type_contains='DialogsConfigurationObjectBuilder')
```
