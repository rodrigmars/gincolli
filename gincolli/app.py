import asyncio
from random import sample
from typing import Any, Dict, List, Tuple, Callable

from gincolli.infra.dumps_infra import create_dump, read_dump

Package = Dict[int, list[str]]
Spin = List[Tuple[int, List[str]]]
Message = Tuple[int, List[str]]
Cannon = Callable[[str, float], Callable]


class Colors:
    CYELLOW = '\33[33m'
    RESET = '\033[0m'
    CGREEN = '\33[32m'
    CRED = '\33[31m'


def log(log: str):
    print(f"{Colors.CYELLOW}{log}")


def log_share(log: str):
    print(f"{Colors.CGREEN}entanglement{Colors.RESET} - {log}")



def log_compose(log: str):
    print(f"{Colors.CGREEN}compose{Colors.RESET} - message:{Colors.CYELLOW}{log}")


def get_chunks(data: Any, num: int) -> list[tuple[int, Any]]:
    return [(i, data[i*num:i*num+num])
            for i, _ in enumerate(data[::num])]


def get_sping():

    def particle(text: str) -> Package:

        text_list = [*text]

        shared_size = int(len(text_list) / 2)

        return {0: text_list[0:shared_size], 1: text_list[shared_size:]}

    def spin(package: Package) -> Spin:
        return sample([*package.items()], len(package))

    return spin, particle

async def process(file:str, message: Tuple[int, str], delay: float) -> None:

    await asyncio.sleep(delay)

    await create_dump(file, message)

def mock_share(position: int, delay: float):

    async def send(package):

        if position == 0:
            log_share(package)
            await process("message_temp_a", package, delay)

        elif position == 1:
            log_share(package)
            await process("message_temp_b", package, delay)

    return send

async def compose_message(delay: float) -> str:

    print()
    print()
    print("-----------------")

    await asyncio.sleep(delay)

    def compose(vetor: list[str]) -> str:
        return ''.join(vetor)

    dump_a = await read_dump("message_temp_a")

    dump_b = await read_dump("message_temp_b")

    print("dump_a:", dump_a)
    print("dump_b:", dump_b)

    # if 0 == dump_a[0]:
    #     message = compose(dump_a[1]) + compose(dump_b[1])
    # else:
    #     message = compose(dump_b[1]) + compose(dump_a[1])

    # log_compose(message)

    # return message

    return ""


def main():
    pass


if __name__ == '__main__':

    main()
