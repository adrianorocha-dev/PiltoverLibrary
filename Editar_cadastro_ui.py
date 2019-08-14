# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editar_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Nome(object):
    def setupUi(self, Dialog_Nome):
        Dialog_Nome.setObjectName("Dialog_Nome")
        Dialog_Nome.resize(900, 550)
        self.pushButton_alterar = QtWidgets.QPushButton(Dialog_Nome)
        self.pushButton_alterar.setGeometry(QtCore.QRect(334, 396, 80, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Icon/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_alterar.setIcon(icon)
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.lineEdit_Login = QtWidgets.QLineEdit(Dialog_Nome)
        self.lineEdit_Login.setGeometry(QtCore.QRect(330, 277, 290, 25))
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.pushButton_cancelar = QtWidgets.QPushButton(Dialog_Nome)
        self.pushButton_cancelar.setEnabled(True)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(434, 396, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_cancelar.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_cancelar.setIcon(icon1)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.label_editora = QtWidgets.QLabel(Dialog_Nome)
        self.label_editora.setGeometry(QtCore.QRect(330, 200, 290, 17))
        self.label_editora.setObjectName("label_editora")
        self.lineEdit_Senha = QtWidgets.QLineEdit(Dialog_Nome)
        self.lineEdit_Senha.setGeometry(QtCore.QRect(330, 334, 290, 25))
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.lineEdit_Nome = QtWidgets.QLineEdit(Dialog_Nome)
        self.lineEdit_Nome.setGeometry(QtCore.QRect(330, 169, 290, 25))
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        self.lineEdit_CPF = QtWidgets.QLineEdit(Dialog_Nome)
        self.lineEdit_CPF.setGeometry(QtCore.QRect(330, 223, 290, 25))
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.label = QtWidgets.QLabel(Dialog_Nome)
        self.label.setGeometry(QtCore.QRect(350, 90, 290, 38))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_Nome)
        self.label_2.setGeometry(QtCore.QRect(330, 254, 290, 17))
        self.label_2.setObjectName("label_2")
        self.label_titulo = QtWidgets.QLabel(Dialog_Nome)
        self.label_titulo.setGeometry(QtCore.QRect(330, 146, 290, 17))
        self.label_titulo.setObjectName("label_titulo")
        self.label_4 = QtWidgets.QLabel(Dialog_Nome)
        self.label_4.setGeometry(QtCore.QRect(330, 308, 290, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton_Logo = QtWidgets.QPushButton(Dialog_Nome)
        self.pushButton_Logo.setGeometry(QtCore.QRect(30, 40, 290, 128))
        self.pushButton_Logo.setStyleSheet("QPushButton{\n"
"border: None;\n"
"}")
        self.pushButton_Logo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_Logo.setIcon(icon2)
        self.pushButton_Logo.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_Logo.setObjectName("pushButton_Logo")
        self.pushButton_Excluir = QtWidgets.QPushButton(Dialog_Nome)
        self.pushButton_Excluir.setGeometry(QtCore.QRect(544, 396, 80, 25))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("Icon/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_Excluir.setIcon(icon3)
        self.pushButton_Excluir.setObjectName("pushButton_Excluir")

        self.retranslateUi(Dialog_Nome)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Nome)

    def retranslateUi(self, Dialog_Nome):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Nome.setWindowTitle(_translate("Dialog_Nome", "Dialog"))
        self.pushButton_alterar.setText(_translate("Dialog_Nome", "Confirmar"))
        self.pushButton_cancelar.setText(_translate("Dialog_Nome", "Cancelar"))
        self.label_editora.setText(_translate("Dialog_Nome", "CPF"))
        self.label.setText(_translate("Dialog_Nome", "Editar Cadastro"))
        self.label_2.setText(_translate("Dialog_Nome", "Login"))
        self.label_titulo.setText(_translate("Dialog_Nome", "Nome"))
        self.label_4.setText(_translate("Dialog_Nome", "Senha"))
        self.pushButton_Excluir.setText(_translate("Dialog_Nome", "Excluir"))
