# Создайте класс Author и класс Book.
# Класс Book должен использовать композицию для включения автора в качестве объекта.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author.name}"


author = Author("J.K. Rowling", "British")
book = Book("Harry Potter and the Philosopher's Stone", author)
print(book)