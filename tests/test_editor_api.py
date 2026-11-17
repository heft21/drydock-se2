"""The C# snippets sent to the editor: no editor is needed to check their shape.

A snippet that is missing a brace, or still carries a template placeholder, only
fails inside the editor, where the error is far from its cause. These tests catch
that on any machine.
"""

import re
import unittest

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import editor_api

# Words the server substitutes before sending a snippet (see server.py).
PLACEHOLDERS = {
    "GENERATORS": ["FILTER"],
    "CREATE_FROM_TEMPLATE": ["MENU_PATH", "WHICH_MENU"],
    "OPEN_ASSET": ["TARGET_NAME", "SET_OPEN"],
}


def snippets() -> dict[str, str]:
    return {name: value for name, value in vars(editor_api).items()
            if name.isupper() and not name.startswith("_") and isinstance(value, str)}


def strip_literals(code: str) -> str:
    """Remove comments and string/char literals so only structure is left."""
    code = re.sub(r"//[^\n]*", "", code)
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.S)
    code = re.sub(r'@"(?:[^"]|"")*"', '""', code)
    code = re.sub(r'"(?:\\.|[^"\\\n])*"', '""', code)
    return re.sub(r"'(?:\\.|[^'\\\n])'", "''", code)


def unbalanced(code: str) -> str | None:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in strip_literals(code):
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return f"unexpected {ch!r}"
    return f"unclosed {stack[-1]!r}" if stack else None


class Snippet(unittest.TestCase):
    def test_snippet_puts_the_prelude_before_the_body(self):
        out = editor_api.snippet("return J(1);")
        self.assertTrue(out.startswith(editor_api._PRELUDE))
        self.assertTrue(out.endswith("return J(1);"))
        self.assertIn("object Svc(string n)", out)

    def test_the_prelude_alone_is_balanced(self):
        self.assertIsNone(unbalanced(editor_api._PRELUDE))


class ViewModelPicker(unittest.TestCase):
    def test_vm_of_names_the_view_model_it_is_given(self):
        code = editor_api.vm_of("ProjectExplorerViewModel")
        self.assertIn('GetType().Name == "ProjectExplorerViewModel"', code)
        self.assertIn("ProjectExplorerViewModel is not among", code)

    def test_vm_of_leaves_no_doubled_braces_from_the_format_string(self):
        code = editor_api.vm_of("X")
        self.assertNotIn("{{", code)
        self.assertNotIn("}}", code)
        self.assertIsNone(unbalanced(code))

    def test_different_names_give_different_snippets(self):
        self.assertNotEqual(editor_api.vm_of("A"), editor_api.vm_of("B"))


class Constants(unittest.TestCase):
    def test_there_are_snippets_to_check(self):
        self.assertGreaterEqual(len(snippets()), 8)

    def test_every_snippet_has_balanced_brackets(self):
        for name, code in snippets().items():
            with self.subTest(snippet=name):
                self.assertIsNone(unbalanced(code))

    def test_every_snippet_starts_with_the_prelude(self):
        for name, code in snippets().items():
            with self.subTest(snippet=name):
                self.assertTrue(code.startswith(editor_api._PRELUDE))

    def test_every_snippet_answers_with_json(self):
        for name, code in snippets().items():
            with self.subTest(snippet=name):
                self.assertIn("J(", code.split(editor_api._PRELUDE, 1)[1])

    def test_only_the_snippets_that_take_parameters_carry_placeholders(self):
        every = {w for words in PLACEHOLDERS.values() for w in words}
        for name, code in snippets().items():
            body = code.split(editor_api._PRELUDE, 1)[1]
            for word in every:
                with self.subTest(snippet=name, placeholder=word):
                    if word in PLACEHOLDERS.get(name, []):
                        self.assertIn(word, body)
                    else:
                        self.assertNotRegex(body, rf'"{word}"|\b{word}\b')

    def test_a_parameterised_snippet_is_complete_once_filled_in(self):
        for name, words in PLACEHOLDERS.items():
            code = getattr(editor_api, name)
            for word in words:
                code = code.replace(word, "x")
            with self.subTest(snippet=name):
                self.assertIsNone(unbalanced(code))
                for word in words:
                    self.assertNotIn(word, code)


if __name__ == "__main__":
    unittest.main()
