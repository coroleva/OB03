# Пример 3: Полиморфизм через операцию с методами drive для разных транспортных средств
# Класссы для нескольких транспортных средств и методы drive для каждого из них.
# Реализация: создать список транспортных средств и вызвать метод drive
# для каждого из них через дополнительную функцию start_drive
class Vehicle:
    def drive(self):
        pass
class Car(Vehicle):
    def drive(self):
        print("Автомобиль едет")
class Truck(Vehicle):
    def drive(self):
        print("Грузовик едет")
class Bus(Vehicle):
    def drive(self):
        print("Автобус едет")
class Airplane(Vehicle):
    def drive(self):
        print("Самолет летит")
class Steamship(Vehicle):
    def drive(self):
        print("Паараход плывет")

vehicles = [Car(), Truck(), Bus(), Airplane(), Steamship()]
for vehicle in vehicles:
    vehicle.drive()