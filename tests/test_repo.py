"""The repository itself: it has to check out on Windows from an ordinary folder."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Windows refuses paths over 260 characters unless long paths are switched on,
# and git then fails the whole checkout. A clone in a folder such as
# C:\Users\<name>\OneDrive\Documents\GitHub\drydock-se2\ already spends ~70 of
# them, so no path inside the repository may take more than 140 of the rest.
MAX_RELATIVE = 140
SKIP = {".git", "__pycache__", ".backups", "cache", "bin", "obj", "runs"}


class PathLength(unittest.TestCase):
    def test_no_path_is_too_long_for_a_windows_checkout(self):
        long = []
        for path in ROOT.rglob("*"):
            rel = path.relative_to(ROOT)
            if SKIP.intersection(rel.parts) or not path.is_file():
                continue
            if len(rel.as_posix()) > MAX_RELATIVE:
                long.append(f"{len(rel.as_posix())}  {rel.as_posix()}")
        self.assertEqual(long, [], "paths too long for a Windows checkout")


if __name__ == "__main__":
    unittest.main()
