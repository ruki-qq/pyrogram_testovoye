import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from pyrogram import Client

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


class UserBotConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="api_")

    id: str
    hash: str


class UserBot(Client):
    def __init__(self):
        self.config = UserBotConfig()

        super().__init__(
            "userbot",
            api_id=self.config.id,
            api_hash=self.config.hash,
        )

    async def start(self):
        await super().start()

        me = await self.get_me()
        logging.info(f"Started userbot on user: {me.username}")

    async def stop(self, *args):
        me = await self.get_me()
        await super().stop()

        logging.info(f"Userbot on user {me.username} stopped.")
