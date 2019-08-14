# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adm_livros.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 550)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, -10, 181, 171))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: None;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(128, 128))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 50, 341, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_buscar = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_buscar.setGeometry(QtCore.QRect(320, 160, 190, 25))
        self.lineEdit_buscar.setObjectName("lineEdit_buscar")
        self.pushButton_buscar = QtWidgets.QPushButton(Dialog)
        self.pushButton_buscar.setGeometry(QtCore.QRect(530, 160, 80, 25))
        self.pushButton_buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Icon/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_buscar.setIcon(icon1)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.textBrowser_info = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_info.setGeometry(QtCore.QRect(220, 240, 520, 190))
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.pushButton_editar = QtWidgets.QPushButton(Dialog)
        self.pushButton_editar.setGeometry(QtCore.QRect(320, 460, 80, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/edit-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_editar.setIcon(icon2)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_adicionar = QtWidgets.QPushButton(Dialog)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(530, 460, 91, 25))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/addition-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_adicionar.setIcon(icon3)
        self.pushButton_adicionar.setObjectName("pushButton_adicionar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Administrar livros"))
        self.pushButton_editar.setText(_translate("Dialog", "Editar"))
        self.pushButton_adicionar.setText(_translate("Dialog", "Adicionar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

