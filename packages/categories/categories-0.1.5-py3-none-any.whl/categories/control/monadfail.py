from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.control.monad import Monad, MonadIO, MonadList, MonadMaybe
from categories.data.maybe import Maybe, Nothing, Just
from categories.type import IO, hkt, typeclass

__all__ = (
    'MonadFail',
    'MonadFailIO',
    'MonadFailList',
    'MonadFailMaybe',
)


a = TypeVar('a')

m = TypeVar('m')


@dataclass(frozen=True)
class MonadFail(Monad[m], typeclass[m]):
    def fail(self, x : str, /) -> hkt[m, a]: ...


@dataclass(frozen=True)
class MonadFailIO(MonadIO, MonadFail[IO]):
    async def fail(self, x : str, /) -> a:
        raise Exception(x)


@dataclass(frozen=True)
class MonadFailList(MonadList, MonadFail[list]):
    def fail(self, _ : str, /) -> list[a]:
        return []


@dataclass(frozen=True)
class MonadFailMaybe(MonadMaybe, MonadFail[Maybe]):
    def fail(self, _ : str, /) -> Maybe[a]:
        return Nothing()
