import asyncio
import json
import logging.config
import logging.handlers
import pathlib

import uvloop
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from handlers import msg_handler, trigger_handler
from userbot import UserBot, UserBotConfig
from utils import check_profiles_and_send_msg


logger = logging.getLogger("userbot")


def setup_logging():
    config_file = pathlib.Path("logs/logging_config.json")
    with open(config_file, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)


bot_config = UserBotConfig()


async def main():
    setup_logging()
    app = UserBot(bot_config)
    app.add_handler(msg_handler)
    app.add_handler(trigger_handler)
    logger.info("Starting bot...")
    async with app:
        while True:
            session: AsyncSession = db_helper.get_scoped_session()
            await check_profiles_and_send_msg(app, session)
            await session.close()
            await asyncio.sleep(10)


if __name__ == "__main__":
    uvloop.install()
    logger.info("Starting main() asynchronously...")
    asyncio.run(main())
