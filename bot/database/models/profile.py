from datetime import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from database.enums import MsgNum, Status


class Profile(Base):
    chat_id: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    status: Mapped[Status] = mapped_column(
        default=Status.ALIVE,
        server_default="ALIVE",
    )
    status_updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    msg_num_to_recieve: Mapped[MsgNum | None] = mapped_column(
        default=MsgNum.FIRST,
        server_default="FIRST",
    )

    def __str__(self):
        return f"{self.__class__.__name__}, id={self.id}, status={self.status}"

    def __repr__(self):
        return str(self)
