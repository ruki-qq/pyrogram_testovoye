from pydantic import BaseModel


class MessageBase(BaseModel):
    title: str | None = None
    text: str
    num: str | None = None

    def __str__(self):
        return f"'{self.__class__.__name__}; title={self.title}; text={self.text[:30]}'"

    def __repr__(self):
        return str(self)


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    pass


class Message(MessageBase):
    pass
