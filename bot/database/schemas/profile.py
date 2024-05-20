from datetime import datetime

from pydantic import BaseModel, Field

from database.enums import MsgNum, Status


class ProfileBase(BaseModel):
    chat_id: int
    status: Status = Field(default=Status.ALIVE)

    def __str__(self):
        return (
            f"'{self.__class__.__name__}; chat_id={self.chat_id}; status={self.status}'"
        )

    def __repr__(self):
        return str(self)


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    chat_id: int | None = None
    status: Status | None = None
    status_updated_at: datetime | None = None
    msg_num_to_recieve: MsgNum | None = None


class Profile(ProfileBase):
    id: int
