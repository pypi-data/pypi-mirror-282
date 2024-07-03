from enum import Enum


class StatusCycle(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
