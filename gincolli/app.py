from os import system, name
import asyncio
from random import sample
from typing import Dict, List, Tuple, Callable

from infra.dumps_infra import create_dump, read_dump

Package = Dict[int, list[str]]
Spin = List[Tuple[int, List[str]]]
Message = Tuple[int, List[str]]
Cannon = Callable[[str, float], Callable]


class Colors:
    CYELLOW = '\33[33m'
    RESET = '\033[0m'
    CGREEN = '\33[32m'
    CRED = '\33[31m'


def clear():
    system('clear' if name.__eq__('posix') else 'cls')


def log(log: str):
    print(f"{Colors.CYELLOW}{log}")


def log_share(log: str):
    print(f"{Colors.CGREEN}entanglement{Colors.RESET} - {log}")


def log_compose(log: str):
    print(f"{Colors.CGREEN}compose{Colors.RESET} - message:{Colors.CYELLOW}{log}")


def get_chunks(data: str, num: int) -> list[tuple[int, str]]:
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


async def process(file: str, message: Tuple[int, str], delay: float) -> None:

    await asyncio.sleep(delay)

    await create_dump(file, message)


def mock_share(position: int, delay: float):

    async def send(package):

        if 0 == position:
            log_share(package)
            await process("message_temp_0", package, delay)

        elif 1 == position:
            log_share(package)
            await process("message_temp_1", package, delay)

    return send


async def compose_message(delay: float) -> str:

    await asyncio.sleep(delay)

    dump_x = await read_dump("message_temp_0")

    dump_y = await read_dump("message_temp_1")

    particles_list = sorted(dump_x + dump_y)

    return ''.join(map(lambda m: m[1], particles_list))


async def main(message: str):

    clear()

    automatic_message = "Newton's third law - the only way humans \
have ever figured out of getting somewhere is to leave something behind."

    message = message if len(message) >= 1 else automatic_message

    chunks = get_chunks(message, 3)

    packages = sample(chunks, len(chunks))

    key: int = 0

    particles_x = []
    particles_y = []

    for _, p in enumerate(packages, 1):

        if key == 0:
            particles_x.append(p)

            key = 1
            continue

        particles_y.append(p)
        key = 0

    await mock_share(position=0, delay=.1)(package=particles_x)
    await mock_share(position=1, delay=.07)(package=particles_y)

    compose = await compose_message(.2)

    print(f"\nmessage compose:> {compose}\n")


if __name__ == '__main__':

    clear()

    script = "\nrunning the Gincolli console...\n\nEnter a message for transmission \
or allow the system to automatically send\n_: "

    asyncio.run(
        main(input(script).strip()))
