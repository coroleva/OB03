# Полиморфизм
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Гаф!"
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Мяу!"

def animals_speak(animals):
    for animal in animals:
        print(f'{animal.name} {animal.speak()}')

animals = [Dog("Бобик"), Cat("Мурзик")]
animals_speak(animals)