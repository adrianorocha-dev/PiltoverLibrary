from firebase import db, auth

# email = input("Email:")
# pwd = input("Password:")

# user = auth.sign_in_with_email_and_password(email, pwd)

# from data import LevelOfAccess
# print(LevelOfAccess.COMMON_USER.value)

line = '192.168.125-00'

import re
line = re.sub('[.-]', '', line)

print(line)

exit()

booksRef = db.child('books')

from data import Book, User, LevelOfAccess

b = Book('1234567890123', 'Teste', "Editora", 'Genero', "Descrição do livro.", '2019', ['Fulano'])

print('sending ', b, ' to firebase...')
booksRef.push(b.to_dict())

u = User("fulano@mail.com", "Fulano", "123467543091", LevelOfAccess.COMMON_USER)
db.child('users').child(u.email).set(u.to_dict())

docs = booksRef.get()

print("Data:")
print(docs.val())

'''
for doc in docs.val():
    print('Retrieved document ', doc.id, ' from Firebase: ', Book.from_dict(doc.to_dict()))
'''