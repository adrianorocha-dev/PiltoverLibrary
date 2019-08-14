# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 550))
        self.stackedWidget.setObjectName("stackedWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionCadastrar_Livro = QtWidgets.QAction(MainWindow)
        self.actionCadastrar_Livro.setObjectName("actionCadastrar_Livro")
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionCadastrar_Livro)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionCadastrar_Livro.setText(_translate("MainWindow", "Cadastrar Livro"))



def goto_CadastrarUsuario():
    ui.stackedWidget.setCurrentIndex(1)

def back_to_Login():
    ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys

    from gui import LoginUI, CadastrarUsuario

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    login = LoginUI()
    login.pushButton_cadastrar.clicked.connect(goto_CadastrarUsuario)
    cadastrarUsuario = CadastrarUsuario()
    cadastrarUsuario.pushButton_cancelar.clicked.connect(back_to_Login)

    ui.stackedWidget.insertWidget(0, login)
    ui.stackedWidget.insertWidget(1, cadastrarUsuario)

    MainWindow.show()
    sys.exit(app.exec_())
