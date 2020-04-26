# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 405)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(10, 20, 401, 33))
        self.numberEdit.setObjectName("numberEdit")
        self.numberEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit_2.setGeometry(QtCore.QRect(10, 80, 401, 31))
        self.numberEdit_2.setObjectName("numberEdit_2")
        self.plusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plusBtn.setGeometry(QtCore.QRect(10, 140, 91, 41))
        self.plusBtn.setObjectName("plusBtn")
        self.minusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.minusBtn.setGeometry(QtCore.QRect(120, 140, 91, 41))
        self.minusBtn.setObjectName("minusBtn")
        self.divBtn = QtWidgets.QPushButton(self.centralwidget)
        self.divBtn.setGeometry(QtCore.QRect(230, 140, 91, 41))
        self.divBtn.setObjectName("divBtn")
        self.mulBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mulBtn.setGeometry(QtCore.QRect(330, 140, 91, 41))
        self.mulBtn.setObjectName("mulBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 220, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plusBtn.clicked.connect(self.Plus)

        self.minusBtn.clicked.connect(self.Minus)

        self.divBtn.clicked.connect(self.Div)

        self.mulBtn.clicked.connect(self.Multi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Python Calculator For Beginners")
        self.numberEdit.setText(_translate("MainWindow", "0"))
        self.numberEdit.setPlaceholderText(_translate("MainWindow", "Number"))
        self.numberEdit_2.setText(_translate("MainWindow", "0"))
        self.numberEdit_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.plusBtn.setText(_translate("MainWindow", "+"))
        self.minusBtn.setText(_translate("MainWindow", "-"))
        self.divBtn.setText(_translate("MainWindow", "/"))
        self.mulBtn.setText(_translate("MainWindow", "*"))
    
    def Plus(self):
        self.result = int(self.numberEdit.text()) + int(self.numberEdit_2.text())
        self.label.setText(str(self.result))

    def Minus(self):
        self.result = int(self.numberEdit.text()) - int(self.numberEdit_2.text())
        self.label.setText(str(self.result))

    def Div(self):
        self.result = float(self.numberEdit.text()) / float(self.numberEdit_2.text())
        self.label.setText(str(self.result))

    def Multi(self):
        self.result = int(self.numberEdit.text()) * int(self.numberEdit_2.text())
        self.label.setText(str(self.result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
