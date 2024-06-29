#!/usr/bin/python3

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable
import functools
import os
import sys

from .core import (
    ClonedLineT,
    FileReader,
    KeyT,
    LineT,
    NIL,
    Parser,
    RawValueT,
    Unit,
    ValueT,
    _r_clone,
    _r_list_keys,
    _r_list_paths,
    _r_list_sections,
    _r_raw_values,
    _r_values,
    _valid_section,
    _valid_keypath,
    SingleFileReader,
    KeypathT,
    SectionT,
)

__doc__ = """
inigrep
=======

grep for (some) INIs

inigrep is designed to read a particular simplistic dialect of
INI configuration files. In a sense, it can be considered as
a "grep for INIs", in that rather than parsing the file into
a typed memory structure for later access, it passes file each
time a query is done, and spits out relevant parts; treating
everything as text. Hence, it's not intended as replacement
for a full-blown configuration system but rather a quick & dirty
"swiss axe" for quick & dirty scripts.

That's not to say that you cannot do things nicely; but don't
count on speed -- well since you're using bash you obviously
don't -- and compliance -- simple things are simple, but there
are a bit unusual pitfalls.


The format by examples
----------------------

The most basic example understood by inigrep is identical
to most INI formats:

    # Let's call this simple.ini

    [foo]
        bar = baz
        qux = quux

    [corge]
        grault = graply

Structure here is obvious: two sections named `foo` and `corge`,
the first one has two key/value pairs and the other has one pair.

Getting values from this file is trivial:

    inigrep foo.bar simple.ini
    inigrep foo.qux simple.ini
    inigrep corge.grault simple.ini

would list `baz`, `quux` and `graply`.

This is where 80% of use cases are covered.


Multi-line
----------

Multi-line values are rather unusual but very simple:

    [lipsum]

        latin = Lorem ipsum dolor sit amet, consectetur adipiscing
        latin = elit, sed do eiusmod tempor incididunt ut labore et
        latin = dolore magna aliqua. Ut enim ad minim veniam, quis
        latin = ...

        english = [32] But I must explain to you how all this mistaken
        english = idea of denouncing of a pleasure and praising pain
        english = was born and I will give you a complete account of
        english = ...

This file can be read as:

    inigrep lipsum.latin lipsum.ini
    inigrep lipsum.english lipsum.ini


Exploration
-----------

Other than basic value retrieval, inigrep allows you to look around
first. For example, to list all keypaths available in a file:

    inigrep -P simple.ini

In case of simple.ini, this would print:

    foo.bar
    foo.qux
    corge.grault

Similarly:

    inigrep -S simple.ini

would list just the section names:

    foo
    corge

and

    inigrep -K foo simple.ini

would list all keys from section 'foo'

    bar
    qux
"""


def clone(files: list[str], kpath: str = '.') -> Iterable[str]:
    """
    Return replica of INI file that is concatenation of *files*.
    """
    for value in _r_clone(reader=FileReader(files), kpath=kpath):
        yield str(value)


def values(files: list[str], kpath: str) -> Iterable[str]:
    """
    Return list of values from files *files* at key path *kpath*.

    *kpath* must be key path, i.e. string containing section and
    key names delimited by period.

    *files* must list of file paths.
    """
    for value in _r_values(reader=FileReader(files), kpath=kpath):
        yield str(value)


def raw_values(files: list[str], kpath: str) -> Iterable[str]:
    """
    Return list of raw values found in *files* at key path *kpath*.

    Same as values(), but uses raw inigrep engine, which keeps in-line
    comments and value leading/trailing whitespace.
    """
    for value in _r_raw_values(reader=FileReader(files), kpath=kpath):
        yield str(value)


def list_sections(files: list[str]) -> Iterable[str]:
    """
    Return list of sections found in *files*.
    """
    for value in _r_list_sections(reader=FileReader(files)):
        yield str(value)


def list_keys(files: list[str], section: str) -> Iterable[str]:
    """
    Return list of keys found in *files* under *section*.
    """
    return _r_list_keys(reader=FileReader(files), section=section)


def list_paths(files: list[str], keypath: str = '.') -> Iterable[str]:
    """
    Return list of all key paths found by *in files*.
    """
    return _r_list_paths(reader=FileReader(files), keypath=keypath)


def load(files: list[str]) -> Ini:
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_files().
    """
    return Ini.from_files(files)


def load_existent(files: list[str]) -> Ini:
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_existent_files().
    """
    return Ini.from_existent_files(files)


class IniDataError(ValueError):
    pass


class MissingSectionError(IniDataError):
    pass


class RepeatSectionError(IniDataError):
    pass


class MissingKeyError(IniDataError):
    pass


class RepeatKeyError(IniDataError):
    pass


@dataclass
class DictWrapper:
    data: dict[str, list[str]]

    def get01(self, key: str) -> str | None:
        found = self.data.get(key, [])
        if not found:
            return None
        if len(found) > 1:
            raise RepeatKeyError(key)
        return found[0]

    def get0N(self, key: str) -> list[str]:
        return self.data.get(key, [])

    def get11(self, key: str) -> str:
        found = self.data.get(key, [])
        if not found:
            raise MissingKeyError(key)
        if len(found) > 1:
            raise RepeatKeyError(key)
        return found[0]

    def get1N(self, key: str) -> list[str]:
        found = self.data.get(key, [])
        if not found:
            raise MissingKeyError(key)
        return found

    def have(self, key: str) -> bool:
        found = self.data.get(key, [])
        return bool(found)

    def sget01(self, prefix: str) -> str | None:
        found = self.sget0N(prefix)
        if not found:
            return None
        if len(found) > 1:
            raise RepeatSectionError(prefix)
        return found[0]

    def sget0N(self, prefix: str | None) -> list[str]:
        if not prefix:
            return list(self.data.keys())
        real_prefix = prefix if prefix.endswith('.') else f'{prefix}.'
        found = []
        for k in self.data.keys():
            if not k.startswith(real_prefix):
                continue
            sct = k.removeprefix(real_prefix).split('.')[0]
            if sct in found:
                continue
            found.append(sct)
        return found

    def sget11(self, prefix: str) -> str:
        found = self.sget0N(prefix)
        if not found:
            raise MissingSectionError(prefix)
        if len(found) > 1:
            raise RepeatSectionError(prefix)
        return found[0]

    def sget1N(self, prefix: str) -> list[str]:
        found = self.sget0N(prefix)
        if not found:
            raise MissingSectionError(prefix)
        return found


@dataclass
class UnitIni:
    units: list[Unit]

    @classmethod
    def from_lines(cls, lines: Iterable[str]):
        parser = Parser()
        units = [unit for unit in parser.parse(map(LineT, lines))]
        return cls(units=units)

    @classmethod
    def from_stdin(cls):
        def collect_lines() -> Iterable[str]:
            for line in sys.stdin.readlines():
                yield line[:-1]
        return cls.from_lines(collect_lines())

    @classmethod
    def from_files(cls,
                   paths: list[str],
                   ignore_missing: bool = False,
                   ):
        def collect_lines() -> Iterable[str]:
            for path in paths:
                if path == '-':
                    for line in sys.stdin.readlines():
                        yield line[:-1]
                    continue
                if ignore_missing and not os.path.exists(path):
                    continue
                with open(path) as fp:
                    for line in fp.readlines():
                        yield line[:-1]
        return cls.from_lines(collect_lines())

    def clone(self) -> Iterable[ClonedLineT]:
        """
        Return lines of INI file with the same data as in this object
        """
        for unit in self.units:
            for cloned_line in unit.cloned_lines:
                yield cloned_line

    def data(self) -> dict[KeypathT, list[ValueT]]:
        """
        Return dictionary containing all INI data

        A flat dictionary is returned, mapping all valid keypaths to lists
        of lines.
        """
        data: dict[KeypathT, list[ValueT]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.values(kpath))
        return data

    def list_keys(self, section: str) -> Iterable[KeyT]:
        """
        Return list of keys under *section*.
        """
        want_section = _valid_section(section)
        seen = set()
        for unit in self.units:
            if not unit.ctx_section == want_section:
                continue
            if isinstance(unit.key, NIL):
                continue
            if unit.key in seen:
                continue
            seen.add(unit.key)
            yield unit.key

    def list_paths(self) -> Iterable[KeypathT]:
        """
        Return list of all paths
        """
        seen = set()
        for unit in self.units:
            if isinstance(unit.keypath, NIL):
                continue
            if unit.keypath in seen:
                continue
            seen.add(unit.keypath)
            yield unit.keypath

    def list_sections(self) -> Iterable[SectionT]:
        """
        Return list of keys under *section*.
        """
        seen = set()
        for unit in self.units:
            if isinstance(unit.section, NIL):
                continue
            if unit.section in seen:
                continue
            seen.add(unit.section)
            yield unit.section

    def raw_data(self) -> dict[KeypathT, list[RawValueT]]:
        """
        Return dictionary containing all raw INI data

        Same as .data(), but keeps in-line comments and leading/trailing
        whitespace around values.
        """
        data: dict[KeypathT, list[RawValueT]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.raw_values(kpath))
        return data

    def raw_values(self, kpath: str) -> Iterable[RawValueT]:
        """
        Return list of raw values at key path *kpath*.

        Same as .values(), but keeps in-line comments and leading/trailing
        whitespace around values.
        """
        want_section, want_key = _valid_keypath(kpath)
        for unit in self.units:
            if not unit.ctx_section == want_section:
                continue
            if not unit.key == want_key:
                continue
            if isinstance(unit.raw_value, NIL):
                continue
            yield unit.raw_value

    def raw_wrapper(self) -> DictWrapper:
        """
        Like .raw_data() but return DictWrapper with convenience access methods
        """
        return DictWrapper(data={
            str(key): [str(v) for v in values]
            for key, values in self.raw_data().items()
        })

    def wrapper(self) -> DictWrapper:
        """
        Like .data() but return DictWrapper with convenience access methods
        """
        return DictWrapper(data={
            str(key): [str(v) for v in values]
            for key, values in self.data().items()
        })

    def values(self, kpath: str) -> Iterable[ValueT]:
        """
        Return list of values at key path *kpath*.

        *kpath* must be key path, i.e. string containing section and
        key names delimited by period.
        """
        want_section, want_key = _valid_keypath(kpath)
        for unit in self.units:
            if not unit.ctx_section == want_section:
                continue
            if not unit.key == want_key:
                continue
            if isinstance(unit.value, NIL):
                continue
            yield unit.value


@dataclass
class SimpleIni:
    """
    Set of cached INI files
    """
    _unit_ini: UnitIni

    @classmethod
    def from_files(cls, files: list[str], ignore_missing: bool = False) -> SimpleIni:
        """
        Initialize SimpleIni object containing lines of all *files*.

        If a file name consists of single dash ('-'), it is interpreted as
        standard input.  If *ignore_missing* is true, non-existent files are
        ignored silently, otherwise they raise OSError.
        """
        unit_ini = UnitIni.from_files(paths=files, ignore_missing=ignore_missing)
        return cls(_unit_ini=unit_ini)

    def clone(self) -> Iterable[str]:
        """
        Return lines of INI file with the same data as in this object
        """
        return map(str, self._unit_ini.clone())

    def data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all INI data

        A flat dictionary is returned, mapping all valid keypaths to
        lists of lines.
        """
        return {
            str(key): [str(v) for v in values]
            for key, values in self._unit_ini.data().items()
        }

    def list_keys(self, section: str) -> Iterable[str]:
        """
        Return list of keys under *section*.
        """
        return map(str, self._unit_ini.list_keys(section))

    def list_paths(self) -> Iterable[str]:
        """
        Return list of all paths
        """
        return map(str, self._unit_ini.list_paths())

    def list_sections(self) -> Iterable[str]:
        """
        Return list of all sections
        """
        return map(str, self._unit_ini.list_sections())

    def raw_data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all raw INI data

        Same as .data(), but keeps in-line comments and leading/trailing
        whitespace around values.
        """
        return {
            str(key): [str(v) for v in values]
            for key, values in self._unit_ini.raw_data().items()
        }

    def raw_values(self, kpath: str) -> Iterable[str]:
        """
        Return list of raw values at key path *kpath*.

        Same as .values(), but keeps in-line comments and leading/trailing
        whitespace around values.
        """
        return map(str, self._unit_ini.raw_values(kpath))

    def raw_wrapper(self) -> DictWrapper:
        """
        Like .raw_data() but return DictWrapper with convenience access methods
        """
        return DictWrapper(data=self.raw_data())

    def wrapper(self) -> DictWrapper:
        """
        Like .data() but return DictWrapper with convenience access methods
        """
        return DictWrapper(data=self.data())

    def values(self, kpath: str) -> Iterable[str]:
        """
        Return list of values at key path *kpath*.
        """
        return map(str, self._unit_ini.values(kpath))


class Ini:
    """
    Set of cached INI files
    """

    @classmethod
    def from_files(cls, files: list[str]) -> Ini:
        """
        Initialize Ini object containing lines of all *files*.
        """
        cache = []
        for path in files:
            for line in SingleFileReader(path):
                cache.append(line)
        return cls(cache)

    @classmethod
    def from_existent_files(cls, files: list[str]) -> Ini:
        """
        Initialize Ini object containing lines of all existent *files*.

        Similar to Ini.from_files(), but non-existent files are silently
        ignored.
        """
        cache = []
        for path in files:
            if not os.path.exists(path):
                continue
            for line in SingleFileReader(path):
                cache.append(line)
        return cls(cache)

    def __init__(self, cache):
        self._cache = cache

    def branch(self, prefix: str) -> Ini:
        """
        Create new Ini object containing only sections that
        start with *prefix*.
        """
        want_scts: list[str] = []
        lines = []
        for sct in self.list_sections():
            if sct.startswith(prefix + '.'):
                want_scts.append(sct.replace(prefix + '.', '', 1))
        for sct in want_scts:
            lines.append('[%s]' % sct)
            for key in self.list_keys('%s.%s' % (prefix, sct)):
                branch_keypath = '%s.%s.%s' % (prefix, sct, key)
                for value in self.raw_values(branch_keypath):
                    lines.append('    %s =%s' % (key, value))
        return self.__class__(lines)

    def mkreader1(self, *kpath: str) -> Callable[[], str | None]:
        """
        Create function to read single-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either single-line string corresponding to value
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _read1(*kpath):
            out = list(self.values('.'.join(kpath)))
            if out:
                return out[0]
            return None
        return functools.partial(_read1, *kpath)

    def mkreaderN(self, *kpath: str) -> Callable[[], list[str]]:
        """
        Create function to read multi-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either list of strings corresponding to values
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _readN(*kpath):
            return list(self.values('.'.join(kpath)))
        return functools.partial(_readN, *kpath)

    def _cache_reader(self):
        for line in self._cache:
            yield line

    def data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all INI data

        Uses basic inigrep engine.

        A flat dictionary is returned, mapping all valid
        keypaths to lists of lines.
        """
        data: dict[str, list[str]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.values(kpath))
        return data

    def clone(self, kpath: str = '.') -> Iterable[str]:
        """
        Return lines of INI file with the same data as in this object
        """
        vg = _r_clone(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def raw_data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all raw INI data

        Same as Ini.data(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        data: dict[str, list[str]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.raw_values(kpath))
        return data

    def values(self, kpath: str) -> Iterable[str]:
        """
        Return list of values at key path *kpath*.

        Uses basic inigrep engine.
        """
        vg = _r_values(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def raw_values(self, kpath: str) -> Iterable[str]:
        """
        Return list of values at key path *kpath*.

        Same as Ini.values(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        vg = _r_raw_values(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def list_sections(self) -> Iterable[str]:
        """
        Return list of sections.

        Similar to Ini.values(), but uses section listing engine.
        """
        vg = _r_list_sections(
            reader=self._cache_reader(),
        )
        return (str(v) for v in vg)

    def list_keys(self, section: str) -> Iterable[str]:
        """
        Return list of keys under *section*.

        Similar to Ini.values(), but uses key listing engine.
        """
        vg = _r_list_keys(
            reader=self._cache_reader(),
            section=SectionT(section),
        )
        return (str(v) for v in vg)

    def list_paths(self, keypath: str = '.') -> Iterable[str]:
        """
        Return list of all defined key paths.

        Similar to Ini.values(), but uses key path listing engine.
        """
        vg = _r_list_paths(
            reader=self._cache_reader(),
            keypath=KeypathT(keypath),
        )
        return (str(v) for v in vg)
