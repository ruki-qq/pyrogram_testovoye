import logging

from pyrogram import filters
from pyrogram.handlers import MessageHandler

from database import profiles
from database.schemas import ProfileCreate

logger = logging.getLogger("userbot")


async def handle_msg(client, message):
    profile_id = message.chat.id
    existing_profile = await profiles.get_profile_by_chat_id(profile_id)
    if not existing_profile:
        profile_in = ProfileCreate(chat_id=message.chat.id)
        logger.info(f"Creating user with id: {message.chat.id} in db...")
        await profiles.add_profile(profile_in)


msg_handler = MessageHandler(handle_msg, filters.private & ~filters.bot & ~filters.me)
