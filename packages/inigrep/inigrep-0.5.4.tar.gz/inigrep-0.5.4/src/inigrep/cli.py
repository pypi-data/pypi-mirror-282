from __future__ import annotations
import sys
from typing import Any, Iterable
from dataclasses import dataclass, field
from enum import Enum, auto

from ._meta import VERSION
from .core import (
    KeypathError,
)
import inigrep
import inigrep.front


_USAGE: str = """
usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -c|--clone [file]...
    inigrep [-1] -e|--basic section.key [file]...
    inigrep [-1] -r|--raw section.key [file]...
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


@dataclass
class Args:
    args: list[str]

    def take1(self) -> str:
        if not self.args:
            raise UsageError('missing argument')
        return self.args.pop(0)

    def take2(self) -> tuple[str, str]:
        if len(self.args) < 2:
            raise UsageError('missing arguments')
        return self.args.pop(0), self.args.pop(0)

    def next(self) -> str:
        return self.args[0]

    def next_is(self, *cases) -> bool:
        return self.args[0] in cases

    def rest(self) -> list[str]:
        return self.args[:]


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
    action_args: dict[str, Any] = field(default_factory=dict)
    oneline: bool = False
    files: list[str] = field(default_factory=list)

    @classmethod
    def from_args(cls, args: list[str]) -> Options:
        o = cls()
        a = Args(args)
        while a.rest():
            if a.next_is('--help'):
                raise HelpNeeded()
            if a.next_is('--version'):
                raise VersionNeeded()
            elif a.next_is('-1'):
                o.oneline = True
                a.take1()
            elif a.next_is('-c', '--clone'):
                o.action = Action.CLONE
                o.action_args = {}
                a.take1()
            elif a.next_is('-s', '--clsct'):
                o.action = Action.CLONE_SECTION
                o.action_args = {'kpath': a.take2()[1] + '.'}
            elif a.next_is('-e', '--basic'):
                o.action = Action.VALUES
                o.action_args = {'kpath': a.take2()[1]}
            elif a.next_is('-r', '--raw'):
                o.action = Action.RAW_VALUES
                o.action_args = {'kpath': a.take2()[1]}
            elif a.next_is('-K', '--lskey'):
                o.action = Action.LIST_KEYS
                o.action_args = {'section': a.take2()[1]}
            elif a.next_is('-S', '--lssct'):
                o.action = Action.LIST_SECTIONS
                o.action_args = {}
                a.take1()
            elif a.next_is('-P', '--lspth'):
                o.action = Action.LIST_PATHS
                o.action_args = {}
                a.take1()
            elif a.next().startswith('-'):
                raise UsageError('unknown argument: %s' % a.next())
            else:
                break
        if o.action == Action.NONE:
            o.action = Action.VALUES
            o.action_args = {'kpath': a.take1()}
        files = a.rest()
        if not files:
            files = ['-']
        elif files == ['']:
            # FIXME: this is strange but turns out saturnin relies on it
            files = ['-']
        o.files = files
        return o


def run(options: Options):
    o = options
    if o.action == Action.VALUES:
        return inigrep.front.values(files=o.files, **o.action_args)
    if o.action == Action.RAW_VALUES:
        return inigrep.front.raw_values(files=o.files, **o.action_args)
    if o.action == Action.LIST_KEYS:
        return inigrep.front.list_keys(files=o.files, **o.action_args)
    if o.action == Action.LIST_SECTIONS:
        return inigrep.front.list_sections(files=o.files, **o.action_args)
    if o.action == Action.LIST_PATHS:
        return inigrep.front.list_paths(files=o.files, **o.action_args)
    if o.action == Action.CLONE:
        return inigrep.front.clone(files=o.files, **o.action_args)
    raise ValueError(f"invalid action: {o.action}")


def main() -> None:

    try:
        options = Options.from_args(sys.argv[1:])
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
