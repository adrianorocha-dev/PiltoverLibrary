from PyQt5 import uic, QtWidgets

class UI_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UI_Window, self).__init__(parent)
        uic.loadUi('base.ui', self)

        self.actionLogin.triggered.connect(self.back_to_Login)
        self.actionCadastrar_Usuario.triggered.connect(self.goto_CadastrarUsuario)
        self.actionMenu_Adm.triggered.connect(self.goto_Adm)
        self.actionAdm_Usu_rio.triggered.connect(self.goto_adm_user)


        self.show()

    def goto_CadastrarLivro(self):
        self.stackedWidget.setCurrentIndex(7)
        
    def goto_edt_livro(self):
        self.stackedWidget.setCurrentIndex(6)

    def goto_edt_cadastro(self):
        self.stackedWidget.setCurrentIndex(5)

    def goto_adm_livros(self):
       self.stackedWidget.setCurrentIndex(4)

    def goto_adm_user (self):
       self.stackedWidget.setCurrentIndex(3)

    def goto_Adm(self):
       self.stackedWidget.setCurrentIndex(2)

    def goto_CadastrarUsuario(self):
        self.stackedWidget.setCurrentIndex(1)

    def back_to_Login(self):
        self.stackedWidget.setCurrentIndex(0)

    

if __name__ == "__main__":
    import sys

    from gui import *

    app = QtWidgets.QApplication(sys.argv)
    window = UI_Window()


    login = LoginUI()
    login.pushButton_cadastrar.clicked.connect(window.goto_CadastrarUsuario)
    
    cadastrarUsuario = CadastrarUsuario()
    cadastrarUsuario.pushButton_cancelar.clicked.connect(window.back_to_Login)
    cadastrarUsuario.pushButton_cadastrar.clicked.connect(window.back_to_Login)

    menuAdm = menuAdm()
    menuAdm.pushButton_admUsuarios.clicked.connect(window.goto_adm_user)
    menuAdm.pushButton_AdmLivros.clicked.connect(window.goto_adm_livros)
    
    adm_usuario = AdmUsuarios()
    adm_usuario.pushButton_Editar.clicked.connect(window.goto_edt_cadastro)
    adm_usuario.pushButton_adicionar.clicked.connect(window.goto_CadastrarUsuario)

    AdmLivros = AdmLivros()
    AdmLivros.pushButton_editar.clicked.connect(window.goto_edt_livro)
    AdmLivros.pushButton_adicionar.clicked.connect(window.goto_CadastrarLivro)

    CadastrarLivro = CadastrarLivro()

    EditarCadastro = EditarCadastro()

    EditarLivro = EditarLivro()

    window.stackedWidget.insertWidget(0, login)
    window.stackedWidget.insertWidget(1, cadastrarUsuario)
    window.stackedWidget.insertWidget(2, menuAdm)
    window.stackedWidget.insertWidget(3, adm_usuario)
    window.stackedWidget.insertWidget(4, AdmLivros)
    window.stackedWidget.insertWidget(5, EditarCadastro)
    window.stackedWidget.insertWidget(6, EditarLivro)
    window.stackedWidget.insertWidget(7, CadastrarLivro)
    

    #window.show()
    sys.exit(app.exec_())