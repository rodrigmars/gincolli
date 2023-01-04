import os
import pytest
import asyncio
import pickle
from random import sample
from typing import Dict, List, Tuple, Callable

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

    def spin(
        package: Package) -> Spin: return sample([*package.items()], len(package))

    async def photon_trigger_mock(epoc: int) -> None:

        if epoc > 3: return

        epoc += 1

        packages = spin(particle(message))

        log_terminal("Start")

        await cannon(">>a", 1.2)(packages[0])

        await cannon("<<b", 2.2)(packages[1])

        log_terminal("fin °°°")

        await photon_trigger_mock(epoc)

    def cannon(service: str, delay: float):
        
        async def send(message):
            if ">>a" == service:
                await process_a(message, delay, False)

            elif "<<b" == service:
                await process_b(message, delay)

        return send

    await photon_trigger_mock(0)


async def process_a(message, delay:float, handshake:bool) -> bool:
    
    await asyncio.sleep(delay)

    status: str = "interweaving" if not handshake else "handshake"
    
    if not handshake:

        print(f"{Colors.CGREEN}{status}{Colors.RESET} - process a:{message}")
        
        with open(os.path.join('data', 'message_temp'), 'wb') as file_pk:
            pickle.dump(message, file_pk)

    else:
        def convert_message(lista):
            return ''.join(lista)

        with open(os.path.join('data', 'message_temp'), 'rb') as file_pk:

            dump = pickle.load(file_pk)

            if 0 == message[0]:
                message = convert_message(message[1]) + convert_message(dump[1])
            else:
                message = convert_message(dump[1]) + convert_message(message[1])

            print(f"{Colors.CGREEN}{status}{Colors.RESET} - message:{Colors.CYELLOW}{message}")

    return True

async def process_b(message, delay:float) -> bool:
    
    await asyncio.sleep(delay)
    
    print(f"{Colors.CGREEN}interweaving{Colors.RESET} - process b:{message}")
    
    await process_a(message, .8, True)

    return True
