using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using Keen.VRage.Core.Game.Systems;
using Keen.VRage.DCS.Builders;
using Keen.VRage.DCS.Components;
using Keen.VRage.Library.Reflection;
using Keen.VRage.Library.Serialization;
using Keen.VRage.Library.Utils;
using Keen.VRage.Plugin.Editor;
using Keen.VRage.Plugin.Editor.Preview;
using SE2McpBridge;

// Three attributes, all normally emitted by Keen's VRage.Library.Generator,
// have to be written by hand for a plugin built outside their build system.
// Each one is a separate gate, and missing any of them means the assembly
// loads but the plugin is silently never instantiated:
//
//  1. IndexMetadata      - MetadataHelper.FilterAssembliesWithMetadata drops
//                          every assembly without it before indexing starts.
//  2. MetadataDependencies - names the assemblies pulled into the same metadata
//                          context; without it this assembly is "unknown".
//  3. ModuleIndexedAttributes - the actual index entry AttributeIndexer reads
//                          to answer "which types carry [ProjectPlugin]".
[assembly: IndexMetadata]
[assembly: MetadataDependencies(new[] { "VRage.Plugin.Editor", "VRage.Library" })]
[module: ModuleIndexedAttributes(
    typeof(ProjectPluginAttribute),
    new[] { typeof(BridgePlugin) },
    new string[0])]

namespace SE2McpBridge
{
    /// <summary>
    /// Editor plugin that opens a local HTTP bridge so an MCP server can read
    /// editor state, watch what happens, and run code inside the process.
    ///
    /// Everything interesting is deliberately reached through the /eval endpoint
    /// instead of typed wrappers: the editor's own services (ISelectionService,
    /// IProjectsService, ...) are declared `internal`, so reflection from inside
    /// the process is the only way to touch them.
    /// </summary>
    [ProjectPlugin]
    public class BridgePlugin : IProjectPlugin, IDisposable
    {
        private HttpBridge _bridge;

        public BridgePlugin()
        {
            // The constructor runs during plugin discovery, before a project is
            // loaded. Starting here means the bridge answers even if project
            // loading later fails, which is exactly when it is most useful.
            try
            {
                _bridge = new HttpBridge();
                _bridge.Start();
                EventLog.Add("plugin", "SE2McpBridge constructed; listening on " + _bridge.Prefix);
            }
            catch (Exception ex)
            {
                EventLog.Add("error", "Bridge failed to start: " + ex);
            }
        }

        /// <summary>Called once the project tree finished loading.</summary>
        public void OnProjectLoaded()
        {
            EventLog.Add("project", "OnProjectLoaded");
            EditorApi.OnProjectLoaded();
        }

        // --- Required interface members. The bridge is an observer; it must not
        // --- change how the editor builds sessions or previews.

        public void ObjectBuilderLoadingContextConfigurator(
            ref ServiceLocatorContext.Builder contextBuilder, Entity engineEntity)
        {
        }

        public bool TryConfigureSessionAndScene(
            Entity engine, SessionBuilder sessionBuilder,
            [NotNullWhen(false)] out SessionConfigurationErrors configurationErrors)
        {
            configurationErrors = null;
            return true;
        }

        public void FilterJobs(List<SceneBuilder.JobInfo> sceneJobs)
        {
        }

        public void ConfiguratorProcessorConfigurator(ref EntityBuilder configurator)
        {
        }

        /// <summary>This plugin provides no previews; it defers to the others.</summary>
        public bool TryGetPreviewForAsset(
            AssetDescriptor asset,
            [NotNullWhen(true)] out PreviewEntityDataBase previewEntityData,
            out PreviewErrors previewErrors,
            IAccessible previewSettings = null)
        {
            previewEntityData = null;
            previewErrors = null;
            return false;
        }

        public void Dispose()
        {
            EventLog.Add("plugin", "SE2McpBridge disposing");
            _bridge?.Dispose();
            _bridge = null;
        }
    }
}
