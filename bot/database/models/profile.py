from datetime import datetime
from enum import Enum
from typing import Final

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Status(Enum):
    ALIVE: Final[str] = "alive"
    DEAD: Final[str] = "dead"
    FINISHED: Final[str] = "finished"


class Profile(Base):
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    status: Mapped[Status]
    status_updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )

    def __str__(self):
        return f"{self.__class__.__name__}, id={self.id}, status={self.status}"

    def __repr__(self):
        return str(self)
