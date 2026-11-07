import pytest

from catalog.errors import RoomError
from catalog.models import Room


def test_room():
    room = Room('1', '101', 'Лекционная', 2000, 30, 'А')
    assert room.room_id == '1'
    assert room.count == 30

def test_zero_count():
    with pytest.raises(RoomError):
        Room('1', '101', 'Лекционная', 2000, 0, 'А')

def test_no_id():
    with pytest.raises(RoomError):
        Room('', '101', 'Лекционная', 2000, 30, 'А')
