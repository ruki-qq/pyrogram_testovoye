import logging
from datetime import datetime, timedelta

from pyrogram import Client, errors
from sqlalchemy.ext.asyncio import AsyncSession

from database.enums import MsgNum, Status
from database.messages import get_message_by_enum
from database.profiles import get_alive_profiles, update_profile
from database.schemas import ProfileUpdate

intervals: dict[MsgNum, timedelta] = {
    MsgNum.FIRST: timedelta(minutes=6),
    MsgNum.SECOND: timedelta(minutes=39),
    MsgNum.THIRD: timedelta(days=1, hours=2),
}

logger = logging.getLogger("userbot")


async def check_profiles_and_send_msg(app: Client, session: AsyncSession) -> None:
    alive_profiles = await get_alive_profiles(session)
    for profile in alive_profiles:
        curr_num = profile.msg_num_to_recieve
        if datetime.now() - profile.status_updated_at > intervals[curr_num]:
            logger.info(f"Sending {curr_num} message to {profile.chat_id}...")
            msg = await get_message_by_enum(curr_num)
            try:
                await app.send_message(profile.chat_id, msg.text)
            except (errors.UserIsBlocked, errors.UserDeactivated) as e:
                update = ProfileUpdate(
                    msg_num_to_recieve=None,
                    status=Status.DEAD,
                    status_updated_at=datetime.now(),
                )
                await update_profile(profile.id, update, session)
                return
            if curr_num == MsgNum.THIRD:
                logger.info(f"Sent all messages to {profile.chat_id}.")
                update = ProfileUpdate(
                    msg_num_to_recieve=None,
                    status=Status.FINISHED,
                    status_updated_at=datetime.now(),
                )
            else:
                new_msg_num = (
                    MsgNum.THIRD if curr_num == MsgNum.SECOND else MsgNum.SECOND
                )
                logger.info(
                    f"Setting up {new_msg_num} message to send to {profile.chat_id}."
                )
                update = ProfileUpdate(
                    status_updated_at=datetime.now(),
                    msg_num_to_recieve=new_msg_num,
                )
            await update_profile(profile.id, update, session)
