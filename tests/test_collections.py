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

def test_spin(setup: list[int]) -> None:

    # assert eletron(setup)
    spin_send("the darkness that you fear")

    pass

def spin_send(message:str):

    def particle(text):

        text_list = list(text)

        total = int(len(text_list) / 2)

        package = [{0: text_list[0:total]},
                   {1: text_list[-total:]}]

        return package

    def spin(package: list[dict]):
        return sample(package, len(package))

    def tigger_spin(package) ->None:
        print("package:>", package)

    print()

    while True:
        
        packages = spin(particle(message))

        print("-----------------------")
        tigger_spin(packages[0])
        
        sleep(1.5)
        
        tigger_spin(packages[1])


    # str_1_encoded = data.encode(encoding='UTF-8')
    
    # print("str_1_encoded: ", str_1_encoded.split(b' '))


