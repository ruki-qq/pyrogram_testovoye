import asyncio
import os

import uvloop
from pyrogram import Client

api_id: str = os.getenv("API_ID")
api_hash: str = os.getenv("API_HASH")


async def main():
    app = Client(
        "my_account",
        api_id=api_id,
        api_hash=api_hash,
    )

    async with app:
        print(await app.get_me())


uvloop.install()
asyncio.run(main())
