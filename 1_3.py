# АГРЕГАЦИЯ
# Этот код реализует две связанные между собой сущности — сотрудников (Employee) и команду (Team) с использованием композиции. Вот описание:
#
# Класс Employee:
#
# Представляет сотрудника с именем и должностью.
# В конструкторе (__init__) класса задаются два атрибута: name (имя сотрудника) и position (должность сотрудника).
# Класс Team:
#
# Представляет команду с названием и списком сотрудников.
# Конструктор класса принимает параметр team_name (название команды) и создает пустой список members, куда будут добавляться сотрудники.
# Метод add_member позволяет добавлять объект сотрудника (Employee) в команду, добавляя его в список members.
# Метод get_team_info возвращает строку с информацией о команде и списке имен всех членов команды, используя генератор списка для получения имени каждого сотрудника.
# Использование:
#
# Создаются два объекта класса Employee: employee1 с именем "John" и должностью "Developer", и employee2 с именем "Sara" и должностью "Designer".
# Затем создается объект команды team с названием "Product Team".
# С помощью метода add_member в команду добавляются созданные сотрудники.
# Метод get_team_info выводит информацию о команде, включая её название и имена членов, что отображается при вызове print.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, employee):
        self.members.append(employee)

    def get_team_info(self):
        return f"Team: {self.team_name}, Members: {[member.name for member in self.members]}"

# Использование
employee1 = Employee("John", "Developer")
employee2 = Employee("Sara", "Designer")

team = Team("Product Team")
team.add_member(employee1)
team.add_member(employee2)

print(team.get_team_info())
for member in team.members:
    print(member.name)
