import os
import aiofiles
import pickle
from typing import Tuple


async def create_dump(file: str, message: Tuple[int, str]) -> None:

    async with aiofiles.open(os.path.join('data', file), mode='ab') as file_pk:

        pickled_message = pickle.dumps(message)

        await file_pk.write(pickled_message)


async def read_dump(file: str) -> Tuple[int, str]:

    async with aiofiles.open(os.path.join('data', file), mode='rb') as file_pk:

        contents = await file_pk.read()

        return pickle.loads(contents)
