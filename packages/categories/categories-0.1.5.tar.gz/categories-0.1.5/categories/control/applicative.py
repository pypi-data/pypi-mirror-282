from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.data.either import Either, Left, Right
from categories.data.functor import Functor, FunctorEither, FunctorIO, FunctorIdentity, FunctorLambda, FunctorList, FunctorMaybe, FunctorNode, FunctorParser
from categories.data.identity import Identity
from categories.data.maybe import Maybe, Nothing, Just
from categories.data.node import Node
from categories.text.parser import Parser
from categories.type import IO, Lambda, _, hkt, typeclass

__all__ = (
    'Applicative',
    'ApplicativeEither',
    'ApplicativeIO',
    'ApplicativeIdentity',
    'ApplicativeLambda',
    'ApplicativeList',
    'ApplicativeMaybe',
    'ApplicativeNode',
    'ApplicativeParser',
)


a = TypeVar('a')

b = TypeVar('b')

e = TypeVar('e')

f = TypeVar('f')

r = TypeVar('r')


@dataclass(frozen=True)
class Applicative(Functor[f], typeclass[f]):
    def pure(self, x : a, /) -> hkt[f, a]: ...

    def apply(self, f : hkt[f, Lambda[a, b]], x : hkt[f, a], /) -> hkt[f, b]: ...

    def seq(self, _ : hkt[f, a], x : hkt[f, b], /) -> hkt[f, b]:
        return self.apply(self.const(lambda x, /: x, _), x)


@dataclass(frozen=True)
class ApplicativeEither(FunctorEither, Applicative[Either[e, _]]):
    def pure(self, x : a, /) -> Either[e, a]:
        return Right(x)

    def apply(self, e : Either[e, Lambda[a, b]], e_ : Either[e, a], /) -> Either[e, b]:
        match e:
            case Left(x):
                return Left(x)
            case Right(f):
                return self.map(f, e_)


@dataclass(frozen=True)
class ApplicativeIO(FunctorIO, Applicative[IO]):
    async def pure(self, x : a, /) -> a:
        return x

    async def apply(self, m : IO[Lambda[a, b]], m_ : IO[a], /) -> b:
        match await m, await m_:
            case f, x:
                return f(x)

    async def seq(self, m : IO[a], k : IO[b], /) -> b:
        match await m:
            case _:
                return await k


@dataclass(frozen=True)
class ApplicativeIdentity(FunctorIdentity, Applicative[Identity]):
    def pure(self, x : a, /) -> Identity[a]:
        return Identity(x)

    def apply(self, f : Identity[Lambda[a, b]], x : Identity[a], /) -> Identity[b]:
        match f, x:
            case Identity(f), Identity(x):
                return Identity(f(x))


@dataclass(frozen=True)
class ApplicativeLambda(FunctorLambda[r], Applicative[Lambda[r, _]]):
    def pure(self, x : a, /) -> Lambda[r, a]:
        return lambda _, /: x

    def apply(self, f : Lambda[r, Lambda[a, b]], g : Lambda[r, a], /) -> Lambda[r, b]:
        return lambda x, /: f(x)(g(x))


@dataclass(frozen=True)
class ApplicativeList(FunctorList, Applicative[list]):
    def pure(self, x : a, /) -> list[a]:
        return [x]

    def apply(self, fs : list[Lambda[a, b]], xs : list[a], /) -> list[b]:
        return [f(x) for f in fs for x in xs]


@dataclass(frozen=True)
class ApplicativeMaybe(FunctorMaybe, Applicative[Maybe]):
    def pure(self, x : a, /) -> Maybe[a]:
        return Just(x)

    def apply(self, m : Maybe[Lambda[a, b]], m_ : Maybe[a], /) -> Maybe[b]:
        match m:
            case Nothing():
                return Nothing()
            case Just(f):
                return self.map(f, m_)


@dataclass(frozen=True)
class ApplicativeNode(FunctorNode, Applicative[Node]):
    def pure(self, x : a, /) -> Node[a]:
        return Node(x, [])

    def apply(self, n : Node[Lambda[a, b]], n_ : Node[a], /) -> Node[b]:
        match n, n_:
            case Node(f, fs), Node(x, xs):
                return Node(f(x), [self.map(f, x) for x in xs] + [self.apply(f, n_) for f in fs])

    def seq(self, _ : Node[a], n : Node[b], /) -> Node[b]:
        match _, n:
            case Node(_, xs), Node(y, ys):
                return Node(y, ys + [self.seq(x, n) for x in xs])


@dataclass(frozen=True)
class ApplicativeParser(FunctorParser, Applicative[Parser]):
    def pure(self, x : a, /) -> Parser[a]:
        return lambda s, /: [(x, s)]

    def apply(self, p : Parser[Lambda[a, b]], q : Parser[a], /) -> Parser[b]:
        return lambda s, /: [(f(x), s) for (f, s) in p(s) for (x, s) in q(s)]
