# класс двигатель с атрибутом power - мощность
# класс автомобиль с атрибутами model и engine_power - модель и двигатель_мощность
# внутри класс Car создайте экземпляр двигателя и сохраните его в атрибуте engine
class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return "Двигатель заведен"


class Car:
    def __init__(self, model, power):
        self.model = model
        self.engine = Engine(power)

eng = Engine(500)
print(eng.start())
car = Car("Audi", 300)
print(car.model)
print(car.engine.power)









