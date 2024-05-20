import asyncio
import json

from database.messages import bulk_add_messages
from database.schemas import MessageCreate


async def main():
    messages = [MessageCreate(**msg) for msg in json.load(open("data/messages.json"))]
    loaded_msgs = await bulk_add_messages(messages)
    print(loaded_msgs)


if __name__ == "__main__":
    asyncio.run(main())
