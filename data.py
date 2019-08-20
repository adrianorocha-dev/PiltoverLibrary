class Book:
    def __init__(self, isbn, title, pages, genre, description, year, author):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.genre = genre
        self.description = description
        self.year = year
        self.author = author
    
    @staticmethod
    def from_dict(source):
        book = Book(source['isbn'], source['title'], source['pages'], source['genre'], source['description'], source['year'], source['author'])

        return book
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'pages': self.pages,
            'genre': self.genre,
            'description': self.description,
            'year': self.year,
            'author': self.author,
        }
    
    def __repr__(self):
        return ('ISBN={}, Title={}, Year={}, Author={}'.format(self.isbn, self.title, self.year, self.author))

from enum import Enum
class LevelOfAccess(Enum):
    COMMON_USER = 0
    ADMIN = 1

class User():
    def __init__(self, email, name, cpf, level=LevelOfAccess.COMMON_USER):
        self.email = email
        self.name = name
        self.cpf = cpf
        self.level = level
    
    @staticmethod
    def from_dict(source):
        user = User(source['email'], source['name'], source['cpf'], level=LevelOfAccess(source['level']))
        return user

    def to_dict(self):
        return {
            'email': self.email,
            'name': self.name,
            'cpf': self.cpf,
            'level': self.level.value
        }
    
    def __repr__(self):
        return ('Email={}, Name={}, CPF={}, Level of Access={}'.format(self.email, self.name, self.cpf, self.level))