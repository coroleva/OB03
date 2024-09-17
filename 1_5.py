# АГРЕГАЦИЯ
# Этот код создает простую структуру, состоящую из дома и комнат, с использованием принципа композиции в ООП.
#
# Класс Room (Комната):
#
# У класса есть метод инициализации __init__, который принимает параметр name (название комнаты) и сохраняет его в атрибуте объекта self.name.
# Метод describe возвращает строку, описывающую комнату, например: "This is the living room".
# Класс House (Дом):
#
# Метод инициализации __init__ создает пустой список self.rooms, куда будут добавляться комнаты.
# Метод add_room принимает объект комнаты и добавляет его в список комнат дома.
# Метод show_rooms возвращает список описаний всех комнат в доме. Он использует метод describe для каждой комнаты в списке self.rooms.
# Создание объектов:
#
# Создаются два объекта класса Room: комната под названием "living room" и комната под названием "kitchen".
# Затем создается объект класса House (дом).
# С помощью метода add_room комнаты добавляются в дом.
# Вывод информации:
#
# В конце программа вызывает метод show_rooms, который выводит описания всех комнат в доме в виде списка строк. Например: ["This is the living room", "This is the kitchen"].
# Таким образом, этот код моделирует дом, который состоит из нескольких комнат, каждая из которых может быть добавлена и описана.

class Room:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is the {self.name}"

class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        return [room.describe() for room in self.rooms]

living_room = Room("living room")
kitchen = Room("kitchen")

house = House()
house.add_room(living_room)
house.add_room(kitchen)

print(house.show_rooms())
