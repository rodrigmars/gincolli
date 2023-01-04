from pytest import fixture
from collections import Counter
from random import shuffle,  choice, sample
from time import sleep
 
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

def test_spin() -> None:

    print()

    send_message("the darkness that you fear")

from random import sample
from time import sleep
from typing import Dict, List, Tuple

Package = Dict[int, list[str]]
Spin = List[Tuple[int, List[str]]]

def send_message(message: str):

    def particle(text: str) -> Package:

        text_list = [*text]

        shared_size = int(len(text_list) / 2)

        return {0: text_list[0:shared_size], 1: text_list[-shared_size:]}

    def spin(package: Package) -> Spin:
        return sample([*package.items()], len(package))

    def triger(package:  Tuple[int, List[str]]) -> None:
        print("package:>", package)

    requests:int = 0

    while requests < 10:
        
        packages = spin(particle(message))

        print("-----------------------")
        triger(packages[0])
        
        sleep(1.5)
        
        triger(packages[1])

        requests += 1


    # str_1_encoded = data.encode(encoding='UTF-8')
    
    # print("str_1_encoded: ", str_1_encoded.split(b' '))


