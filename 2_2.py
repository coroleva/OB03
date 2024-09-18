# Пример 2: Полиморфизм с методами area для разных фигур
# классы: Rectangle, Square, Circle (атрибуты для  определения площади)
# и метод area для вычисления площади
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f'Площать прямоугольника со сторонами {self.width} и {self.height} = {self.width * self.height}')


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        print(f'Площать квадрата со стороной {self.width}  = {self.width ** 2}')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f'Площать окружности с радиусом {self.radius}  = {3.1415 * self.radius ** 2}')

# # 1 вариант реализаии
# figures = [Rectangle(10, 10), Square(5), Circle(10)]
# for figure in figures:
#     figure.area()

# 2 вариант реализаии
def area_calculation(figure):
    figure.area()

figures = [Rectangle(10, 10), Square(5), Circle(10)]
for figure in figures:
    area_calculation(figure)