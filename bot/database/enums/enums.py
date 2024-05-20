from enum import Enum


class MsgNum(Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"


class Status(Enum):
    ALIVE = "alive"
    DEAD = "dead"
    FINISHED = "finished"
