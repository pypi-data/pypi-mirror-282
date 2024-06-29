from __future__ import annotations
import sys
from dataclasses import dataclass, field
from enum import Enum, auto

from ._meta import VERSION
from .front import UnitIni
from .core import KeypathError


_USAGE: str = """
usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -c|--clone [file]...
    inigrep [-1] -e|--basic section.key [file]...
    inigrep [-1] -r|--raw section.key [file]...
    inigrep [-1] -s|--clsct section [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help
    inigrep --version
"""

__doc__ = """
Query INI file(s) for data

Usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -c|--clone [file]...
    inigrep [-1] -e|--basic section.key [file]...
    inigrep [-1] -r|--raw section.key [file]...
    inigrep [-1] -s|--clsct section [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help
    inigrep --version

First form implies the basic engine.

Option *-r* switches to raw mode, in which comments,
empty lines and whitespace are all preserved in applicable
contexts.

Key *keypath* consists of section name and key name delimited
by dot. Note that keypath may contain dots but key may not.

If *file* is not given or is a single dash, standard input
is read. Note that standard input is not duplicated in case
of multiple dashes.

If suitable key is found at multiple lines, all values
are printed, which allows for creating multi-line values.
Providing *-1* argument, however, always prints only one
line.

Options -K, -S and -P can be used for inspecting file structure;
-K needs an argument of section name and will list all keys from
that section. -S will list all sections and -P will list all
existing keypaths.


#### Examples ####

Having INI file such as

    [foo]
    bar=baz
    quux=qux
    quux=qux2
    quux=qux3

* `inigrep foo.bar ./file.ini` gives "bar".
* `inigrep foo.quux ./file.ini` gives three lines "qux", "qux2"
    and "qux3".
* `inigrep -P ./file.ini` gives two lines "foo.bar" and "foo.quux".
* `inigrep -K foo ./file.ini` gives two lines "bar" and "quux".
* `inigrep -S ./file.ini` gives "foo".
"""


class UsageError(RuntimeError):
    pass


class HelpNeeded(RuntimeError):
    pass


class VersionNeeded(RuntimeError):
    pass


class Action(Enum):
    NONE = auto()
    CLONE = auto()
    CLONE_SECTION = auto()
    VALUES = auto()
    RAW_VALUES = auto()
    LIST_SECTIONS = auto()
    LIST_KEYS = auto()
    LIST_PATHS = auto()


@dataclass
class Options:
    action: Action = Action.NONE
    query: str | None = None
    oneline: bool = False
    files: list[str] = field(default_factory=list)


@dataclass
class Args:
    args: list[str]

    def _check_args(self,
                    num: int = 1,
                    name: str = '',
                    *ctx_names: str,
                    ) -> None:
        if len(self.args) >= num:
            # we have enough
            return
        ctx_hint = '' if not ctx_names else f" after `{' '.join(ctx_names)}`"
        raise UsageError(
            f"no {name}{ctx_hint}?"
            if name else
            f"missing one or more arguments{ctx_hint}"
        )

    def len(self) -> int:
        return len(self.args)

    def take1(self, name: str = '') -> str:
        self._check_args(1, name)
        return self.args.pop(0)

    def next(self) -> str:
        return self.args[0]

    def next_is(self, *cases) -> bool:
        return self.args[0] in cases

    def next_was(self, *cases) -> bool:
        if not self.next_is(*cases):
            return False
        self.args.pop(0)
        return True

    def rest(self) -> list[str]:
        return self.args[:]


def parse_args(args: list[str]) -> Options:
    o = Options()
    a = Args(args)
    while a.len():
        if a.next_was('--help'):
            raise HelpNeeded()
        if a.next_was('--version'):
            raise VersionNeeded()
        elif a.next_was('-1'):
            o.oneline = True
        elif a.next_was('-c', '--clone'):
            o.action = Action.CLONE
        elif a.next_was('-s', '--clsct'):
            o.action = Action.CLONE_SECTION
            o.query = a.take1('section') + '.'
        elif a.next_was('-e', '--basic'):
            o.action = Action.VALUES
            o.query = a.take1('section.key')
        elif a.next_was('-r', '--raw'):
            o.action = Action.RAW_VALUES
            o.query = a.take1('section.key')
        elif a.next_was('-K', '--lskey'):
            o.action = Action.LIST_KEYS
            o.query = a.take1('section')
        elif a.next_was('-S', '--lssct'):
            o.action = Action.LIST_SECTIONS
        elif a.next_was('-P', '--lspth'):
            o.action = Action.LIST_PATHS
        elif a.next().startswith('-'):
            raise UsageError('unknown argument: %s' % a.next())
        else:
            break
    if o.action == Action.NONE:
        o.action = Action.VALUES
        o.query = a.take1('section.key')
    files = a.rest()
    if not files:
        files = ['-']
    elif files == ['']:
        # FIXME: this is strange but turns out saturnin relies on it
        files = ['-']
    o.files = files
    return o


def run(options: Options):
    ini = UnitIni.from_files(options.files)
    if options.action == Action.VALUES:
        return ini.values(options.query)
    if options.action == Action.RAW_VALUES:
        return ini.raw_values(options.query)
    if options.action == Action.LIST_KEYS:
        return ini.list_keys(options.query)
    if options.action == Action.LIST_SECTIONS:
        return ini.list_sections()
    if options.action == Action.LIST_PATHS:
        return ini.list_paths()
    if options.action == Action.CLONE_SECTION:
        return ini.clone_section(options.query)
    if options.action == Action.CLONE:
        return ini.clone()
    raise ValueError(f"invalid action: {options.action}")


def main() -> None:

    try:
        options = parse_args(sys.argv[1:])
    except UsageError as e:
        sys.stderr.write('%s\n' % _USAGE[1:])
        sys.stderr.write('error: %s\n' % e)
        sys.exit(2)
    except HelpNeeded as e:
        sys.stderr.write('%s\n' % __doc__)
        sys.stderr.write('%s\n' % e)
        sys.exit(0)
    except VersionNeeded:
        sys.stderr.write('%s\n' % VERSION)
        sys.exit(0)

    gen = run(options)

    try:
        for line in gen:
            print(line)
            if options.oneline:
                break
    except KeypathError as e:
        sys.stderr.write('%s\n' % e)
        sys.exit(2)
