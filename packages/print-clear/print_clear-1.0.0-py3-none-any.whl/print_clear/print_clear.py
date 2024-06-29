from termcolor import colored
from pathlib import Path
import argparse
import sys


from ._version import __version__


def print_clear(string: str) -> None:
    print("".join(colored(i, "red") if i.isdigit() else i for i in string))


def main(prog: str, *args: str) -> None:
    base: str = Path(prog).name
    parser = argparse.ArgumentParser(prog=base)
    parser.add_argument("string", help="The string to print clearly")
    parser.add_argument("--version", action="version", version=f"{base} {__version__}")
    print_clear(**vars(parser.parse_args(args)))


def cli() -> None:
    main(*sys.argv)
