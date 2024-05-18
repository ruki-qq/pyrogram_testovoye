from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import URLType

from .base import Base


class Message(Base):
    text: Mapped[str] = mapped_column(String(4096))
    media_url: Mapped[URLType | None] = mapped_column(URLType)

    def __str__(self):
        return f"{self.__class__.__name__}, id={self.id}, text={self.text[:30]}"

    def __repr__(self):
        return str(self)
