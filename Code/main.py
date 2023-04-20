from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from reportwindow2 import Ui_reports_window
from editentrywindow import Ui_edit_entry_window
class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui.ui", self)
        self.show()
        self.login_button.clicked.connect(self.login)
        self.actionClose.triggered.connect(exit)
        self.show_report_button.clicked.connect(self.openReportWindow)
        self.edit_entries_button.clicked.connect(self.openEditEntryWindow)

    def openReportWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_reports_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openEditEntryWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_entry_window()
        self.ui.setupUi(self.window)
        self.window.show()

     

    def login(self):
        if self.username_edit.text() == "SDranger1" and self.password_edit.text() == "aztecs123":
            self.show_report_button.setEnabled(True)
            self.edit_entries_button.setEnabled(True)
            self.show_alerts_button.setEnabled(True)
            self.open_library_button.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid login")
            message.exec_()
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
if __name__ == '__main__':
    main()