from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.type import forall

__all__ = (
    'Either',
    'Left',
    'Right',
)


a = TypeVar('a')

b = TypeVar('b')


@dataclass(frozen=True)
class Left(forall[a]):
    x : a


@dataclass(frozen=True)
class Right(forall[b]):
    y : b


Either = Left[a] | Right[b]
