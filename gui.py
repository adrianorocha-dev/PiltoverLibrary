from PyQt5 import uic, QtWidgets

from firebase import auth, db
from data import User, LevelOfAccess, Book

import requests
import json

firebase_user = None
loggedUser = None

class LoginUI(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(LoginUI, self).__init__(parent)
        uic.loadUi('login.ui', self)

        self.mainWindow = mainWindow

        self.pushButton_confirmar.clicked.connect(self.authenticate)
    
    def authenticate(self):
        email = self.lineEdit_login.text()
        password = self.lineEdit_senha.text()

        global firebase_user
        global loggedUser

        try:
            firebase_user = auth.sign_in_with_email_and_password(email, password)
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            if error['message'] == "INVALID_PASSWORD":
                infoText = "Senha inválida"
            elif error['message'] == "EMAIL_NOT_FOUND":
                infoText = "Email não cadastrado"
            elif error['message'] == "INVALID_EMAIL":
                infoText = "Email inválido"
            else:
                infoText = "Erro no Login"
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Erro")
            msg.setInformativeText(infoText)
            msg.setWindowTitle("Erro")
            msg.exec_()

        if firebase_user:
            userDict = db.child('users').order_by_child('email').equal_to(email).get().each()
            loggedUser = User.from_dict(userDict[0].val())

            if loggedUser.level == LevelOfAccess.ADMIN:
                self.mainWindow.stackedWidget.setCurrentIndex(2)
            else:
                self.mainWindow.stackedWidget.setCurrentIndex(3)


class CadastrarUsuario(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(CadastrarUsuario, self).__init__(parent)
        uic.loadUi('TelaCadastrarUsuario.ui', self)

        self.mainWindow = mainWindow

        self.pushButton_cadastrar.clicked.connect(self.save_to_firebase)

    def validate(self):
        import re
        nameVal = self.lineEdit_nome.text() != ""
        cpfVal = re.match("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", self.lineEdit_CPF.text()) != None
        emailVal = re.match(".*@.*\..*", self.lineEdit_Login.text()) != None
        pwdVal = (self.lineEdit_Senha.text()) == (self.lineEdit_ConfirmarSenha.text())
        
        print("Validando...")

        if not (nameVal and cpfVal and emailVal and pwdVal):
            if not nameVal:
                infoText = "Erro! Preencha o campo nome."
            elif not cpfVal:
                infoText = "Erro! CPF inválido."
            elif not emailVal:
                infoText = "Erro! Email inválido."
            else:
                infoText = "Erro! A senha e a confirmação estão diferentes."
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Erro")
            msg.setInformativeText(infoText)
            msg.setWindowTitle("Erro")
            msg.exec_()

            return False
        else:
            print("validado")
            return True

    def save_to_firebase(self):
        validation = self.validate()
        if validation:
            print("validation success")
            email = self.lineEdit_Login.text()
            password = self.lineEdit_Senha.text()
            name = self.lineEdit_nome.text()
            cpf = self.lineEdit_CPF.text()

            #Remove dots and dashes from CPF
            from re import sub as re_sub
            cpf = re_sub('[.-]', '', cpf)

            user = User(email, name, cpf, LevelOfAccess.COMMON_USER)

            auth.create_user_with_email_and_password(email, password)
            db.child('users').push(user.to_dict())

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg.setText("Sucesso")
            msg.setInformativeText("Cadastrado com sucesso!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()

            global loggedUser

            if self.mainWindow:
                if loggedUser != None and loggedUser.level == LevelOfAccess.ADMIN:
                    self.mainWindow.stackedWidget.setCurrentIndex(4)
                else:
                    self.mainWindow.stackedWidget.setCurrentIndex(0)
        else:
            print("validation error")
        


class CadastrarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarLivro, self).__init__(parent)
        uic.loadUi('cadastrar_livro.ui', self)

        self.pushButton_cadastrar.clicked.connect(self.save_to_firebase)
    
    def validate(self):
        from re import match

        titleVal = self.lineEdit_titulo.text() != ""
        isbnVal = match("[0-9]{10} | [0-9]{13}", self.lineEdit_ISBN.text()) != None
        pagesVal = match("[0-9]+", self.lineEdit_numerodepaginas.text()) != None
        yearVal = match("[0-9]{4}", self.lineEdit_ano.text()) != None
        genreVal = self.lineEdit_Genero.text() != ""
        descVal = self.lineEdit_descricao.text() != ""
        authorVal = self.lineEdit_autor.text() != ""

        if not (titleVal and isbnVal and pagesVal and yearVal and genreVal and descVal and authorVal):
            if not titleVal:
                infoText = "Preencha o campo Título."
            elif not isbnVal:
                infoText = "O ISBN está em um formato inválido."
            elif not pagesVal:
                infoText = "O Número de páginas está em um formato inválido."
            elif not yearVal:
                infoText = "O campo Ano está em formato inválido."
            elif not genreVal:
                infoText = "Preencha o campo Gênero."
            elif not descVal:
                infoText = "Preencha o campo Descrição."
            else: # not author
                infoText = "Preencha o campo Autor."
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Erro")
            msg.setInformativeText(infoText)
            msg.setWindowTitle("Erro")
            msg.exec_()

            return False
        else:
            print('Validado')
            return True

    def save_to_firebase(self):
        validation = self.validate()
        if validation:
            titulo = self.lineEdit_titulo.text()
            isbn = self.lineEdit_ISBN.text()
            numerodepaginas = self.lineEdit_numerodepaginas.text()
            ano = self.lineEdit_ano.text()
            genero = self.lineEdit_Genero.text()
            descricao = self.lineEdit_descricao.text()
            autor = self.lineEdit_autor.text()

            book = Book(isbn, titulo, numerodepaginas, genero, descricao, ano, autor)

            db.child('books').push(book.to_dict())

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg.setText("Sucesso")
            msg.setInformativeText("Cadastrado com sucesso!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()
        else:
            print("Validation Error")
    
   
        
class EditarCadastro(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(EditarCadastro, self).__init__(parent)
        uic.loadUi('Editar_cadastro.ui', self)

        self.mainWindow = mainWindow

        self.editing_user = None

        self.pushButton_alterar.clicked.connect(self.save_to_firebase)
        self.pushButton_Excluir.clicked.connect(self.delete)

    def setValues(self, user):
        self.editing_user = user
        self.lineEdit_Nome.setText(user.name)
        self.lineEdit_CPF.setText(user.cpf)
        self.radioButton_common.setChecked(False)
        self.radioButton_common.setChecked(False)

    
    def validate(self):
        import re
        nameVal = self.lineEdit_Nome.text() != ""
        cpfVal = re.match("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", self.lineEdit_CPF.text()) != None
        
        print("Validando...")

        if not (nameVal and cpfVal):
            if not nameVal:
                infoText = "Erro! Preencha o campo nome."
            else: # not cpfVal
                infoText = "Erro! CPF inválido."
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Erro")
            msg.setInformativeText(infoText)
            msg.setWindowTitle("Erro")
            msg.exec_()

            return False
        else:
            print("validado")
            return True
    
    def save_to_firebase(self):
        validation = self.validate()
        if validation:
            name = self.lineEdit_Nome.text()
            cpf = self.lineEdit_CPF.text()

            #Remove dots and dashes from CPF
            from re import sub as re_sub
            cpf = re_sub('[.-]', '', cpf)

            user_update = { 'name': name, 'cpf': cpf }

            user = db.child('users').order_by_child("email").equal_to(self.editing_user.email).get().each()
            db.child('users').child(user[0].key()).update(user_update)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg.setText("Sucesso")
            msg.setInformativeText("Alterações salvas com sucesso!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()

            if self.mainWindow:
                if loggedUser != None and loggedUser.level == LevelOfAccess.ADMIN:
                    self.mainWindow.stackedWidget.setCurrentIndex(4)
                else:
                    self.mainWindow.stackedWidget.setCurrentIndex(0)
            
    def delete(self):
        from firebase import admin_auth

        user = db.child('users').order_by_child('email').equal_to(self.editing_user.email).get().each()
        db.child('users').child(user[0].key()).remove()
        
        auth_user = admin_auth.get_user_by_email(self.editing_user.email)
        admin_auth.delete_user(auth_user.uid)

class EditarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(EditarLivro, self).__init__(parent)
        uic.loadUi('atualizar_livro.ui', self)

        self.mainWindow = mainWindow
        
        self.editing_book = None

        self.pushButton_confirmar.clicked.connect(self.setValuesInFirebase)
        self.pushButton_Excluir.clicked.connect(self.deletelivro)

    def deletelivro(self):
        book = db.child('books').order_by_child("isbn").equal_to(self.lineEdit_ISBN.text()).get().each()
        db.child('books').child(book[0].key()).remove()


    def setValues(self, livro):
        self.editing_book = livro
        self.lineEdit_titulo.setText(livro.title)
        self.lineEdit_numerodepaginas.setText(livro.pages)
        self.lineEdit_ano.setText(livro.year)
        self.lineEdit_Genero.setText(livro.genre)
        self.lineEdit_descricao.setText(livro.description)
        self.lineEdit_autor.setText(livro.author)

    def validate(self):
        from re import match

        titleVal = self.lineEdit_titulo.text() != ""
        pagesVal = match("[0-9]+", self.lineEdit_numerodepaginas.text()) != None
        yearVal = match("[0-9]{4}", self.lineEdit_ano.text()) != None
        genreVal = self.lineEdit_Genero.text() != ""
        descVal = self.lineEdit_descricao.text() != ""
        authorVal = self.lineEdit_autor.text() != ""

        if not (titleVal and pagesVal and yearVal and genreVal and descVal and authorVal):
            if not titleVal:
                infoText = "Preencha o campo Título."
            elif not pagesVal:
                infoText = "O Número de páginas está em um formato inválido."
            elif not yearVal:
                infoText = "O campo Ano está em formato inválido."
            elif not genreVal:
                infoText = "Preencha o campo Gênero."
            elif not descVal:
                infoText = "Preencha o campo Descrição."
            else: # not author
                infoText = "Preencha o campo Autor."
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Erro")
            msg.setInformativeText(infoText)
            msg.setWindowTitle("Erro")
            msg.exec_()

            return False
        else:
            print('Validado')
            return True

    def setValuesInFirebase (self):
        validation = self.validate()
        if validation:
            titulo = self.lineEdit_titulo.text()
            numerodepaginas = self.lineEdit_numerodepaginas.text()
            ano = self.lineEdit_ano.text()
            genero = self.lineEdit_Genero.text()
            descricao = self.lineEdit_descricao.text()
            autor = self.lineEdit_autor.text()
    
            book_update = {'title': titulo, 'pages': numerodepaginas, 'genre': genero, 'description': descricao, 'year': ano, 'author': autor}

            book = db.child('books').order_by_child("isbn").equal_to(self.editing_book.isbn).get().each()

            db.child('books').child(book[0].key()).update(book_update)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg.setText("Sucesso")
            msg.setInformativeText("Alterações salvas com sucesso!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()

            if self.mainWindow:
                if loggedUser != None and loggedUser.level == LevelOfAccess.ADMIN:
                    self.mainWindow.stackedWidget.setCurrentIndex(4)
                else:
                    self.mainWindow.stackedWidget.setCurrentIndex(0)
        else:
            print("Validation Error")
    
               



class MenuAdm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MenuAdm, self).__init__(parent)
        uic.loadUi('menuAdm.ui', self)

class MenuUsuario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MenuUsuario, self).__init__(parent)
        uic.loadUi('menu_usuario.ui', self)

        self.pushButton_buscar.clicked.connect(self.search_book)
        self.pushButton_listar.clicked.connect(self.list_books)
        self.list_books()

    def list_books(self):
        
        self.titulos = []

        self.textBrowser_info.setText('')

        self.books = db.child('books').get()
        for self.book in self.books.each():
            print(self.book.val()['title'])
            self.titulos.append(self.book.val()['title'].upper())
            self.textBrowser_info.setText(self.textBrowser_info.toPlainText()+ "{} : {}\n".format(self.book.val()['title'], self.book.val()['author']))
        
    def search_book(self):
        self.textBrowser_info.setText('')
        titulo = self.lineEdit_buscar.text().upper()
        if (titulo in self.titulos):
            for t in self.books.each():
                if (t.val()['title'].upper()==titulo):
                    self.textBrowser_info.setText("Título: {}\nAutor: {}\nGênero: {}\nISBN: {}\nDescrição: {}\nAno: {}\nNúmero de páginas: {}\n".format(t.val()['title'], t.val()['author'], t.val()['genre'], t.val()['isbn'], t.val()['description'], t.val()['year'], t.val()['pages']))
        else:
            print("nao achei")
            self.list_books()
            

class AdmLivros(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(AdmLivros, self).__init__(parent)
        uic.loadUi('adm_livros.ui', self)

        self.mainWindow = mainWindow

        self.pushButton_editar.setVisible(False)
        self.pushButton_buscar.clicked.connect(self.search_book)
        self.pushButton_editar.clicked.connect(self.edit_book)
        self.pushButton_cancelar.clicked.connect(self.limpes)
       
        self.list_books()
        
    def limpes(self):
        self.textBrowser_info.setText('')
        self.list_books()
        
    def list_books(self):
        
        self.titulos = []
        self.textBrowser_info.setText("")

        self.books = db.child('books').get()
        for book in self.books.each():
            print(book.val()['title'])
            self.titulos.append(book.val()['title'].upper())
            self.textBrowser_info.setText(self.textBrowser_info.toPlainText()+ "{} (por {})\n".format(book.val()['title'], book.val()['author']))
        
    def search_book(self):
        self.pushButton_editar.setVisible(False)
        self.textBrowser_info.setText('')
        titulo = self.lineEdit_buscar.text().upper()
        if (titulo in self.titulos):
            self.pushButton_editar.setVisible(True)
            for t in self.books.each():
                if (t.val()['title'].upper()==titulo):
                    self.textBrowser_info.setText("Título: {}\nAutor: {}\nGênero: {}\nISBN: {}\nDescrição: {}\nAno: {}\nNúmero de páginas: {}\n".format(t.val()['title'], t.val()['author'], t.val()['genre'], t.val()['isbn'], t.val()['description'], t.val()['year'], t.val()['pages']))
                    self.livro = Book.from_dict(t.val())
        
        else:
            print("nao achei")
            self.list_books()
        
    def edit_book(self):
        self.mainWindow.stackedWidget.setCurrentIndex(7)
        self.mainWindow.stackedWidget.widget(7).setValues(self.livro)

        
class AdmUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None, mainWindow=None):
        super(AdmUsuarios, self).__init__(parent)
        uic.loadUi('adm_usuarios.ui', self)

        self.mainWindow = mainWindow

        self.pushButton_Editar.setVisible(False)
        self.pushButton_buscar.clicked.connect(self.search_user)
        self.pushButton_Editar.clicked.connect(self.edit_user)

        self.list_users()
    
    def list_users(self):
        
        self.userslist = []

        self.textBrowser_info.setText("")

        self.users = db.child('users').get()
        for self.user in self.users.each():
            print(self.user.val()['name'])
            self.userslist.append(self.user.val()['email'].lower())
            self.textBrowser_info.setText(self.textBrowser_info.toPlainText()+ "{} ({})\n".format(self.user.val()['email'], self.user.val()['name']))
        
    def search_user(self):
        self.pushButton_Editar.setVisible(False)
        self.textBrowser_info.setText('')
        usuario_email = self.lineEdit_buscar.text().lower()
        if (usuario_email in self.userslist):
             self.pushButton_Editar.setVisible(True)
             for u in self.users.each():
                 if (u.val()['email'].lower()==usuario_email):
                     self.textBrowser_info.setText("Nome: {}\nCPF: {}\nEmail: {}\n".format(u.val()['name'], u.val()['cpf'], u.val()['email']))
                     self.user_to_edit = User.from_dict(u.val())
        else:
            print("nao achei")
            self.list_users()

    def edit_user(self):
        self.mainWindow.stackedWidget.setCurrentIndex(6)
        self.mainWindow.stackedWidget.widget(6).setValues(self.user_to_edit)