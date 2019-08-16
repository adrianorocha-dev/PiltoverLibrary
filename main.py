from PyQt5 import uic, QtWidgets

class UI_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UI_Window, self).__init__(parent)
        uic.loadUi('base.ui', self)

        self.actionLogin.triggered.connect(self.back_to_Login)
        self.actionCadastrar_Usuario.triggered.connect(self.goto_CadastrarUsuario)

        self.show()

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

    window.stackedWidget.insertWidget(0, login)
    window.stackedWidget.insertWidget(1, cadastrarUsuario)
    
    #window.show()
    sys.exit(app.exec_())