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


def eletron(lista: list[int]) -> list[int]:

    def add() -> list[int]:
        return lista.__iadd__([8])

    def remove(lista_a: list[int]) -> None:
        lista_a.__delitem__(8)

    lista_copia = add()

    remove(lista_copia)

    return lista_copia
