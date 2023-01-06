import pytest
import asyncio
from random import sample
from typing import Dict, List, Tuple, Callable
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


def get_sping():

    def particle(text: str) -> Package:

        text_list = [*text]

        shared_size = int(len(text_list) / 2)

        return {0: text_list[0:shared_size], 1: text_list[shared_size:]}

    def spin(package: Package) -> Spin:
        return sample([*package.items()], len(package))

    return spin, particle

async def process_a(message, delay: float) -> None:

    await asyncio.sleep(delay)

    log_share(f"process a:{message}")

    await create_dump("message_temp_a", message)

async def process_b(message, delay: float):

    await asyncio.sleep(delay)

    log_share(f"process b:{message}")

    await create_dump("message_temp_b", message)

def mock_share(position: int, delay: float):

    async def send(message):

        if position == 0:
            await process_a(message, delay)

        elif position == 1:
            await process_b(message, delay)

    return send

async def compose_message(delay: float) -> str:

    await asyncio.sleep(delay)

    def compose(vetor: list[str]) -> str:
        return ''.join(vetor)

    dump_a = await read_dump("message_temp_a")

    dump_b = await read_dump("message_temp_b")

    if 0 == dump_a[0]:
        message = compose(dump_a[1]) + compose(dump_b[1])
    else:
        message = compose(dump_b[1]) + compose(dump_a[1])

    log_compose(message)

    return message




def main():
    pass


if __name__ == '__main__':

    main()
