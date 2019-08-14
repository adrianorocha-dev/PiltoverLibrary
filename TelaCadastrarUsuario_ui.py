# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastrarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(902, 550)
        Dialog.setStyleSheet("QPushButton{\n"
"borde: None;\n"
"}\n"
"\n"
"QDialog{\n"
"background: \n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_logo = QtWidgets.QPushButton(Dialog)
        self.pushButton_logo.setStyleSheet("QPushButton{\n"
"border: None; \n"
"}")
        self.pushButton_logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logo.setIcon(icon)
        self.pushButton_logo.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_logo.setObjectName("pushButton_logo")
        self.gridLayout.addWidget(self.pushButton_logo, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 25, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 20, 1, 1, 1)
        self.label_nome = QtWidgets.QLabel(Dialog)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 6, 1, 1, 1)
        self.label_CPF = QtWidgets.QLabel(Dialog)
        self.label_CPF.setObjectName("label_CPF")
        self.gridLayout.addWidget(self.label_CPF, 12, 1, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 11, 1, 1, 2)
        self.lineEdit_CPF = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.gridLayout.addWidget(self.lineEdit_CPF, 13, 1, 1, 2)
        self.label_login = QtWidgets.QLabel(Dialog)
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 14, 1, 1, 1)
        self.lineEdit_ConfirmarSenha = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ConfirmarSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_ConfirmarSenha.setObjectName("lineEdit_ConfirmarSenha")
        self.gridLayout.addWidget(self.lineEdit_ConfirmarSenha, 19, 1, 1, 2)
        self.lineEdit_Login = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.gridLayout.addWidget(self.lineEdit_Login, 15, 1, 1, 2)
        self.label_confirmarsenha = QtWidgets.QLabel(Dialog)
        self.label_confirmarsenha.setObjectName("label_confirmarsenha")
        self.gridLayout.addWidget(self.label_confirmarsenha, 18, 1, 1, 1)
        self.label_senha = QtWidgets.QLabel(Dialog)
        self.label_senha.setObjectName("label_senha")
        self.gridLayout.addWidget(self.label_senha, 16, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 13, 3, 1, 1)
        self.pushButton_cancelar = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancelar.setIcon(icon1)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.gridLayout.addWidget(self.pushButton_cancelar, 24, 1, 1, 2)
        self.label_cadastrarusuario = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_cadastrarusuario.setFont(font)
        self.label_cadastrarusuario.setObjectName("label_cadastrarusuario")
        self.gridLayout.addWidget(self.label_cadastrarusuario, 5, 1, 1, 1)
        self.pushButton_cadastrar = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cadastrar.setIcon(icon2)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.gridLayout.addWidget(self.pushButton_cadastrar, 23, 1, 1, 2)
        self.lineEdit_Senha = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.gridLayout.addWidget(self.lineEdit_Senha, 17, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_nome.setText(_translate("Dialog", "Nome:"))
        self.label_CPF.setText(_translate("Dialog", "CPF:"))
        self.lineEdit_CPF.setInputMask(_translate("Dialog", "99999999999"))
        self.label_login.setText(_translate("Dialog", "Login:"))
        self.label_confirmarsenha.setText(_translate("Dialog", "Confirme Senha:"))
        self.label_senha.setText(_translate("Dialog", "Senha:"))
        self.pushButton_cancelar.setText(_translate("Dialog", "Cancelar"))
        self.label_cadastrarusuario.setText(_translate("Dialog", "       Cadastrar Usuário"))
        self.pushButton_cadastrar.setText(_translate("Dialog", "Cadastrar"))
