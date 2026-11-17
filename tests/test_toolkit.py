"""The properties that make the server usable by a small model."""

import inspect
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from se2_mcp import server, toolkit  # noqa: E402


def declared():
    return {n: getattr(server, n) for n in sorted(toolkit._declared)
            if callable(getattr(server, n, None))}


class Profiles(unittest.TestCase):
    def test_every_profile_names_only_real_tools(self):
        real = set(toolkit._declared)
        for name, tools in toolkit.PROFILES.items():
            if tools is not None:
                self.assertEqual(tools - real, set(), name)

    def test_mini_is_inside_core(self):
        self.assertLessEqual(toolkit.MINI_TOOLS, toolkit.CORE_TOOLS)

    def test_the_session_bookends_are_always_available(self):
        for name in ("work_on", "finish_and_publish"):
            self.assertIn(name, toolkit.CORE_TOOLS)

    def test_a_small_model_can_read_write_and_check_in_mini(self):
        for name in ("search_content", "read_definition", "write_definition", "audit_project"):
            self.assertIn(name, toolkit.MINI_TOOLS)


class Tools(unittest.TestCase):
    def test_every_tool_has_an_example_in_its_description(self):
        missing = []
        # descriptions live on the registered tool, so read them from the source text
        text = Path(server.__file__).read_text(encoding="utf-8")
        for name, fn in declared().items():
            if not inspect.signature(fn).parameters:
                continue                      # nothing to show how to call
            marker = f"def {name}("
            start = text.index(marker)
            head = text.rfind("@tool(", 0, start)
            block = text[head:start]
            if f"{name}(" not in block.split(f"def {name}(")[0]:
                missing.append(name)
        self.assertEqual(missing, [], "tools without a call written out in the description")

    def test_every_optional_argument_accepts_null(self):
        bad = []
        for name, fn in declared().items():
            for pname, p in inspect.signature(fn).parameters.items():
                if p.default is not inspect._empty and p.default is not None:
                    text = str(p.annotation)
                    if "None" not in text:
                        bad.append(f"{name}.{pname}")
        self.assertEqual(bad, [], "optional arguments must be declared nullable")

    def test_the_write_tools_never_raise(self):
        for fn, args in ((server.write_definition, ("relative.def", "A", {})),
                         (server.refresh_meta, ("relative.def",))):
            out = fn(*args)
            self.assertIn("error", out)


if __name__ == "__main__":
    unittest.main()
