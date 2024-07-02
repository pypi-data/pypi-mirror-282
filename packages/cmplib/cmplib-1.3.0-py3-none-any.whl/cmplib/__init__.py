# SPDX-License-Identifier: LGPL-3.0-only
# Copyright (C) 2023 Michał Góral.

import importlib.metadata as importlib_metadata
import re
from datetime import date, datetime
from fnmatch import fnmatchcase
from typing import Any, Callable, Dict, Optional

__title__ = "cmplib"
__description__ = "Writing composable matchers"
__author__ = "Michał Góral (dev@goral.net.pl)"
__version__ = importlib_metadata.version("cmplib")
__copyright__ = "Copyright (c) Michał Góral"
__license__ = "LGPL-3.0-only"

# NOTE: __all__ is managed by @api decorator. We only keep here names of
# objects which can't be decorated.
__all__ = ["SKIP"]


def api(lhs):
    __all__.append(lhs.__name__)
    return lhs


@api
class Cmp:
    def match(self, other: Any) -> bool:
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        try:
            return self.match(other)
        except (TypeError, ValueError):
            return False

    def __and__(self, other: Any) -> Any:
        return _compose(And, self, other)

    def __or__(self, other: Any) -> Any:
        return _compose(Or, self, other)


@api
class And(Cmp):
    def __init__(self, *cmps: Cmp):
        self.cmps = cmps

    def match(self, other):
        return all(c == other for c in self.cmps)

    def __repr__(self):
        s = []
        for c in self.cmps:
            s.append(repr(c))
        return "(" + " AND ".join(s) + ")"


@api
class Or(Cmp):
    def __init__(self, *cmps: Cmp):
        self.cmps = cmps

    def match(self, other):
        return any(c == other for c in self.cmps)

    def __repr__(self):
        s = []
        for c in self.cmps:
            if isinstance(c, Cmp):
                s.append(repr(c))
            else:
                s.append(f"equals {repr(c)}")
        return "(" + " OR ".join(s) + ")"


@api
class Each(Cmp):
    def __init__(self, cmp: Cmp):
        self.cmp = cmp

    def match(self, other):
        return all(self.cmp == elem for elem in other)

    def __repr__(self):
        return f"Each element equals {repr(self.cmp)}"


@api
class Values(Cmp):
    def __init__(self, cmp: Cmp, *, at_least: int = 1):
        # TODO: is there a point in allowing at_least 0 values?
        assert at_least >= 0
        self.cmp = cmp
        self.at_least = at_least

    def match(self, other):
        match = 0
        for el in other:
            if self.cmp == el:
                match += 1
                if match >= self.at_least:
                    return True
        return match >= self.at_least

    def __repr__(self):
        if self.at_least == 0:
            return f"0 or more values equal {repr(self.cmp)}"
        if self.at_least == 1:
            return f"any value equals {repr(self.cmp)}"
        return f"at least {self.at_least} values equal {repr(self.cmp)}"


@api
class Not(Cmp):
    def __init__(self, cmp: Cmp):
        self.cmp = cmp

    def match(self, other):
        return self.cmp != other

    def __repr__(self):
        return f"~{repr(self.cmp)}"


@api
class Eq(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return self.val == other

    def __repr__(self):
        return f"{repr(self.val)}"


@api
class Ne(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return self.val != other

    def __repr__(self):
        return f"!{repr(self.val)}"


@api
class Gt(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return other > self.val

    def __repr__(self):
        return f"greater than {repr(self.val)}"


@api
class Ge(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return other >= self.val

    def __repr__(self):
        return f"greater equal than {repr(self.val)}"


@api
class Lt(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return other < self.val

    def __repr__(self):
        return f"less than {repr(self.val)}"


@api
class Le(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return other <= self.val

    def __repr__(self):
        return f"less equal than {repr(self.val)}"


@api
class Truish(Cmp):
    def match(self, other):
        return bool(other)

    def __repr__(self):
        return "maps to true"


@api
class Is(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        return self.val is other

    def __repr__(self):
        return f"is {repr(self.val)}"


@api
class IsNone(Cmp):
    def match(self, other):
        return other is None

    def __repr__(self):
        return "is None"


@api
class IsEmpty(Cmp):
    def match(self, other):
        return len(other) == 0

    def __repr__(self):
        return "is empty"


@api
class Glob(Cmp):
    def __init__(self, pat: str, coerce=False, case=True):
        self.pat = pat
        self.coerce = coerce
        self.case = case

    def match(self, other):
        if self.coerce:
            other = str(other)
        if not self.case:
            return fnmatchcase(other.lower(), self.pat.lower())
        return fnmatchcase(other, self.pat)

    def __repr__(self):
        return f"matches glob {self.pat}"


@api
class Re(Cmp):
    # NOTE: we use flags = 0 instead of  re.NOFLAG, because NOFLAG was added in
    # Python 3.11 and at the time of writing it cmplib supports older Python
    # versions (3.8)
    def __init__(self, pat: str, flags: re.RegexFlag | int = 0, coerce=False):
        self._rawpat = pat
        self.pat = re.compile(pat, flags)
        self.coerce = coerce

    def match(self, other):
        if self.coerce:
            other = str(other)

        # NOTE: we use re.match instead of re.search to keep the behaviour
        # similar to Glob()
        return self.pat.match(other) is not None

    def __repr__(self):
        return f"matches regular expression {self._rawpat}"


@api
class Contains(Cmp):
    def __init__(self, val):
        self.val = val

    def match(self, other):
        if isinstance(self.val, Cmp):
            return any(obj == self.val for obj in other)
        return self.val in other

    def __repr__(self):
        return f"(contains {repr(self.val)})"


@api
class Unordered(Cmp):
    def __init__(self, *cmps: Any):
        self.cmps = cmps

    def match(self, other):
        used_matchers = set()
        for elem in other:
            for i, c in enumerate(self.cmps):
                if i not in used_matchers and elem == c:
                    used_matchers.add(i)
                    break
            else:
                return False

        return len(used_matchers) == len(self.cmps)

    def __repr__(self):
        s = []
        for c in self.cmps:
            s.append(repr(c))
        return "(in any order" "; ".join(s) + ")"


@api
class Len(Cmp):
    def __init__(self, cmp: Any):
        self.cmp = cmp

    def match(self, other):
        return self.cmp == len(other)

    def __repr__(self):
        return f"len equals {repr(self.cmp)}"


@api
class KeyEq(Cmp):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def match(self, other):
        try:
            return other[self.key] == self.val
        except (IndexError, KeyError):
            return False

    def __repr__(self):
        if isinstance(self.val, Cmp):
            return f"value of key '{self.key}' {repr(self.val)}"
        return f"value of key '{self.key}' equals {repr(self.val)}"


@api
class AttrEq(Cmp):
    def __init__(self, attr, val):
        self.attr = attr
        self.val = val

    def match(self, other):
        try:
            return getattr(other, self.attr) == self.val
        except AttributeError:
            return False

    def __repr__(self):
        if isinstance(self.val, Cmp):
            return f"object.{self.attr} {repr(self.val)}"
        return f"object.{self.attr} equals {repr(self.val)}"


@api
class IsInstance(Cmp):
    def __init__(self, cls):
        self.cls = cls

    def match(self, other):
        return isinstance(other, self.cls)

    def __repr__(self):
        return f"object is instance of {self.cls}"


@api
class CanBeTimestamp(Cmp):
    def match(self, other):
        return isinstance(other, (int, float, str)) and float(other) >= 0

    def __repr__(self):
        return "is timestamp"


@api
class IsIsoDateTime(Cmp):
    def match(self, other):
        if isinstance(other, date):
            return True

        try:
            datetime.fromisoformat(other)
        except ValueError:
            return False
        return True

    def __repr__(self):
        return "is ISO date-time"


@api
class IsUnique(Cmp):
    _UNIQUE_CACHE: Dict[Any, Any] = {}

    def __init__(self, cacheid: Optional[str] = None):
        if cacheid is None:
            cacheid = self._generate_unique_cache_id()
        self.values_container = IsUnique._UNIQUE_CACHE.setdefault(cacheid, set())

    def match(self, other):
        ret = other not in self.values_container
        self.values_container.add(other)
        return ret

    def __repr__(self) -> str:
        return "is unique"

    @classmethod
    def clear(cls, name=None):
        if not name:
            cls._UNIQUE_CACHE = {}
        cls._UNIQUE_CACHE.pop(name, None)

    def _generate_unique_cache_id(self):
        cacheid = len(IsUnique._UNIQUE_CACHE)
        while cacheid in IsUnique._UNIQUE_CACHE:
            cacheid += 1
        return cacheid


@api
class Fn(Cmp):
    """Matches true when fn(val) is True. When coerce=True, fn doesn't have to
    return a bool, but instead its return value is cast to bool."""

    def __init__(self, fn: Callable[[Any], bool], coerce=False):
        self.fn = fn
        self.coerce = coerce

    def match(self, other) -> bool:
        if self.coerce:
            return bool(self.fn(other)) is True
        return self.fn(other) is True

    def __repr__(self) -> str:
        return f"call to function {self.fn.__name__}(value) returns true"


@api
def Object(_cls=None, **kw):
    matchers = []
    if _cls:
        matchers = [IsInstance(_cls)]
    matchers.extend(AttrEq(k, v) for k, v in kw.items())
    return And(*matchers)


@api
def DictFields(**kw):
    matchers = [KeyEq(k, v) for k, v in kw.items()]
    return And(*matchers)


@api
def Items(*a):
    matchers = [KeyEq(k, v) for k, v in a]
    return And(*matchers)


@api
class Skip(Cmp):
    def match(self, other):
        return True

    def __repr__(self):
        return "<SKIP>"


SKIP = Skip()


def _compose(cls, lhs, rhs):
    cmps = []
    for c in (lhs, rhs):
        if isinstance(c, cls):
            cmps.extend(c.cmps)
        elif isinstance(c, Cmp):
            cmps.append(c)
        else:
            cmps.append(Eq(c))
    return cls(*cmps)
