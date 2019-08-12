from firebase import db, auth

email = input("Email:")
pwd = input("Password:")

user = auth.sign_in_with_email_and_password(email, pwd)

booksRef = db.child('books')

from data import Book

b = Book('1234567890123', 'Teste', "Editora", 'Genero', "Descrição do livro.", '2019', ['Fulano'])

print('sending ', b, ' to firebase...')
booksRef.push(b.to_dict())

docs = booksRef.get()

print("Data:")
print(docs.val())

'''
for doc in docs.val():
    print('Retrieved document ', doc.id, ' from Firebase: ', Book.from_dict(doc.to_dict()))
'''