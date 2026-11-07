import json

from .errors import FileError, FormatError, RoomError
from .models import Room


def save(catalog, filename):
    rooms_list = []
    for room in catalog:
        info = {
            'room_id': room.room_id,
            'name': room.name,
            'room_type': room.room_type,
            'year': room.year,
            'count': room.count,
            'building': room.building
        }
        rooms_list.append(info)

    data = {
        'format_version': 1,
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

    if data.get('format_version') != 1:
        raise FormatError('Неизвестная версия файла')

    new_rooms = {}
    try:
        for item in data['rooms']:
            room = Room(
                room_id=item['room_id'],
                name=item['name'],
                room_type=item['room_type'],
                year=item['year'],
                count=item['count'],
                building=item['building']
            )
            if room.room_id in new_rooms:
                raise FileError('Дубликат ID в файле')
            new_rooms[room.room_id] = room
    except (KeyError, TypeError, RoomError):  # <--- ВОТ ТУТ ДОЛЖЕН БЫТЬ RoomError
        raise FileError('Ошибка обработки данных файла')

    catalog._rooms = new_rooms
