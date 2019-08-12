# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrar_livro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(900, 550)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_autor = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.gridLayout.addWidget(self.lineEdit_autor, 16, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 18, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 2, 1, 1)
        self.label_titulo = QtWidgets.QLabel(Dialog)
        self.label_titulo.setObjectName("label_titulo")
        self.gridLayout.addWidget(self.label_titulo, 3, 2, 1, 1)
        self.lineEdit_ano = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ano.setObjectName("lineEdit_ano")
        self.gridLayout.addWidget(self.lineEdit_ano, 10, 2, 1, 1)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.gridLayout.addWidget(self.lineEdit_ISBN, 8, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 19, 2, 1, 1)
        self.lineEdit_descricao = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_descricao.setObjectName("lineEdit_descricao")
        self.gridLayout.addWidget(self.lineEdit_descricao, 14, 2, 1, 1)
        self.label_editora = QtWidgets.QLabel(Dialog)
        self.label_editora.setObjectName("label_editora")
        self.gridLayout.addWidget(self.label_editora, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 17, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border: None;\n"
"}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("PiltoverLibrary/Icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 5, 1)
        self.lineEdit_titulo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.gridLayout.addWidget(self.lineEdit_titulo, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 2, 1, 1)
        self.lineEdit_editora = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_editora.setObjectName("lineEdit_editora")
        self.gridLayout.addWidget(self.lineEdit_editora, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 9, 3, 1, 1)
        self.lineEdit_Genero = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Genero.setObjectName("lineEdit_Genero")
        self.gridLayout.addWidget(self.lineEdit_Genero, 12, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 15, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Cadastrar-se"))
        self.label_4.setText(_translate("Dialog", "Ano"))
        self.label_titulo.setText(_translate("Dialog", "Título"))
        self.pushButton.setText(_translate("Dialog", "Cancelar"))
        self.label_editora.setText(_translate("Dialog", "Editora"))
        self.label_2.setText(_translate("Dialog", "ISBN"))
        self.label_6.setText(_translate("Dialog", "Descrição"))
        self.label_5.setText(_translate("Dialog", "Gênero"))
        self.label_7.setText(_translate("Dialog", "Autor"))
        self.label.setText(_translate("Dialog", "Cadastrar livro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

