import builtins
from typing import (
    Any,
    Callable,
    Coroutine,
    Iterable,
    Iterator,
    List,
    Optional,
    TypeVar,
    cast,
)

from streamable.wrappers import (
    AsyncConcurrentMappingIterable,
    CatchingIterator,
    ConcurrentFlatteningIterable,
    ConcurrentMappingIterable,
    FlatteningIterator,
    GroupingIterator,
    ObservingIterator,
    RaisingIterator,
    SlowingIterator,
    TruncatingOnCountIterator,
    TruncatingOnPredicateIterator,
)

T = TypeVar("T")
U = TypeVar("U")

from streamable import util


class WrappedStopIteration(Exception):
    pass


def catch(
    iterator: Iterator[T],
    when: Callable[[Exception], Any] = bool,
    raise_after_exhaustion: bool = False,
) -> Iterator[T]:
    when = util.reraise_as(when, source=StopIteration, target=WrappedStopIteration)
    return CatchingIterator(
        iterator,
        when,
        raise_after_exhaustion=raise_after_exhaustion,
    )


def flatten(iterator: Iterator[Iterable[T]], concurrency: int = 1) -> Iterator[T]:
    util.validate_concurrency(concurrency)
    if concurrency == 1:
        return FlatteningIterator(iterator)
    else:
        return RaisingIterator(
            iter(
                ConcurrentFlatteningIterable(
                    iterator,
                    concurrency=concurrency,
                    buffer_size=concurrency,
                )
            )
        )


def group(
    iterator: Iterator[T],
    size: Optional[int] = None,
    seconds: float = float("inf"),
    by: Optional[Callable[[T], Any]] = None,
) -> Iterator[List[T]]:
    util.validate_group_size(size)
    util.validate_group_seconds(seconds)
    if by is not None:
        by = util.reraise_as(by, StopIteration, WrappedStopIteration)
    if size is None:
        size = cast(int, float("inf"))
    return GroupingIterator(iterator, size, seconds, by)


def map(
    transformation: Callable[[T], U], iterator: Iterator[T], concurrency: int = 1
) -> Iterator[U]:
    util.validate_concurrency(concurrency)
    transformation = util.reraise_as(
        transformation, StopIteration, WrappedStopIteration
    )
    if concurrency == 1:
        return builtins.map(transformation, iterator)
    else:
        return RaisingIterator(
            iter(
                ConcurrentMappingIterable(
                    iterator,
                    transformation,
                    concurrency=concurrency,
                    buffer_size=concurrency,
                )
            )
        )


def amap(
    transformation: Callable[[T], Coroutine[Any, Any, U]],
    iterator: Iterator[T],
    concurrency: int = 1,
) -> Iterator[U]:
    util.validate_concurrency(concurrency)
    return RaisingIterator(
        iter(
            AsyncConcurrentMappingIterable(
                iterator,
                util.reraise_as(transformation, StopIteration, WrappedStopIteration),
                buffer_size=concurrency,
            )
        )
    )


def observe(iterator: Iterator[T], what: str, colored: bool = False) -> Iterator[T]:
    return ObservingIterator(iterator, what, colored)


def slow(iterator: Iterator[T], frequency: float) -> Iterator[T]:
    util.validate_slow_frequency(frequency)
    return SlowingIterator(iterator, frequency)


def truncate(
    iterator: Iterator[T],
    count: Optional[int] = None,
    when: Optional[Callable[[T], Any]] = None,
) -> Iterator[T]:
    util.validate_truncate_args(count, when)
    if count is not None:
        iterator = TruncatingOnCountIterator(iterator, count)
    if when is not None:
        iterator = TruncatingOnPredicateIterator(iterator, when)
    return iterator
