from PyQt5 import uic, QtWidgets

from firebase import auth, db
from data import User, LevelOfAccess, Book

class LoginUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginUI, self).__init__(parent)
        uic.loadUi('login.ui', self)

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

            if self.mainWindow:
                #self.mainWindow.back_to_login()
                self.mainWindow.stackedWidget.setCurrentIndex(0)
        else:
            print("validation error")
        


class CadastrarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarLivro, self).__init__(parent)
        uic.loadUi('cadastrar_livro.ui', self)

        self.pushButton_cadastrar.clicked.connect(self.save_to_firebase)
       
    def save_to_firebase(self):

            
            titulo = self.lineEdit_titulo.text()
            numerodepaginas = self.lineEdit_numerodepaginas.text()
            isbn = self.lineEdit_ISBN.text()
            ano = self.lineEdit_ano.text()
            genero = self.lineEdit_Genero.text()
            descricao = self.lineEdit_descricao.text()
            autor = self.lineEdit_autor.text()

            if not(titulo == '' or numerodepaginas == '' or isbn == '' or  genero == '' or descricao == '' or autor == ''):


            #Remove dots and dashes from CPF
    
                book = Book(isbn, titulo, numerodepaginas, genero, descricao, ano, autor)

                db.child('books').push(book.to_dict())

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.NoIcon)
                msg.setText("Sucesso")
                msg.setInformativeText("Cadastrado com sucesso!")
                msg.setWindowTitle("Sucesso")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.NoIcon)
                msg.setText("Failure")
                msg.setInformativeText("Todos os campos são obrigatorios")
                msg.setWindowTitle("Failure")
                msg.exec_()
    
   
        
class EditarCadastro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarCadastro, self).__init__(parent)
        uic.loadUi('Editar_cadastro.ui', self)

class EditarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarLivro, self).__init__(parent)
        uic.loadUi('atualizar_livro.ui', self)

class menuAdm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(menuAdm, self).__init__(parent)
        uic.loadUi('menuAdm.ui', self)
        
class AdmLivros(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmLivros, self).__init__(parent)
        uic.loadUi('adm_livros.ui', self)

        self.pushButton_buscar.clicked.connect(self.search_book)
    
        
        self.titulos = []

        self.books = db.child('books').get()
        for self.book in self.books.each():
            print(self.book.val()['title'])
            self.titulos.append(self.book.val()['title'].upper())
            self.textBrowser_info.setText(self.textBrowser_info.toPlainText()+ self.book.val()['title'] + ":" + self.book.val()['author']+ "\n")
        
    def search_book(self):
        titulo = self.lineEdit_buscar.text().upper()
        if (titulo in self.titulos):
             for t in self.books.each():
                 if (t.val()['title'].upper()==titulo):
                     self.textBrowser_info.setText("Título: " + t.val()['title'] + "\n Autor: " + t.val()['author'] + "\n Gênero: " + t.val()['genre'] + "\n ISBN: " + t.val()['isbn'] + "\n Descrição: " + t.val()['description'] + "\n Ano: "+ t.val()['year'] + "\n Nº de páginas: " + t.val()['publisher'])
        else:
            print("nao achei")


        
class AdmUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmUsuarios, self).__init__(parent)
        uic.loadUi('adm_usuarios.ui', self)

        self.pushButton_buscar.clicked.connect(self.search_user)
    
        
        self.userslist = []

        self.users = db.child('users').get()
        for self.user in self.users.each():
            print(self.user.val()['name'])
            self.userslist.append(self.user.val()['name'].upper())
            self.textBrowser_info.setText(self.textBrowser_info.toPlainText()+ self.user.val()['name'] + " : " + self.user.val()['cpf']+ "\n")
        
    def search_user(self):
        usuario = self.lineEdit_buscar.text().upper()
        if (usuario in self.userslist):
             for u in self.users.each():
                 if (u.val()['name'].upper()==usuario):
                     self.textBrowser_info.setText("Nome: " + u.val()['name'] + "\n CPF: " + u.val()['cpf'] + "\n Email: " + u.val()['email'] )
        else:
            print("nao achei")
