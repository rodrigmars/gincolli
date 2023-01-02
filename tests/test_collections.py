from pytest import fixture
from collections import Counter 


@fixture
def setup():
    return [5, 3, 5, 2, 1, 6, 6, 4]

def test_find_duplicates(setup):
    assert Counter(setup).get(5) == 2
