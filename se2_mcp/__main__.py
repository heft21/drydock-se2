"""Entry point: `python -m se2_mcp` runs the server on stdio.

`--selftest` runs the same checks the `self_test` tool exposes and prints them,
which is the fastest way to find out whether an install is wired up correctly
without attaching an MCP client to it.
"""

import sys


def main() -> int:
    args = [a.lower().lstrip("-") for a in sys.argv[1:]]
    if "selftest" in args or "self-test" in args or "test" in args:
        from .selftest import main as selftest_main
        return selftest_main()
    if "version" in args:
        from . import __author__, __product__, __url__, __version__
        print(f"{__product__} {__version__} by {__author__} - {__url__}")
        return 0
    if "help" in args or "h" in args:
        from . import __author__, __product__, __url__
        print(f"{__product__} by {__author__} - {__url__}")
        print(__doc__)
        print("usage: python -m se2_mcp [--selftest | --version]")
        return 0
    from .server import main as server_main
    server_main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
