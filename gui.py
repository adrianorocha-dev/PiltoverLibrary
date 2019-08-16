from PyQt5 import uic, QtWidgets

from firebase import auth, db
from data import User, LevelOfAccess

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

            if self.mainWindow:
                #self.mainWindow.back_to_login()
                self.mainWindow.stackedWidget.setCurrentIndex(0)
        else:
            print("validation error")
        


class CadastrarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarLivro, self).__init__(parent)
        uic.loadUi('cadastrar_livro.ui', self)

class EditarCadastro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarCadastro, self).__init__(parent)
        uic.loadUi('Editar_cadastro.ui', self)

class EditarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarLivro, self).__init__(parent)
        uic.loadUi('atualizar_livro.ui', self)

class MenuAdm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MenuAdm, self).__init__(parent)
        uic.loadUi('menuAdm.ui', self)

class MenuUsuario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MenuUsuario, self).__init__(parent)
        uic.loadUi('menu_usuario.ui', self)
        
class AdmLivros(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmLivros, self).__init__(parent)
        uic.loadUi('adm_livros.ui', self)
        
class AdmUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmUsuarios, self).__init__(parent)
        uic.loadUi('adm_usuarios.ui', self)