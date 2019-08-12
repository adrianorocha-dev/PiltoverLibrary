# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setEnabled(True)
        self.listView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listView.setLineWidth(1)
        self.listView.setMidLineWidth(-1)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAuthors = QtWidgets.QMenu(self.menubar)
        self.menuAuthors.setObjectName("menuAuthors")
        MainWindow.setMenuBar(self.menubar)
        self.menu_file_newbook = QtWidgets.QAction(MainWindow)
        self.menu_file_newbook.setObjectName("menu_file_newbook")
        self.menu_view_listbook = QtWidgets.QAction(MainWindow)
        self.menu_view_listbook.setObjectName("menu_view_listbook")
        self.menu_view_listauthor = QtWidgets.QAction(MainWindow)
        self.menu_view_listauthor.setObjectName("menu_view_listauthor")
        self.menu_file_newauthor = QtWidgets.QAction(MainWindow)
        self.menu_file_newauthor.setObjectName("menu_file_newauthor")
        self.menuFile.addAction(self.menu_file_newbook)
        self.menuFile.addAction(self.menu_file_newauthor)
        self.menuAuthors.addAction(self.menu_view_listbook)
        self.menuAuthors.addAction(self.menu_view_listauthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAuthors.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        itemModel = QtGui.QStandardItemModel(self.listView)

        item = QtGui.QStandardItem('Potato')
        itemModel.appendRow((item))

        self.listView.setModel(itemModel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Piltover Library"))
        self.label.setText(_translate("MainWindow", "Books List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAuthors.setTitle(_translate("MainWindow", "View"))
        self.menu_file_newbook.setText(_translate("MainWindow", "New Book"))
        self.menu_file_newbook.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.menu_view_listbook.setText(_translate("MainWindow", "Books list"))
        self.menu_view_listbook.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.menu_view_listauthor.setText(_translate("MainWindow", "Authors list"))
        self.menu_view_listauthor.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.menu_file_newauthor.setText(_translate("MainWindow", "New Author"))
        self.menu_file_newauthor.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
