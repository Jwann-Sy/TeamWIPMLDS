# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mygui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from reportwindow2 import Ui_reports_window
class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_reports_window()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(220, 30, 60, 16))
        self.password_label.setObjectName("password_label")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(280, 30, 113, 22))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(410, 30, 81, 26))
        self.login_button.setObjectName("login_button")
        self.show_alerts_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_alerts_button.setEnabled(False)
        self.show_alerts_button.setGeometry(QtCore.QRect(60, 150, 141, 26))
        self.show_alerts_button.setObjectName("show_alerts_button")
        self.open_library_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_library_button.setEnabled(False)
        self.open_library_button.setGeometry(QtCore.QRect(60, 190, 141, 26))
        self.open_library_button.setObjectName("open_library_button")
        self.show_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_report_button.setEnabled(False)
        self.show_report_button.setGeometry(QtCore.QRect(60, 70, 141, 26))
        self.show_report_button.setObjectName("show_report_button")

        self.show_report_button.clicked.connect(self.openWindow)

        self.edit_entries_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_entries_button.setEnabled(False)
        self.edit_entries_button.setGeometry(QtCore.QRect(60, 110, 141, 26))
        self.edit_entries_button.setObjectName("edit_entries_button")
        self.show_reports_label = QtWidgets.QLabel(self.centralwidget)
        self.show_reports_label.setGeometry(QtCore.QRect(230, 70, 181, 21))
        self.show_reports_label.setObjectName("show_reports_label")
        self.edit_entries_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_entries_label.setGeometry(QtCore.QRect(230, 110, 181, 21))
        self.edit_entries_label.setObjectName("edit_entries_label")
        self.show_alerts_label = QtWidgets.QLabel(self.centralwidget)
        self.show_alerts_label.setGeometry(QtCore.QRect(230, 150, 251, 31))
        self.show_alerts_label.setObjectName("show_alerts_label")
        self.open_library_label = QtWidgets.QLabel(self.centralwidget)
        self.open_library_label.setGeometry(QtCore.QRect(230, 190, 181, 21))
        self.open_library_label.setObjectName("open_library_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username "))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.show_alerts_button.setText(_translate("MainWindow", "Show Alerts"))
        self.open_library_button.setText(_translate("MainWindow", "Open Library"))
        self.show_report_button.setText(_translate("MainWindow", "Show Reports"))
        self.edit_entries_button.setText(_translate("MainWindow", "Edit Entries"))
        self.show_reports_label.setText(_translate("MainWindow", "Displays database reports"))
        self.edit_entries_label.setText(_translate("MainWindow", "Edit an entry by file name"))
        self.show_alerts_label.setText(_translate("MainWindow", "Displays alerts that need a classification"))
        self.open_library_label.setText(_translate("MainWindow", "Goes to audio file directory"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
