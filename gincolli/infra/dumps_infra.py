import os
import aiofiles
import pickle


async def create_dump(file: str, message):

    async with aiofiles.open(os.path.join('data', file), 'wb') as file_pk:

        pickled_message = pickle.dumps(message)

        await file_pk.write(pickled_message)


async def read_dump(file: str):

    async with aiofiles.open(os.path.join('data', file), 'rb') as file_pk:

        contents = await file_pk.read()

        return pickle.loads(contents)
