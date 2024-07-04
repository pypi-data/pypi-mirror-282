from __future__ import annotations

import builtins
from copy import deepcopy
import functools
from dataclasses import dataclass
import itertools
from typing import Callable, Generic, Iterable, List, Protocol, Tuple, TypeVar

from entoli.data.maybe import Just, Maybe, Nothing
from entoli.data.monad import Monad
from entoli.data.ord import Ord
from entoli.data.seq import Seq

_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")

# Tuple


def fst(pair: Tuple[_A, _B]) -> _A:
    return pair[0]


def _test_fst():
    assert fst((1, 2)) == 1


def snd(pair: Tuple[_A, _B]) -> _B:
    return pair[1]


def _test_snd():
    assert snd((1, 2)) == 2


def curry(f: Callable[[_A, _B], _C]) -> Callable[[_A], Callable[[_B], _C]]:
    return lambda x: lambda y: f(x, y)


def _test_curry():
    def _add(x, y):
        return x + y

    assert curry(_add)(1)(2) == 3  # type : ignore


def uncurry(f: Callable[[_A], Callable[[_B], _C]]) -> Callable[[_A, _B], _C]:
    return lambda x, y: f(x)(y)


def _test_uncurry():
    assert uncurry(lambda x: lambda y: x + y)(1, 2) == 3  # type: ignore


# Folds and traversals


def foldl(f: Callable[[_A, _B], _A], acc: _A, xs: Iterable[_B]) -> _A:
    return functools.reduce(f, xs, acc)


def _test_foldl():
    assert foldl(lambda acc, x: acc + x, 0, []) == 0
    assert foldl(lambda acc, x: acc + x, 0, [1]) == 1
    assert foldl(lambda acc, x: acc + x, 0, [1, 2, 3]) == 6


def foldr(f: Callable[[_A, _B], _B], acc: _B, xs: Iterable[_A]) -> _B:
    return functools.reduce(lambda acc, x: f(x, acc), reversed(list(xs)), acc)


def _test_foldr():
    assert foldr(lambda x, acc: x + acc, 0, []) == 0
    assert foldr(lambda x, acc: x + acc, 0, [1]) == 1
    assert foldr(lambda x, acc: x + acc, 0, [1, 2, 3]) == 6


def elem(x: _A, xs: Iterable[_A]) -> bool:
    return x in xs


def _test_elem():
    assert not elem(1, [])
    assert elem(1, [1, 2, 3])
    assert not elem(4, [1, 2, 3])

    @dataclass(frozen=True, slots=True)
    class PyIdent:
        module: List[str]
        qual_name: List[str]

    ident_0 = PyIdent(
        module=["auto_generated", "some_package", "some_module"], qual_name=["greet_0"]
    )
    ident_1 = PyIdent(
        module=["auto_generated", "some_package", "some_module"], qual_name=["greet_1"]
    )

    assert elem(ident_0, [ident_0, ident_1])
    assert not elem(ident_0, [ident_1])


# maximum, minimum, sum, product, any, all are built-in functions

# def traverse(
#     f: Callable[[_A], Applicative[_B]], xs: Iterable[_A]
# ) -> Applicative[Iterable[_B]]:


# def sequence(
#     mas : Iterable[Monad[_A]]
# ) -> Monad[Iterable[_A]]:


# Miscellaneous functions


def id(x: _A) -> _A:
    return x


# List operations


def map(f: Callable[[_A], _B], xs: Iterable[_A]) -> Iterable[_B]:
    return Seq(lambda: builtins.map(f, xs))


def _test_map():
    assert map(lambda x: x + 1, []) == []
    assert map(lambda x: x + 1, [1]) == [2]
    assert map(lambda x: x + 1, [1, 2]) == [2, 3]


def append(xs: Iterable[_A], ys: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.chain(xs, ys))


def _test_append():
    assert append([], []) == []
    assert append([], [1]) == [1]
    assert append([1], []) == [1]
    assert append([1], [2]) == [1, 2]
    assert append([1, 2], [3, 4]) == [1, 2, 3, 4]


def filter(f: Callable[[_A], bool], xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: builtins.filter(f, xs))


def _test_filter():
    assert filter(lambda x: x % 2 == 0, []) == []
    assert filter(lambda x: x % 2 == 0, [1]) == []
    assert filter(lambda x: x % 2 == 0, [1, 2]) == [2]
    assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]


def head(xs: Iterable[_A]) -> _A:
    """
    Return the first element of the iterable.
    The iterable must not be empty.
    """
    return next(iter(xs))


def _test_head():
    try:
        head([])
        assert False
    except StopIteration:
        assert True

    assert head([1]) == 1
    assert head([1, 2]) == 1


def last(xs: Iterable[_A]) -> _A:
    """
    Return the last element of the iterable.
    The iterable must not be empty.
    """
    return functools.reduce(lambda _, x: x, xs)


def _test_last():
    try:
        last([])
        assert False
    except TypeError:
        assert True

    assert last([1]) == 1
    assert last([1, 2]) == 2
    assert last([1, 2, 3]) == 3


def tail(xs: Iterable[_A]) -> Iterable[_A]:
    """
    Return all elements of the iterable except the first one.
    The iterable must be finite and non-empty.
    """

    def _tail():
        it = iter(xs)
        next(it)
        return it

    return Seq(_tail)


def _test_tail():
    # ! Applying tail to an empty list is undefined
    # ! Defining tail of an empty list if self will not raise an error
    # ! However, calling tail of an empty list will raise an error
    try:
        next(iter(tail([])))
        assert False
    except StopIteration:
        assert True

    assert tail([1]) == []
    assert tail([1, 2]) == [2]
    assert tail([1, 2, 3]) == [2, 3]


def init(xs: Iterable[_A]) -> Iterable[_A]:
    """
    Return all elements of the iterable except the last one.
    The iterable must be finite and non-empty.
    """

    def init_():
        it = iter(xs)
        prev = next(it)
        for curr in it:
            yield prev
            prev = curr

    return Seq(init_)


def _test_init():
    # ! Applying init to an empty list is undefined
    # ! Defining init of an empty list if self will not raise an error
    # ! However, calling init of an empty list will raise an error

    try:
        next(iter(init([])))
        assert False
    except Exception:
        assert True

    assert init([1]) == []
    assert init([1, 2]) == [1]
    assert init([1, 2, 3]) == [1, 2]


def nth(xs: Iterable[_A], n: int) -> _A:
    """
    Return the n-th element of the iterable.
    The iterable must have at least n elements.
    """
    return next(x for i, x in enumerate(xs) if i == n)


def _test_nth():
    assert nth([1], 0) == 1
    assert nth([1, 2], 1) == 2
    assert nth([1, 2, 3], 2) == 3


def null(xs: Iterable[_A]) -> bool:
    try:
        next(iter(xs))
        return False
    except StopIteration:
        return True


def _test_null():
    assert null([])
    assert not null([1])
    assert null({})
    assert not null({1: 2})
    assert null("")
    assert not null("a")


def length(xs: Iterable[_A]) -> int:
    return sum(1 for _ in xs)


def _test_length():
    assert length([]) == 0
    assert length([1]) == 1
    assert length([1, 2]) == 2
    assert length([1, 2, 3]) == 3


def reverse(xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: reversed(list(xs)))


def _test_reverse():
    assert reverse([]) == []
    assert reverse([1]) == [1]
    assert reverse([1, 2]) == [2, 1]
    assert reverse([1, 2, 3]) == [3, 2, 1]


# and, or, any, all are reserved keywords and built-in functions


def concat(xss: Iterable[Iterable[_A]]) -> Iterable[_A]:
    return Seq(lambda: itertools.chain.from_iterable(xss))


def _test_concat():
    assert concat([]) == []
    assert concat([[], []]) == []
    assert concat([[1], [2]]) == [1, 2]
    assert concat([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert concat([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]


def concat_map(f: Callable[[_A], Iterable[_B]], xs: Iterable[_A]) -> Iterable[_B]:
    return Seq(lambda: (y for x in xs for y in f(x)))


def _test_concat_map():
    assert concat_map(lambda x: [], []) == []
    assert concat_map(lambda x: [], [1, 2]) == []
    assert concat_map(lambda x: [x + 1], []) == []
    assert concat_map(lambda x: [x + 1], [1]) == [2]
    assert concat_map(lambda x: [x + 1], [1, 2]) == [2, 3]
    assert concat_map(lambda x: [x + 1, x + 2], []) == []
    assert concat_map(lambda x: [x + 1, x + 2], [1, 2]) == [2, 3, 3, 4]


# Building lists


def scanl(f: Callable[[_B, _A], _B], acc: _B, xs: Iterable[_A]) -> Iterable[_B]:
    def _scanl():
        acc_mut = deepcopy(acc)
        yield acc_mut
        for x in xs:
            acc_mut = f(acc_mut, x)
            yield acc_mut

    return Seq(_scanl)


def _test_scanl():
    assert scanl(lambda acc, x: acc + x, 0, []) == [0]
    assert scanl(lambda acc, x: acc + x, 0, [1]) == [0, 1]
    assert scanl(lambda acc, x: acc + x, 0, [1, 2]) == [0, 1, 3]


def scanl1(f: Callable[[_A, _A], _A], xs: Iterable[_A]) -> Seq[_A]:
    def _scanl1():
        it = iter(xs)
        try:
            acc = next(it)
            yield acc
            for x in it:
                acc = f(acc, x)
                yield acc
        except StopIteration:
            return

    return Seq(_scanl1)


def _test_scanl1():
    assert scanl1(lambda acc, x: acc + x, []) == []
    assert scanl1(lambda acc, x: acc + x, [1]) == [1]
    assert scanl1(lambda acc, x: acc + x, [1, 2]) == [1, 3]


# todo scanr, scanr1

# def scanr(f: Callable[[_A, _B], _B], acc: _B, xs: Iterable[_A]) -> Iterable[_B]:
#     def _scanr():
#         acc_mut = deepcopy(acc)
#         accs = []
#         for x in reversed(list(xs)):
#             acc_mut = f(x, acc_mut)
#             accs.append(acc_mut)
#         return reversed(accs)

#     return Seq(_scanr)


# def _test_scanr():
#     assert scanr(lambda x, acc: x + acc, 0, []) == [0]
#     assert scanr(lambda x, acc: x + acc, 0, [1]) == [1, 0]
#     assert scanr(lambda x, acc: x + acc, 0, [1, 2]) == [3, 2, 0]


# Infinite lists


def iterate(f: Callable[[_A], _A], x: _A) -> Iterable[_A]:
    def _iterate():
        x_ = deepcopy(x)
        while True:
            yield x_
            x_ = f(x_)

    return Seq(_iterate)


def _test_iterate():
    nat = iterate(lambda x: x + 1, 0)
    assert take(3, nat) == [0, 1, 2]


def repeat(x: _A) -> Iterable[_A]:
    def _repeat():
        while True:
            yield x

    return Seq(_repeat)


def _test_repeat():
    assert take(3, repeat(1)) == [1, 1, 1]


def replicate(n: int, x: _A) -> Iterable[_A]:
    def _replicate():
        for _ in range(n):
            yield x

    return Seq(_replicate)


def _test_replicate():
    assert replicate(0, 1) == []
    assert replicate(1, 1) == [1]
    assert replicate(2, 1) == [1, 1]


def cycle(xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.cycle(xs))


def _test_cycle():
    assert take(3, cycle([])) == []
    assert take(3, cycle([1])) == [1, 1, 1]
    assert take(3, cycle([1, 2])) == [1, 2, 1]


# Sublists


def take(n: int, xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.islice(xs, n))


def _test_take():
    assert take(0, []) == []
    assert take(0, [1]) == []
    assert take(1, [1]) == [1]
    assert take(1, [1, 2]) == [1]
    assert take(2, [1, 2]) == [1, 2]
    assert take(2, [1, 2, 3]) == [1, 2]


def drop(n: int, xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.islice(xs, n, None))


def _test_drop():
    assert drop(0, []) == []
    assert drop(0, [1]) == [1]
    assert drop(1, [1]) == []
    assert drop(1, [1, 2]) == [2]
    assert drop(2, [1, 2]) == []
    assert drop(2, [1, 2, 3]) == [3]


def take_while(f: Callable[[_A], bool], xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.takewhile(f, xs))


def _test_take_while():
    assert take_while(lambda x: x < 3, []) == []
    assert take_while(lambda x: x < 3, [1]) == [1]
    assert take_while(lambda x: x < 3, [1, 2]) == [1, 2]
    assert take_while(lambda x: x < 3, [1, 2, 3]) == [1, 2]


def drop_while(f: Callable[[_A], bool], xs: Iterable[_A]) -> Iterable[_A]:
    return Seq(lambda: itertools.dropwhile(f, xs))


def _test_drop_while():
    assert drop_while(lambda x: x < 3, []) == []
    assert drop_while(lambda x: x < 3, [1]) == []
    assert drop_while(lambda x: x < 3, [1, 2]) == []
    assert drop_while(lambda x: x < 3, [1, 2, 3]) == [3]


def span(
    f: Callable[[_A], bool], xs: Iterable[_A]
) -> Tuple[Iterable[_A], Iterable[_A]]:
    return take_while(f, xs), drop_while(f, xs)


def _test_span():
    assert span(lambda x: x < 3, []) == ([], [])
    assert span(lambda x: x < 3, [1]) == ([1], [])
    assert span(lambda x: x < 3, [1, 2]) == ([1, 2], [])
    assert span(lambda x: x < 3, [1, 2, 3]) == ([1, 2], [3])


# no break since it is a keyword


def split_at(n: int, xs: Iterable[_A]) -> Tuple[Iterable[_A], Iterable[_A]]:
    return take(n, xs), drop(n, xs)


def _test_split_at():
    assert split_at(0, []) == ([], [])
    assert split_at(0, [1]) == ([], [1])
    assert split_at(1, [1]) == ([1], [])
    assert split_at(1, [1, 2]) == ([1], [2])
    assert split_at(2, [1, 2]) == ([1, 2], [])
    assert split_at(2, [1, 2, 3]) == ([1, 2], [3])


# Searching lists


def not_elem(x: _A, xs: Iterable[_A]) -> bool:
    return x not in xs


def _test_not_elem():
    assert not_elem(1, [])
    assert not not_elem(1, [1, 2, 3])
    assert not_elem(4, [1, 2, 3])


def lookup(x: _A, xs: Iterable[Tuple[_A, _B]]) -> Maybe[_B]:
    for k, v in xs:
        if k == x:
            return Just(v)
    return Nothing()


def _test_lookup():
    assert lookup(1, []) == Nothing()
    assert lookup(1, [(1, 2)]) == Just(2)
    assert lookup(1, [(2, 3)]) == Nothing()
    assert lookup(1, [(2, 3), (1, 2)]) == Just(2)


# Zipping and unzipping lists


def zip(xs: Iterable[_A], ys: Iterable[_B]) -> Iterable[Tuple[_A, _B]]:
    return Seq(lambda: builtins.zip(xs, ys))


def _test_zip():
    assert zip([], []) == []
    assert zip([1], []) == []
    assert zip([], [1]) == []
    assert zip([1], [2]) == [(1, 2)]
    assert zip([1, 2], [3, 4]) == [(1, 3), (2, 4)]


def zip_with(
    f: Callable[[_A, _B], _C], xs: Iterable[_A], ys: Iterable[_B]
) -> Iterable[_C]:
    return Seq(lambda: (f(x, y) for x, y in builtins.zip(xs, ys)))


def _test_zip_with():
    assert zip_with(lambda x, y: x + y, [], []) == []
    assert zip_with(lambda x, y: x + y, [1], []) == []
    assert zip_with(lambda x, y: x + y, [], [1]) == []
    assert zip_with(lambda x, y: x + y, [1], [2]) == [3]
    assert zip_with(lambda x, y: x + y, [1, 2], [3, 4]) == [4, 6]


def unzip(pairs: Iterable[Tuple[_A, _B]]) -> Tuple[Iterable[_A], Iterable[_B]]:
    if not pairs:
        return [], []
    else:

        def _a():
            for a, _ in pairs:
                yield a

        def _b():
            for _, b in pairs:
                yield b

        return Seq(_a), Seq(_b)


def _test_unzip():
    assert unzip([]) == ([], [])
    assert unzip([(1, 2)]) == ([1], [2])
    assert unzip([(1, 2), (3, 4)]) == ([1, 3], [2, 4])


# Functions on strings


def lines(s: str) -> Iterable[str]:
    return Seq.from_iter(s.splitlines())


def _test_lines():
    assert lines("") == []
    assert lines("\n") == [""]
    assert lines("a\nb") == ["a", "b"]
    assert lines("a\nb\n") == ["a", "b"]  # ! Last empty line is removed


def words(s: str) -> Iterable[str]:
    return Seq.from_iter(s.split())


def _test_words():
    assert words("") == []
    assert words("a") == ["a"]
    assert words("a b") == ["a", "b"]
    assert words("a b ") == ["a", "b"]


def unlines(xs: Iterable[str]) -> str:
    if not xs:
        return ""
    else:
        return "\n".join(xs)


def _test_unlines():
    assert unlines([]) == ""
    assert unlines([""]) == ""
    assert unlines(["a", "b"]) == "a\nb"
    assert unlines(["a", "b", ""]) == "a\nb\n"


def unwords(xs: Iterable[str]) -> str:
    return " ".join(xs).strip()


def _test_unwords():
    assert unwords([]) == ""
    assert unwords([""]) == ""
    assert unwords(["a"]) == "a"
    assert unwords(["a", "b"]) == "a b"
    assert unwords(["a", "b", ""]) == "a b"


# io

_A = TypeVar("_A")
_B = TypeVar("_B")


@dataclass(frozen=True, slots=True)
class Io(Generic[_A], Monad[_A]):
    action: Callable[[], _A]

    def fmap(self, f: Callable[[_A], _B]) -> Io[_B]:
        return Io(lambda: f(self.action()))

    @staticmethod
    def pure(x: _A) -> Io[_A]:
        return Io(lambda: x)

    def ap(self, f: Io[Callable[[_A], _B]]) -> Io[_B]:
        return Io(lambda: f.action()(self.action()))

    def and_then(self, f: Callable[[_A], Io[_B]]) -> Io[_B]:
        return Io(lambda: f(self.action()).action())

    def then(self, x: Io[_B]) -> Io[_B]:
        return self.and_then(lambda _: x)


def put_str(s: str) -> Io[None]:
    return Io(lambda: print(s, end=""))


def put_strln(s: str) -> Io[None]:
    return Io(lambda: print(s))


get_str = Io(input)


# Additional functions


def uncons(xs: Iterable[_A]) -> Maybe[Tuple[_A, Iterable[_A]]]:
    if null(xs):
        return Nothing()
    else:
        return Just((head(xs), tail(xs)))


def _test_uncons():
    assert uncons([]) == Nothing()
    assert uncons([1]) == Just((1, []))
    assert uncons([1, 2]) == Just((1, [2]))
    assert uncons({}) == Nothing()
    assert uncons({1: 2}) == Just((1, []))
    assert uncons({1: 2, 3: 4}) == Just((1, [3]))
    assert uncons("") == Nothing()
    assert uncons("a") == Just(("a", []))
    assert uncons("ab") == Just(("a", ["b"]))
    assert uncons("abc") == Just(("a", ["b", "c"]))
    assert uncons([""]) == Just(("", []))
    assert uncons(["a"]) == Just(("a", []))
    assert uncons(["a", "b"]) == Just(("a", ["b"]))
    assert uncons(["a", "b", "c"]) == Just(("a", ["b", "c"]))


def filter_map(f: Callable[[_A], Maybe[_B]], xs: Iterable[_A]) -> Iterable[_B]:
    return Seq(lambda: (y.unwrap() for x in xs if (y := f(x))))


def _test_filter_map():
    assert filter_map(lambda x: Just(x + 1), []) == []
    assert filter_map(lambda x: Just(x + 1), [1]) == [2]
    assert filter_map(lambda x: Just(x + 1), [1, 2]) == [2, 3]
    assert filter_map(lambda x: Nothing(), [1, 2]) == []


def partition(
    f: Callable[[_A], bool], xs: Iterable[_A]
) -> Tuple[Iterable[_A], Iterable[_A]]:
    # return filter(f, xs), filter(lambda x: not f(x), xs)
    return filter(f, xs), Seq(lambda: itertools.filterfalse(f, xs))


def _test_partition():
    assert partition(lambda x: x < 3, []) == ([], [])
    assert partition(lambda x: x < 3, [1]) == ([1], [])
    assert partition(lambda x: x < 3, [1, 2]) == ([1, 2], [])
    assert partition(lambda x: x < 3, [1, 2, 3]) == ([1, 2], [3])


def chunks_of(n: int, xs: Iterable[_A]) -> Iterable[Iterable[_A]]:
    def _chunk():
        it = iter(xs)
        while True:
            chunk = list(itertools.islice(it, n))
            if not chunk:
                break
            yield chunk

    return Seq(_chunk)


def _test_chunks_of():
    assert chunks_of(1, []) == []
    assert chunks_of(1, [1]) == [[1]]
    assert chunks_of(1, [1, 2]) == [[1], [2]]
    assert chunks_of(2, [1, 2, 3]) == [[1, 2], [3]]
    assert chunks_of(2, [1, 2, 3, 4]) == [[1, 2], [3, 4]]


def group(xs: Iterable[_A]) -> Iterable[Iterable[_A]]:
    def _group():
        it = iter(xs)
        try:
            prev = next(it)
            acc = [prev]
            for curr in it:
                if curr == prev:
                    acc.append(curr)
                else:
                    yield acc
                    acc = [curr]
                    prev = curr
            yield acc
        except StopIteration:
            return

    return Seq(_group)


def _test_group():
    assert group([]) == []
    assert group([1]) == [[1]]
    assert group([1, 1]) == [[1, 1]]
    assert group([1, 2]) == [[1], [2]]
    assert group([1, 1, 2, 2]) == [[1, 1], [2, 2]]
    assert group([1, 1, 2, 2, 1]) == [[1, 1], [2, 2], [1]]


def group_by(f: Callable[[_A], _B], xs: Iterable[_A]) -> Iterable[Iterable[_A]]:
    def _group_by():
        it = iter(xs)
        try:
            prev = next(it)
            prev_key = f(prev)
            acc = [prev]
            for curr in it:
                curr_key = f(curr)
                if curr_key == prev_key:
                    acc.append(curr)
                else:
                    yield acc
                    acc = [curr]
                    prev_key = curr_key
            yield acc
        except StopIteration:
            return

    return Seq(_group_by)


def _test_group_by():
    assert group_by(lambda x: x, []) == []
    assert group_by(lambda x: x, [1]) == [[1]]
    assert group_by(lambda x: x, [1, 1]) == [[1, 1]]
    assert group_by(lambda x: x, [1, 2]) == [[1], [2]]
    assert group_by(lambda x: x, [1, 1, 2, 2]) == [[1, 1], [2, 2]]
    assert group_by(lambda x: x, [1, 1, 2, 2, 1]) == [[1, 1], [2, 2], [1]]

    assert group_by(lambda x: x % 2, []) == []
    assert group_by(lambda x: x % 2, [1]) == [[1]]
    assert group_by(lambda x: x % 2, [1, 1]) == [[1, 1]]
    assert group_by(lambda x: x % 2, [1, 2]) == [[1], [2]]
    assert group_by(lambda x: x % 2, [1, 2, 3]) == [[1], [2], [3]]
    assert group_by(lambda x: x % 2, [1, 2, 2]) == [[1], [2, 2]]


def elem_index(x: _A, xs: Iterable[_A]) -> Maybe[int]:
    for i, y in enumerate(xs):
        if x == y:
            return Just(i)
    return Nothing()


def _test_elem_index():
    assert elem_index(1, []) == Nothing()
    assert elem_index(1, [1]) == Just(0)
    assert elem_index(1, [2]) == Nothing()
    assert elem_index(1, [2, 1]) == Just(1)


def find(f: Callable[[_A], bool], xs: Iterable[_A]) -> Maybe[_A]:
    for x in xs:
        if f(x):
            return Just(x)
    return Nothing()


def _test_find():
    assert find(lambda x: x == 1, []) == Nothing()
    assert find(lambda x: x == 1, [1]) == Just(1)
    assert find(lambda x: x == 1, [2]) == Nothing()
    assert find(lambda x: x == 1, [2, 1]) == Just(1)


def find_index(f: Callable[[_A], bool], xs: Iterable[_A]) -> Maybe[int]:
    for i, x in enumerate(xs):
        if f(x):
            return Just(i)
    return Nothing()


def _test_find_index():
    assert find_index(lambda x: x == 1, []) == Nothing()
    assert find_index(lambda x: x == 1, [1]) == Just(0)
    assert find_index(lambda x: x == 1, [2]) == Nothing()
    assert find_index(lambda x: x == 1, [2, 1]) == Just(1)


def intersperse(x: _A, xs: Iterable[_A]) -> Iterable[_A]:
    def _intersperse():
        it = iter(xs)
        try:
            yield next(it)
            for y in it:
                yield x
                yield y
        except StopIteration:
            return

    return Seq(_intersperse)


def _test_intersperse():
    assert intersperse(0, []) == []
    assert intersperse(0, [1]) == [1]
    assert intersperse(0, [1, 2]) == [1, 0, 2]
    assert intersperse(0, [1, 2, 3]) == [1, 0, 2, 0, 3]


def intercalate(sep: Iterable[_A], xss: Iterable[Iterable[_A]]) -> Iterable[_A]:
    def _intercalate():
        it = iter(xss)
        try:
            yield from next(it)
            for xs in it:
                yield from sep
                yield from xs
        except StopIteration:
            return

    return Seq(_intercalate)


def _test_intercalate():
    assert intercalate([], []) == []
    assert intercalate([], [[]]) == []
    assert intercalate([], [[1]]) == [1]
    assert intercalate([], [[1], [2]]) == [1, 2]
    assert intercalate([0], [[1], [2]]) == [1, 0, 2]
    assert intercalate([0, 0], [[1], [2]]) == [1, 0, 0, 2]


def transpose(xss: Iterable[Iterable[_A]]) -> Iterable[Iterable[_A]]:
    if not xss:
        return Seq(lambda: iter([]))
    else:
        return Seq(lambda: (list(row) for row in builtins.zip(*xss)))


def _test_transpose():
    assert transpose([]) == []
    assert transpose([[]]) == []
    assert transpose([[1]]) == [[1]]
    assert transpose([[1, 2]]) == [[1], [2]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]


def unique(seq: Iterable[_A]) -> Iterable[_A]:
    def _unique(acc: Iterable[_A], x: _A) -> Iterable[_A]:
        if x not in acc:
            return append(acc, [x])
        return acc

    return foldl(_unique, [], seq)


def _test_unique():
    assert unique([]) == []
    assert unique([1]) == [1]
    assert unique([1, 1]) == [1]
    assert unique([1, 2]) == [1, 2]
    assert unique([1, 2, 1]) == [1, 2]


_Ord_A = TypeVar("_Ord_A", bound=Ord | int)
_Ord_B = TypeVar("_Ord_B", bound=Ord | int)


def sort(seq: Iterable[_Ord_A]) -> Iterable[_Ord_A]:
    return Seq.from_iter(sorted(seq))


def _test_sort():
    assert sort([]) == []
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert sort([1, 2, 3]) == [1, 2, 3]


def sort_on(f: Callable[[_A], _Ord_B], seq: Iterable[_A]) -> Iterable[_A]:
    return Seq.from_iter(sorted(seq, key=f))


def _test_sort_on():
    assert sort_on(lambda x: x, []) == []
    assert sort_on(lambda x: x, [3, 2, 1]) == [1, 2, 3]
    assert sort_on(lambda x: x, [3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert sort_on(lambda x: x, [1, 2, 3]) == [1, 2, 3]
    assert sort_on(lambda x: -x, [1, 2, 3]) == [3, 2, 1]
    assert sort_on(lambda x: -x, [3, 2, 1, 1, 2, 3]) == [3, 3, 2, 2, 1, 1]


def is_prefix_of(xs: Iterable[_A], ys: Iterable[_A]) -> bool:
    if length(xs) > length(ys):
        return False
    else:
        return all(x == y for x, y in builtins.zip(xs, ys))


def _test_is_prefix_of():
    assert is_prefix_of([], [])
    assert is_prefix_of([], [1])
    assert is_prefix_of([1], [1])
    assert is_prefix_of([1, 2], [1, 2])
    assert is_prefix_of([1, 2], [1, 2, 3])
    assert not is_prefix_of([1, 2], [1])
    assert not is_prefix_of([1, 2], [1, 3])
    assert not is_prefix_of([1, 2], [1, 3, 4])


def is_suffix_of(xs: Iterable[_A], ys: Iterable[_A]) -> bool:
    if not xs:
        return True
    elif length(xs) > length(ys):
        return False
    else:
        xs_list = list(xs)
        ys_list = list(ys)
        return xs_list == ys_list[-len(xs_list) :]


def _test_is_suffix_of():
    assert is_suffix_of([], [])
    assert is_suffix_of([], [1])
    assert is_suffix_of([1], [1])
    assert is_suffix_of([1, 2], [1, 2])
    assert is_suffix_of([1, 2], [0, 1, 2])
    assert not is_suffix_of([1, 2], [1])
    assert not is_suffix_of([1, 2], [3, 1])
    assert not is_suffix_of([1, 2], [4, 3, 1])


# Other


# ! Side-effect
def for_each(f: Callable[[_A], None], xs: Iterable[_A]) -> None:
    for x in xs:
        f(x)


class ToBool(Protocol):
    def __bool__(self) -> bool: ...


def if_else(cond: ToBool, t: _A, f: _A) -> _A:
    return t if cond else f


def body(*exps):
    return [exp for exp in exps][-1]
