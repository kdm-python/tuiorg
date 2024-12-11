from pydantic import field_validator, ValidationError
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
from enum import Enum


class ImportanceLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=50)
    importance: ImportanceLevel = Field(default=ImportanceLevel.MEDIUM)
    complete: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=50)
    date_time: datetime
    location: str

    @field_validator("date_time", mode="before")
    def validate_date_time(cls, value: datetime):
        if value < datetime.now():
            raise ValueError(
                "Date and time cannot be in the past unless you've developed time travel."
            )
        return value


class Headache(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    pain: int = Field(gt=0, lt=11)
    limit: bool
