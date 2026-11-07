from .errors import DupError, NoRoomError


class Catalog:
    def __init__(self):
        self._rooms = {}

    def add(self, room):
        if room.room_id in self._rooms:
            raise DupError('Аудитория с таким ID уже есть')
        self._rooms[room.room_id] = room

    def get(self, room_id):
        if room_id not in self._rooms:
            raise NoRoomError('Аудитория не найдена')
        return self._rooms[room_id]

    def remove(self, room_id):
        if room_id not in self._rooms:
            raise NoRoomError('Аудитория не найдена')
        del self._rooms[room_id]

    def find_by_type(self, room_type):
        res = []
        for room in self._rooms.values():
            if room.room_type.lower() == room_type.lower():
                res.append(room)
        return res

    def find_by_name(self, query):
        res = []
        for room in self._rooms.values():
            if query.lower() in room.name.lower():
                res.append(room)
        return res

    def __len__(self):
        return len(self._rooms)

    def __iter__(self):
        keys = sorted(self._rooms.keys())
        for k in keys:
            yield self._rooms[k]

    def __contains__(self, room_id):
        return room_id in self._rooms
