import json
import logging
import re
from datetime import datetime

from pyrogram import filters
from pyrogram.handlers import MessageHandler

from database import db_helper, profiles
from database.enums import MsgNum, Status
from database.schemas import ProfileCreate, ProfileUpdate

logger = logging.getLogger("userbot")
triggers = json.load(open("data/triggers.json"))


async def handle_triggers(client, message):
    profile_id = message.chat.id
    existing_profile = await profiles.get_profile_by_chat_id(profile_id)
    if existing_profile:
        if message.text.lower() in triggers["cancel_triggers"]:
            if existing_profile.msg_num_to_recieve == MsgNum.SECOND:
                logger.info(
                    f"Cancelling {MsgNum.SECOND} message sending for user {message.chat.id}..."
                )
                update = ProfileUpdate(
                    status_updated_at=datetime.now(), msg_num_to_recieve=MsgNum.THIRD
                )
                await profiles.update_profile(existing_profile.id, update)
        else:
            for trigger in triggers["stop_triggers"]:
                if re.compile(r"\b({0})\b".format(trigger), flags=re.IGNORECASE).search(
                    message.text.lower()
                ):
                    logger.info(
                        f"Cancelling all messages sending for user {message.chat.id}..."
                    )
                    update = ProfileUpdate(
                        status=Status.FINISHED,
                        status_updated_at=datetime.now(),
                        msg_num_to_recieve=None,
                    )
                    await profiles.update_profile(existing_profile.id, update)


trigger_handler = MessageHandler(handle_triggers, filters.private & filters.me)
