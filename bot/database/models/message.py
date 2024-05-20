from datetime import datetime

from sqlalchemy import func, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from database.enums import MsgNum, Status


class Message(Base):
    title: Mapped[str] = mapped_column(String(120))
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    num: Mapped[MsgNum] = mapped_column()

    def __str__(self):
        return f"'{self.__class__.__name__}; id={self.id}; title={self.title}'"

    def __repr__(self):
        return str(self)
