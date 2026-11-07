from catalog.catalog import Catalog
from catalog.errors import RoomError
from catalog.models import Room
from catalog.storage import load, save

r1 = Room('1', '101', 'Лекционная', 2000, 30, 'А')
r2 = Room('2', '102', 'Компьютерный', 2005, 20, 'Б')

print('Создано комнат:', r1.name, r2.name)

try:
    Room('3', '103', 'Лекционная', 2010, 0, 'А')
except RoomError as e:
    print('Ошибка при создании:', e)

try:
    Room('4', '', 'Лекционная', 2010, 15, 'А')
except RoomError as e:
    print('Ошибка при создании:', e)

cat = Catalog()
cat.add(r1)
cat.add(r2)

print('Комнат в каталоге:', len(cat))
print('Поиск по типу:', len(cat.find_by_type('лекционная')))

save(cat, 'data.json')
print('Сохранено в файл')

new_cat = Catalog()
load(new_cat, 'data.json')
print('Загружено из файла:', len(new_cat))
