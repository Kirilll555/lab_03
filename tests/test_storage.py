import pytest

from catalog.catalog import Catalog
from catalog.errors import FileError, FormatError
from catalog.models import Room
from catalog.storage import load, save


def test_save_load(tmp_path):
    file = tmp_path / 'data.json'
    cat = Catalog()
    cat.add(Room('1', '101', 'Лекционная', 2000, 30, 'А'))

    save(cat, file)

    new_cat = Catalog()
    load(new_cat, file)

    assert len(new_cat) == 1
    assert new_cat.get('1').name == '101'


def test_incorrect_version(tmp_path):
    file = tmp_path / 'data.json'
    file.write_text('{"format_version": 999, "rooms": []}')

    with pytest.raises(FormatError):
        load(Catalog(), file)


def test_incorrect_json(tmp_path):
    file = tmp_path / 'data.json'
    file.write_text('?')

    with pytest.raises(FileError):
        load(Catalog(), file)


def test_atomic(tmp_path):
    file = tmp_path / 'data.json'
    file.write_text('{"format_version": 1, "rooms": [{"room_id": "1"}]}')

    cat = Catalog()
    cat.add(Room('real', 'Настоящая', 'Лекционная', 2000, 30, 'А'))

    with pytest.raises(FileError):
        load(cat, file)

    assert len(cat) == 1
    assert 'real' in cat
