# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 380)
        MainWindow.setMinimumSize(QtCore.QSize(591, 380))
        MainWindow.setMaximumSize(QtCore.QSize(591, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_widget = QtWidgets.QWidget(self.centralwidget)
        self.welcome_widget.setGeometry(QtCore.QRect(0, 0, 600, 481))
        self.welcome_widget.setMinimumSize(QtCore.QSize(600, 481))
        self.welcome_widget.setMaximumSize(QtCore.QSize(600, 481))
        self.welcome_widget.setStyleSheet("QWidget#welcome_widget{\n"
"background-color: qlineargradient(spread:pad, x1:0.095, y1:0.130545, x2:0.965, y2:0.938, stop:0 rgba(170, 85, 127, 255), stop:1 rgba(255, 255, 0, 255));}")
        self.welcome_widget.setObjectName("welcome_widget")
        self.welcome_label = QtWidgets.QLabel(self.welcome_widget)
        self.welcome_label.setGeometry(QtCore.QRect(200, 50, 221, 41))
        self.welcome_label.setStyleSheet("font: 25pt \"Felix Titling\"; color: rgb(255, 255, 255)")
        self.welcome_label.setObjectName("welcome_label")
        self.sign_in_label = QtWidgets.QLabel(self.welcome_widget)
        self.sign_in_label.setEnabled(True)
        self.sign_in_label.setGeometry(QtCore.QRect(260, 110, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_in_label.sizePolicy().hasHeightForWidth())
        self.sign_in_label.setSizePolicy(sizePolicy)
        self.sign_in_label.setStyleSheet("font: 15pt \"Felix Titling\"; color: rgb(255, 255, 255)")
        self.sign_in_label.setObjectName("sign_in_label")
        self.username_label = QtWidgets.QLabel(self.welcome_widget)
        self.username_label.setGeometry(QtCore.QRect(140, 180, 111, 21))
        self.username_label.setStyleSheet("color : rgb(255, 255, 255) ; \n"
"font: 10pt \"Felix Titling\";")
        self.username_label.setObjectName("username_label")
        self.login_button = QtWidgets.QPushButton(self.welcome_widget)
        self.login_button.setGeometry(QtCore.QRect(340, 250, 131, 41))
        self.login_button.setStyleSheet("font: 8pt \"Felix Titling\";")
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(self.welcome_widget)
        self.signup_button.setGeometry(QtCore.QRect(150, 250, 131, 41))
        self.signup_button.setStyleSheet("font: 8pt \"Felix Titling\";")
        self.signup_button.setObjectName("signup_button")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.welcome_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 180, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome"))
        self.sign_in_label.setText(_translate("MainWindow", "Sign In"))
        self.username_label.setText(_translate("MainWindow", "User Name : "))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.signup_button.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())