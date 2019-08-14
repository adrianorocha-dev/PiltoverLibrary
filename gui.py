from PyQt5 import uic, QtWidgets

class LoginUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginUI, self).__init__(parent)
        uic.loadUi('login.ui', self)

class CadastrarUsuario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarUsuario, self).__init__(parent)
        uic.loadUi('TelaCadastrarUsuario.ui', self)

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

class AdmLivros(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmLivros, self).__init__(parent)
        uic.loadUi('adm_livros.ui', self)
        
class AdmUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmUsuarios, self).__init__(parent)
        uic.loadUi('adm_usuarios.ui', self)