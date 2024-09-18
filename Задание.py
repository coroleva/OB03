# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Дополнительно:
#
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

#  мой вариант без зоопарка
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        pass

    def eat(self):
        return f'животное {self.name} кушает.'


class Bird(Animal):
    def make_sound(self, animal):
        return f'животное {animal.name} говорит {animal.sound}.'


class Mammal(Animal):
    def make_sound(self, animal):
        return f'животное {animal.name} говорит {animal.sound}.'


class Reptile(Animal):
    def make_sound(self, animal):
        return f'животное {animal.name} говорит {animal.sound}.'


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f'сотрудник {self.name} кормит {animal.name}'


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f'сотрудник {self.name} лечит {animal.name}'


class Zoo:
    def __init__(self):
        self.list_animals = []
        self.list_employees = []

    def add_list_animals(self, animal):
        self.list_animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def add_list_employees(self, employee):
        self.list_employees.append(employee)
        print(f'Сотрудник {employee.name} добавлен в персонал зоопарка')


bird1 = Bird('Сова', 5, 'Угу-угу')
mammal1 = Mammal('Волк', 3, "Уууу...")
reptile1 = Reptile("Змея", 1, "Шсшсшсссс")

zoo_keeper = ZooKeeper("Александр")
veterinar = Veterinarian("Анна Сергеевна")

zoo = Zoo()
zoo.add_list_animals(bird1)
zoo.add_list_animals(mammal1)
zoo.add_list_animals(reptile1)

zoo.add_list_employees(zoo_keeper)

for animal in zoo.list_animals:
    print(f'{animal.name}, {animal.make_sound(animal)}')

print(f'{zoo_keeper.feed_animal(bird1)}')
print(f'{veterinar.heal_animal(mammal1)}')
print(bird1.make_sound(bird1))  # привызове этого метода в параметр попадает созданный объект.имя
print(bird1.eat())