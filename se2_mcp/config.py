"""Path discovery and shared constants for the SE2 Mod SDK MCP server.

Nothing here should need configuring. The Mod SDK is found by asking Steam where
its libraries are, and a user's own mod projects are found through Mod HUB's own
settings file — so the server starts correctly on a machine it has never seen,
which is the difference between "works" and "works for the person who wrote it".
Every step is still overridable by environment variable when detection is wrong.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

# A GUID as it appears inside definition JSON. References are sometimes written
# with a "{G}" prefix (e.g. "Model": "{G}44aa4447-...") and sometimes bare.
GUID_RE = re.compile(
    r"^(?:\{G\})?([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$"
)

DEF_SUFFIXES = (".def", ".partialdef")

# The folder Steam creates for the SDK, under <library>/steamapps/common.
SDK_FOLDER_NAME = "Space Engineers 2 - Mod SDK"

# Where the game itself installs, used to give the editor its executable path.
GAME_FOLDER_NAME = "SpaceEngineers2"

# Last-resort location, only reached when Steam cannot be found at all.
DEFAULT_SDK = Path(r"C:\Program Files (x86)\Steam\steamapps\common") / SDK_FOLDER_NAME

# Environment variables, in the order they are consulted. SE2_SDK_DIR is the
# name the earlier TypeScript server used; accepting both means an existing
# .env keeps working.
SDK_ENV_VARS = ("SE2_MODSDK", "SE2_SDK_DIR")
MOD_ROOTS_ENV_VARS = ("SE2_MCP_MOD_ROOTS", "SE2_MODS_DIR")


def normalize_guid(value: str) -> str | None:
    """Return the bare lowercase GUID, or None if `value` is not a GUID."""
    if not isinstance(value, str) or not (36 <= len(value) <= 39):
        return None
    m = GUID_RE.match(value)
    return m.group(1).lower() if m else None


# ---------------------------------------------------------------------------
# Steam discovery
# ---------------------------------------------------------------------------

def _steam_root() -> Path | None:
    """Steam's install directory, from the registry it writes on install."""
    if sys.platform != "win32":
        return None
    try:
        import winreg
    except ImportError:
        return None
    for hive, key, name in (
        (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam", "SteamPath"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam", "InstallPath"),
    ):
        try:
            with winreg.OpenKey(hive, key) as handle:
                value, _ = winreg.QueryValueEx(handle, name)
        except OSError:
            continue
        path = Path(str(value))
        if path.is_dir():
            return path
    return None


# libraryfolders.vdf is Valve's own format, but only one field is needed and it
# is always written as a quoted key/value pair on its own line.
_VDF_PATH_RE = re.compile(r'"path"\s*"([^"]+)"')


def _steam_libraries() -> list[Path]:
    """Every Steam library folder on this machine, Steam's own root included."""
    root = _steam_root()
    libraries: list[Path] = []
    if root:
        libraries.append(root)
        vdf = root / "steamapps" / "libraryfolders.vdf"
        try:
            text = vdf.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        for raw in _VDF_PATH_RE.findall(text):
            candidate = Path(raw.replace("\\\\", "\\"))
            if candidate.is_dir() and candidate not in libraries:
                libraries.append(candidate)

    # A library on another drive that Steam has not registered — or a machine
    # where the registry read failed — is still worth a look. Checking a fixed
    # set of well-known layouts costs a few dozen stat calls.
    if sys.platform == "win32":
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZS":
            for tail in ("SteamLibrary", "Steam", r"Program Files (x86)\Steam",
                         r"Games\SteamLibrary"):
                candidate = Path(f"{letter}:\\") / tail
                if candidate.is_dir() and candidate not in libraries:
                    libraries.append(candidate)
    return libraries


def _looks_like_sdk(path: Path) -> bool:
    return (path / "GameData").is_dir() and (path / "Editor").is_dir()


@lru_cache(maxsize=1)
def find_sdk() -> Path:
    """Locate the Mod SDK: environment first, then Steam, then the default."""
    for var in SDK_ENV_VARS:
        raw = os.environ.get(var, "").strip().strip('"')
        if raw:
            # An explicit setting is honoured even when it looks wrong, so the
            # problem surfaces as a clear "not found here" rather than the
            # server quietly using a different install.
            return Path(raw)

    for library in _steam_libraries():
        candidate = library / "steamapps" / "common" / SDK_FOLDER_NAME
        if _looks_like_sdk(candidate):
            return candidate
    return DEFAULT_SDK


@dataclass(frozen=True)
class Paths:
    sdk: Path

    @property
    def editor(self) -> Path:
        return self.sdk / "Editor"

    @property
    def game_data(self) -> Path:
        return self.sdk / "GameData"

    @property
    def vanilla(self) -> Path:
        return self.game_data / "Vanilla"

    @property
    def engine(self) -> Path:
        return self.game_data / "Engine"

    @property
    def builder_exe(self) -> Path:
        return self.editor / "VRage.ContentPipeline.Builder.exe"

    @property
    def editor_exe(self) -> Path:
        return self.editor / "VRage.Editor.exe"

    @property
    def game_dir(self) -> Path:
        """The game install, which sits beside the SDK in the same library."""
        return self.sdk.parent / GAME_FOLDER_NAME

    @property
    def cache_dir(self) -> Path:
        d = Path(
            os.environ.get("SE2_MCP_CACHE")
            or (Path(os.environ.get("LOCALAPPDATA", Path.home())) / "se2-mcp")
        )
        d.mkdir(parents=True, exist_ok=True)
        return d

    @property
    def db_path(self) -> Path:
        return self.cache_dir / "se2_index.sqlite3"

    def doc_xml_files(self) -> list[Path]:
        """XML documentation files shipped next to the SDK assemblies."""
        return sorted(self.editor.glob("*.xml"))

    def check(self) -> list[str]:
        problems = []
        if not self.sdk.is_dir():
            problems.append(
                f"SDK root not found: {self.sdk}. Set the SE2_MODSDK environment "
                f"variable to the '{SDK_FOLDER_NAME}' folder."
            )
        if not self.game_data.is_dir():
            problems.append(f"GameData not found: {self.game_data}")
        if not self.builder_exe.is_file():
            problems.append(f"ContentPipeline builder not found: {self.builder_exe}")
        return problems


def load_paths() -> Paths:
    return Paths(sdk=find_sdk())


PATHS = load_paths()


# ---------------------------------------------------------------------------
# The user's own mod projects
# ---------------------------------------------------------------------------

_MODS_DIR_RE = re.compile(r'"ModsDirectory"\s*:\s*"((?:[^"\\]|\\.)*)"')


def modhub_mods_dir() -> Path | None:
    """Mod HUB's configured mods folder, read from its settings file.

    Scraped rather than JSON-parsed so that a settings file the HUB has written
    in some new shape still yields the one field that matters here.
    """
    roaming = Path(os.environ.get("APPDATA", Path.home() / "AppData/Roaming"))
    settings = roaming / "VRAGE3.ModHUB" / "Settings" / "ApplicationSettings.json"
    try:
        text = settings.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return None
    m = _MODS_DIR_RE.search(text)
    if not m:
        return None
    path = Path(m.group(1).encode().decode("unicode_escape"))
    return path if path.is_dir() else None


def default_mod_roots() -> list[Path]:
    """Where mod projects live when nothing was configured.

    Indexing a modder's own projects alongside vanilla is what makes answers say
    where a definition came from, so it is worth doing without being asked.
    """
    candidates = [
        modhub_mods_dir(),
        Path.home() / "Documents" / "SpaceEngineers2" / "Mods",
    ]
    return [p for p in candidates if p is not None and p.is_dir()]


def _expand_root(p: Path) -> list[Path]:
    """A project folder stays as-is; a folder of projects expands to them."""
    if any(p.glob("*.vrgproj")):
        return [p]
    children = sorted(c for c in p.iterdir() if c.is_dir() and any(c.glob("*.vrgproj")))
    return children or [p]


def extra_roots() -> list[Path]:
    """Additional project roots to index.

    Set SE2_MCP_MOD_ROOTS (an os.pathsep-separated list) to control this. With
    nothing set, Mod HUB's own mods directory is used, so the common case needs
    no configuration at all. A path that is not itself a project but contains
    several expands to the projects inside it.
    """
    raw = ""
    for var in MOD_ROOTS_ENV_VARS:
        raw = os.environ.get(var, "").strip()
        if raw:
            break

    if not raw:
        listed = default_mod_roots()
    else:
        listed = []
        for part in raw.split(os.pathsep):
            part = part.strip().strip('"')
            if part and Path(part).is_dir():
                listed.append(Path(part))

    roots: list[Path] = []
    for p in listed:
        try:
            for expanded in _expand_root(p):
                if expanded not in roots:
                    roots.append(expanded)
        except OSError:
            continue
    return roots
