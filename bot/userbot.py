import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from pyrogram import Client, errors
from pyrogram.enums import UserStatus

logger = logging.getLogger("userbot")


class UserBotConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="api_")

    id: str
    hash: str


class UserBot(Client):
    def __init__(self, config: UserBotConfig):
        self.config = config

        super().__init__(
            "userbot",
            api_id=self.config.id,
            api_hash=self.config.hash,
        )

    async def send_message(self, chat_id: int, text: str, *args):
        user = await self.get_users(chat_id)
        if user.is_deleted:
            logger.warning(f"User with id: {chat_id} is deleted.")
            raise errors.UserDeactivated
        if user.status == UserStatus.LONG_AGO:
            logger.warning(f"User with id: {chat_id} blocked you.")
            raise errors.UserIsBlocked
        await super().send_message(chat_id, text)
