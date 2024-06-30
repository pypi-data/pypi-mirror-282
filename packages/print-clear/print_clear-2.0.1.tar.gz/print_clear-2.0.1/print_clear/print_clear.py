from termcolor import colored
from pathlib import Path
import argparse
import sys


from ._version import __version__


def mk_legend() -> str:
    legend = (
        "Digit:     " + colored("RED", "red"),
        "Special:   " + colored("BLUE", "blue"),
        "Uppercase: " + colored("GREEN", "green"),
        "Lowercase: " + colored("DEFAULT", None),
    )
    return "Legend:\n  " + "\n  ".join(legend)


def color_char(c: str) -> str:
    if c.islower():
        return c
    if c.isupper():
        return colored(c, "green")
    if c.isdigit():
        return colored(c, "red")
    return colored(c, "blue")


def _main(string: str | None, legend: bool) -> None:
    pnt = []
    if string is not None:
        pnt.append("".join(color_char(i) for i in string))
    if legend:
        pnt.append(mk_legend())
    if not pnt:
        print("Error: No arguments passed.")
        sys.exit(1)
    print("\n\n".join(pnt))


def main(prog: str, *args: str) -> None:
    base: str = Path(prog).name
    parser = argparse.ArgumentParser(prog=base)
    parser.add_argument("string", nargs="?", default=None, help="The string to print clearly.")
    parser.add_argument("--legend", action="store_true", help="Print the color code legend at the end.")
    parser.add_argument("--version", action="version", version=f"{base} {__version__}")
    _main(**vars(parser.parse_args(args)))


def cli() -> None:
    main(*sys.argv)
