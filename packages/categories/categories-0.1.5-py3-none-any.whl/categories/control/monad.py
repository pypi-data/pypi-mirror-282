from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.control.applicative import Applicative, ApplicativeEither, ApplicativeIO, ApplicativeIdentity, ApplicativeLambda, ApplicativeList, ApplicativeMaybe, ApplicativeNode, ApplicativeParser
from categories.data.either import Either, Left, Right
from categories.data.identity import Identity
from categories.data.maybe import Maybe, Nothing, Just
from categories.data.node import Node
from categories.text.parser import Parser
from categories.type import IO, Lambda, _, hkt, typeclass

__all__ = (
    'Monad',
    'MonadEither',
    'MonadIO',
    'MonadIdentity',
    'MonadLambda',
    'MonadList',
    'MonadMaybe',
    'MonadNode',
    'MonadParser',
)


a = TypeVar('a')

b = TypeVar('b')

e = TypeVar('e')

m = TypeVar('m')

r = TypeVar('r')


@dataclass(frozen=True)
class Monad(Applicative[m], typeclass[m]):
    def bind(self, m : hkt[m, a], k : Lambda[a, hkt[m, b]], /) -> hkt[m, b]:
        return self.join(self.map(k, m))

    def join(self, m : hkt[m, hkt[m, a]], /) -> hkt[m, a]:
        return self.bind(m, lambda x, /: x)

    def seq(self, m : hkt[m, a], k : hkt[m, b], /) -> hkt[m, b]:
        return self.bind(m, lambda _, /: k)


@dataclass(frozen=True)
class MonadEither(ApplicativeEither, Monad[Either[e, _]]):
    def bind(self, e : Either[e, a], k : Lambda[a, Either[e, b]], /) -> Either[e, b]:
        match e:
            case Left(x):
                return Left(x)
            case Right(y):
                return k(y)


@dataclass(frozen=True)
class MonadIO(ApplicativeIO, Monad[IO]):
    async def bind(self, m : IO[a], k : Lambda[a, IO[b]], /) -> b:
        match await m:
            case x:
                return await k(x)

    async def join(self, m : IO[IO[a]], /) -> a:
        match await m:
            case x:
                return await x


@dataclass(frozen=True)
class MonadIdentity(ApplicativeIdentity, Monad[Identity]):
    def bind(self, m : Identity[a], k : Lambda[a, Identity[b]], /) -> Identity[b]:
        match m:
            case Identity(x):
                return k(x)


@dataclass(frozen=True)
class MonadLambda(ApplicativeLambda[r], Monad[Lambda[r, _]]):
    def bind(self, f : Lambda[r, a], k : Lambda[a, Lambda[r, b]], /) -> Lambda[r, b]:
        return lambda r, /: k(f(r))(r)


@dataclass(frozen=True)
class MonadList(ApplicativeList, Monad[list]):
    def bind(self, xs : list[a], f : Lambda[a, list[b]], /) -> list[b]:
        return [y for x in xs for y in f(x)]

    def join(self, xss : list[list[a]], /) -> list[a]:
        return [x for xs in xss for x in xs]


@dataclass(frozen=True)
class MonadMaybe(ApplicativeMaybe, Monad[Maybe]):
    def bind(self, m : Maybe[a], k : Lambda[a, Maybe[b]], /) -> Maybe[b]:
        match m:
            case Nothing():
                return Nothing()
            case Just(x):
                return k(x)


@dataclass(frozen=True)
class MonadNode(ApplicativeNode, Monad[Node]):
    def bind(self, n : Node[a], k : Lambda[a, Node[b]], /) -> Node[b]:
        match n:
            case Node(x, xs):
                match k(x):
                    case Node(y, ys):
                        return Node(y, ys + [self.bind(x, k) for x in xs])


@dataclass(frozen=True)
class MonadParser(ApplicativeParser, Monad[Parser]):
    def bind(self, p : Parser[a], k : Lambda[a, Parser[b]], /) -> Parser[b]:
        return lambda s, /: [(y, s) for (x, s) in p(s) for (y, s) in k(x)(s)]
