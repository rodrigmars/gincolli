import pytest
import asyncio
from random import sample
from typing import Dict, List, Tuple, Callable
from gincolli.infra.dumps_infra import create_dump, read_dump

Package = Dict[int, list[str]]
Spin = List[Tuple[int, List[str]]]
Message = Tuple[int, List[str]]
Cannon=Callable[[str, float], Callable]
class Colors:
    CYELLOW = '\33[33m'
    RESET = '\033[0m'
    CGREEN = '\33[32m'
    CRED = '\33[31m'

@pytest.mark.asyncio
async def test_asyncio_spin() -> None:

    print()

    await send_message("the darkness that you fear")

async def send_message(message: str):

    def log_terminal(log: str):
        print(f"{Colors.CYELLOW}{log}")

    def particle(text: str) -> Package:

        text_list = [*text]

        shared_size = int(len(text_list) / 2)

        return {0: text_list[0:shared_size], 1: text_list[-shared_size:]}

    def spin(package: Package) -> Spin:
        return sample([*package.items()], len(package))

    async def trigger_mock(epoc: int) -> None:

        if epoc > 3: return

        epoc += 1

        packages = spin(particle(message))

        log_terminal("Start")

        await cannon(">>a", 1.2, True)(packages[0])

        await cannon(">>b", 2.5, True)(packages[1])

        log_terminal("fin °°°")
        
        await cannon(">>a", 1.2, False)(packages[0])
        
        await trigger_mock(epoc)

    def cannon(service: str, delay: float, cache: bool):
        
        async def send(message):

            if service == ">>a":
                await process_a(message, delay, cache)

            elif service == ">>b":
                await process_b(message, delay, cache)

        return send

    await trigger_mock(0)


async def process_b(message, delay: float, cache: bool) -> bool:
    
    await asyncio.sleep(delay)

    status: str = "interweaving" if cache else "handshake"

    if cache:

        print(f"{Colors.CGREEN}{status}{Colors.RESET} - process a:{message}")

        await create_dump("message_temp_b", message)

    else:
        def compose(vetor: list[str]) -> str:
            return ''.join(vetor)

        dump = await read_dump("message_temp_b")

        if 0 == message[0]:
            message = compose(message[1]) + compose(dump[1])
        else:
            message = compose(dump[1]) + compose(message[1])

        print(
            f"{Colors.CGREEN}{status}{Colors.RESET} - message:{Colors.CYELLOW}{message}")

    return True


async def process_a(message, delay: float, cache: bool) -> bool:
    
    await asyncio.sleep(delay)

    if cache:

        print(f"{Colors.CGREEN}interweaving{Colors.RESET} - process b:{message}")

        await create_dump("message_temp_a", message)

    else:

        message = await read_dump("message_temp_a")

        await process_b(message, 1.8, False)

    return True
