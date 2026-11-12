import json

from catalog.errors import FileError, FormatError, RoomError
from catalog.models import Room

FORMAT_VERSION = 1
FIELDS = ['room_id', 'name', 'room_type', 'year', 'count', 'building']


def save(catalog, filename):
    rooms_list = []
    for room in catalog:
        info = {}
        for field in FIELDS:
            info[field] = getattr(room, field)
        rooms_list.append(info)

    data = {
        'format_version': FORMAT_VERSION,
        'rooms': rooms_list
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def load(catalog, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        raise FileError('Ошибка обработки файла')

    if data.get('format_version') != FORMAT_VERSION:
        raise FormatError('Неизвестная версия файла')

    new_rooms = {}
    try:
        for item in data['rooms']:
            room = Room(**{field: item[field] for field in FIELDS})

            if room.room_id in new_rooms:
                raise FileError('Дубликат ID в файле')
            new_rooms[room.room_id] = room
    except (KeyError, TypeError, RoomError):
        raise FileError('Ошибка обработки данных файла')

    catalog._rooms = new_rooms