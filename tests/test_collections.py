from pytest import fixture
from collections import Counter


@fixture
def setup() -> list[int]:

    return [5, 3, 5, 2, 1, 6, 6, 4]


def test_find_duplicates(setup: list[int]) -> None:

    assert Counter(setup).get(5) == 2


def test_add(setup: list[int]) -> None:

    assert Counter(setup).get(5, 0).__add__(2) == 4


def test_median(setup: list[int]) -> None:

    median = sum(setup) / setup.__len__()

    assert median.__eq__(4)
