from dataclasses import dataclass

from .errors import RoomError


@dataclass
class Room:
    room_id: str
    name: str
    room_type: str
    year: int
    count: int
    building: str

    def __post_init__(self):
        if not self.room_id:
            raise RoomError('Пустой ID')
        if not self.name:
            raise RoomError('Пустое название')
        if self.count <= 0:
            raise RoomError('Количество мест должно быть больше нуля')
