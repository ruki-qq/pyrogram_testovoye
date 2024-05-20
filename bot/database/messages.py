import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from database.enums import MsgNum
from database.models import Message
from database.schemas import MessageCreate

logger = logging.getLogger("userbot")


async def bulk_add_messages(
    msgs: list[MessageCreate], session: AsyncSession = db_helper.get_scoped_session()
) -> list[Message]:
    new_messages: list[Message] = []
    for msg in msgs:
        new_message = Message(**msg.model_dump())
        new_messages.append(new_message)
    logger.debug("Adding new messages to db...")
    session.add_all(new_messages)
    await session.commit()
    return new_messages


async def add_message(
    message_in: MessageCreate, session: AsyncSession = db_helper.get_scoped_session()
):
    new_message = Message(**message_in.model_dump())
    logger.debug(f"Adding new message {new_message} to db...")
    session.add(new_message)
    await session.commit()
    return new_message


async def get_message_by_id(
    message_id: int, session: AsyncSession = db_helper.get_scoped_session()
) -> Message | None:
    logger.debug(f"Searching for message with id: {message_id}...")
    return await session.get(Message, message_id)


async def get_message_by_enum(
    message_num: MsgNum, session: AsyncSession = db_helper.get_scoped_session()
) -> Message | None:
    logger.debug(f"Searching for message with num: {message_num}...")
    return await session.scalar(select(Message).filter_by(num=message_num))
