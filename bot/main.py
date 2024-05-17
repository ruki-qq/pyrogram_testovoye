import asyncio
import os

import uvloop

from userbot import UserBot

api_id: str = os.getenv("API_ID")
api_hash: str = os.getenv("API_HASH")


async def main():
    app = UserBot()

    async with app:
        print(await app.get_me())


uvloop.install()
asyncio.run(main())
