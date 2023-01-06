import os
import pytest
from gincolli.infra.dumps_infra import read_dump
import gincolli.app as app
from random import sample

@pytest.fixture(scope="module")
def setup():

    

    message = "the darkness that you fear"

    text_list = [*message]

    shared_size = int(len(text_list) / 2)

    package = sample([(0, text_list[0:shared_size]),
                    (1, text_list[shared_size:])], 2)

    yield package, message

    try:
        for file in ["message_temp_a", "message_temp_b"]:
            os.remove(os.path.join('data', file))

    except FileNotFoundError as e:

        print(e)


# @pytest.mark.skip(reason="")
@pytest.mark.asyncio
async def test_asyncio_spin(setup) -> None:

    _, message = setup

    spin, particle = app.get_sping()

    packages = spin(particle(message))

    print()

    app.log("Start")

    await app.mock_share(position=0, delay=1.2)(packages[0])

    await app.mock_share(position=1, delay=2.5)(packages[1])

    app.log("End")

    compose = await app.compose_message(1.8)

    assert message.__eq__(compose)

def test_particle(setup) -> None:

    _, message = setup

    text_list = [*message]

    shared_size = int(len(text_list) / 2)

    package = {0: text_list[0:shared_size], 1: text_list[shared_size:]}

    compose = ''.join(package.get(0, "")) + ''.join(package.get(1, ""))

    assert message == compose

@pytest.mark.asyncio
async def test_process_a(setup) -> None:

    packages, _ = setup

    await app.process_a(packages[0], 1.3)

    dump = await read_dump("message_temp_a")

    assert packages[0][0] == dump[0]

@pytest.mark.asyncio
async def test_process_b(setup) -> None:

    packages, _ = setup

    await app.process_b(packages[1], 1.3)

    dump = await read_dump("message_temp_b")

    assert packages[1][0] == dump[0]

@pytest.mark.asyncio
async def test_compose_message(setup) -> None:

    _, message = setup

    compose = await app.compose_message(1.8)

    assert compose.__eq__(message)
