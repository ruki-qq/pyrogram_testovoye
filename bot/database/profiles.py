import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from database.enums import Status
from database.models import Profile
from database.schemas import ProfileCreate, ProfileUpdate

logger = logging.getLogger("userbot")


async def add_profile(
    profile_in: ProfileCreate, session: AsyncSession = db_helper.get_scoped_session()
) -> Profile:
    new_profile = Profile(**profile_in.model_dump())
    logger.debug(f"Adding new profile {new_profile.chat_id} to session...")
    session.add(new_profile)
    await session.commit()
    return new_profile


async def get_profile(
    profile_id: int, session: AsyncSession = db_helper.get_scoped_session()
) -> Profile | None:
    logger.debug(f"Searching profile with id: {profile_id}...")
    return await session.get(Profile, profile_id)


async def get_profile_by_chat_id(
    chat_id: int, session: AsyncSession = db_helper.get_scoped_session()
) -> Profile | None:
    logger.debug(f"Searching profile with chat_id: {chat_id}...")
    return await session.scalar(select(Profile).filter_by(chat_id=chat_id))


async def get_alive_profiles(
    session: AsyncSession = db_helper.get_scoped_session(),
) -> list[Profile]:
    logger.debug(f"Getting list of {Status.ALIVE} profiles...")
    profiles = await session.scalars(select(Profile).filter_by(status=Status.ALIVE))
    return list(profiles)


async def update_profile(
    profile_id: int,
    profile_in: ProfileUpdate,
    session: AsyncSession = db_helper.get_scoped_session(),
) -> Profile:
    profile = await get_profile(profile_id, session)
    logger.debug(f"Updating profile {profile_id}...")
    for name, val in profile_in.model_dump(exclude_unset=True).items():
        setattr(profile, name, val)
    await session.commit()
    return profile
