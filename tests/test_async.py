import os
import pytest
from gincolli.infra.dumps_infra import read_dump
import gincolli.app as app
from random import sample

@pytest.fixture(scope="module")
def setup():

    message:str = "the darkness that you fear"
    
    chunks = app.get_chunks(message, 3)

    package = sample(chunks, len(chunks))

    yield package, message

    try:
        for file in ["message_temp_a", "message_temp_b"]:
            os.remove(os.path.join('data', file))

    except FileNotFoundError as e:

        print(e)



@pytest.mark.asyncio
async def test_asyncio_spin(setup) -> None:

    packages, message = setup
    
    key: int = 0

    particles_x = []
    particles_y = []

    for i, p in enumerate(packages, 1):

        # percent = int(i / len(packages) * 100)

        # app.log(f"processed:{percent}%"
        #         if percent == 100 else f"processing:{percent}%")

        if key == 0:
            particles_x.append(p)

            key = 1
            continue

        particles_y.append(p)
        key = 0

    print()
    await app.mock_share(position=0, delay=.1)(package=particles_x)
    await app.mock_share(position=1, delay=.07)(package=particles_y)

    compose = await app.compose_message(.2)
    
    print(f"message compose:{compose}")

    assert message.__eq__(compose)

@pytest.mark.skip(reason="")
def test_particle(setup) -> None:

    _, message = setup

    text_list = [*message]

    shared_size = int(len(text_list) / 2)

    package = {0: text_list[0:shared_size], 1: text_list[shared_size:]}

    compose = ''.join(package.get(0, "")) + ''.join(package.get(1, ""))

    assert message == compose

@pytest.mark.skip(reason="")
@pytest.mark.asyncio
async def test_process_a(setup) -> None:

    packages, _ = setup

    file_dumb = "message_temp_a"

    await app.process(file_dumb, packages[0], 1.3)

    dump = await read_dump(file_dumb)

    assert packages[0][0] == dump[0]

@pytest.mark.skip(reason="")
@pytest.mark.asyncio
async def test_process_b(setup) -> None:

    packages, _ = setup

    file_dumb = "message_temp_b"

    await app.process(file_dumb, packages[1], 1.3)

    dump = await read_dump(file_dumb)

    assert packages[1][0] == dump[0]

@pytest.mark.skip(reason="")
@pytest.mark.asyncio
async def test_compose_message(setup) -> None:

    _, message = setup

    compose = await app.compose_message(1.8)

    assert compose.__eq__(message)
