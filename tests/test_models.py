from pydantic import ValidationError
import pytest
from tuiorg.models import ImportanceLevel, Task, Event, Headache


def test_valid_task():
    t1 = Task(title="Sort life out", importance=ImportanceLevel.HIGH)
    t2 = Task(title="Make appointmentst", importance=ImportanceLevel.MEDIUM)
    t3 = Task(title="Sort life out", importance=ImportanceLevel.LOW)
    assert all([isinstance(x, Task) for x in [t1, t2, t3]])
    assert t1.title == "Sort life out"
    assert t2.importance == 3


def test_invalid_task():
    with pytest.raises(ValidationError):
        ...


def test_valid_event(): ...


def test_invalid_event():
    with pytest.raises(ValidationError):
        ...


def test_valid_headache(): ...


def test_invalid_headache():
    with pytest.raises(ValidationError):
        ...
