from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.type import forall

__all__ = (
    'Node',
)


a = TypeVar('a')


@dataclass(frozen=True)
class Node(forall[a]):
    x  : a
    xs : list[Node[a]]
