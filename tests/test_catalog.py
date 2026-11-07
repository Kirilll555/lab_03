import pytest

from catalog.catalog import Catalog
from catalog.errors import DupError, NoRoomError
from catalog.models import Room


def test_add_remove():
    cat = Catalog()
    room = Room('1', '101', 'Лекционная', 2000, 30, 'А')

    cat.add(room)
    assert len(cat) == 1
    assert '1' in cat
    assert cat.get('1') == room

    cat.remove('1')
    assert len(cat) == 0
    assert '1' not in cat


def test_dup_id():
    cat = Catalog()
    room = Room('1', '101', 'Лекционная', 2000, 30, 'А')
    cat.add(room)
    with pytest.raises(DupError):
        cat.add(room)


def test_no_room():
    cat = Catalog()
    with pytest.raises(NoRoomError):
        cat.get('999')
    with pytest.raises(NoRoomError):
        cat.remove('999')


def test_find():
    cat = Catalog()
    cat.add(Room('1', '101', 'Лекционная', 2000, 30, 'А'))
    cat.add(Room('2', '102', 'Компьютерный', 2005, 20, 'Б'))
    cat.add(Room('3', '201', 'лекционная', 2010, 50, 'В'))

    found_type = cat.find_by_type('лекционная')
    assert len(found_type) == 2

    found_name = cat.find_by_name('10')
    assert len(found_name) == 2


def test_iter():
    cat = Catalog()
    cat.add(Room('3', '301', 'Лекционная', 2000, 30, 'А'))
    cat.add(Room('1', '101', 'Лекционная', 2000, 30, 'А'))
    cat.add(Room('2', '201', 'Лекционная', 2000, 30, 'А'))

    ids = [room.room_id for room in cat]
    assert ids == ['1', '2', '3']
