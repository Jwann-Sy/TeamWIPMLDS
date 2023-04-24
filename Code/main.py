from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, Qt
import sys
import random

import db_reports
from reportwindow2 import Ui_reports_window
from editentrywindow import Ui_edit_entry_window
import Alarm


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui.ui", self)
        self.show()
        self.login_button.clicked.connect(self.login)
        self.actionClose.triggered.connect(exit)
        self.show_report_button.clicked.connect(self.openReportWindow)
        self.edit_entries_button.clicked.connect(self.openEditEntryWindow)
        self.show_alerts_button.clicked.connect(self.openAlarm)

        # disable alarm button for a random time between 30 and 60 seconds
        self.disable_alarm_button(random.randint(30000, 40000))

    def disable_alarm_button(self, time):
        self.show_alerts_button.setDisabled(True)
        QtCore.QTimer.singleShot(time, lambda: self.show_alerts_button.setDisabled(False))

    def openReportWindow(self):
        self.openReportWindow = ReportGUI()

    def openEditEntryWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_entry_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        if self.username_edit.text() == "SDranger1" and self.password_edit.text() == "aztecs123":
            self.show_report_button.setEnabled(True)
            self.edit_entries_button.setEnabled(True)
            self.open_library_button.setEnabled(True)
        else:
            QMessageBox.information(self, "Error", "Invalid login")

    def openAlarm(self):
        self.window = Alarm.AlarmWindow()
        self.window.show()
        self.show_alerts_button.setDisabled(True)


class ReportGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(ReportGUI, self).__init__()
        self.ui = Ui_reports_window()
        self.ui.setupUi(self)
        self.show()
        self.ui.days_entries_button.clicked.connect(self.daysEntriesReport)
        self.ui.entries_by_date_button.clicked.connect(self.entriesByDateReport)
        self.ui.class_defo_button.clicked.connect(self.classDefoReport)
        self.ui.class_sus_button.clicked.connect(self.classSusReport)
        self.ui.class_false_button.clicked.connect(self.classFalseReport)
        self.ui.sensorid_enter_button.clicked.connect(self.sensorIDReport)
        self.ui.rangerid_enter_button.clicked.connect(self.rangerIDReport)

    def daysEntriesReport(self):
        printReport(db_reports.report_1())

    def entriesByDateReport(self):
        printReport(db_reports.report_3())

    def classDefoReport(self):
        printReport(db_reports.report_4("definite"))

    def classSusReport(self):
        printReport(db_reports.report_4("suspected"))

    def classFalseReport(self):
        printReport(db_reports.report_4("false"))

    def sensorIDReport(self):
        valid_senor_ids = ["1001", "1002", "1003", "1004"]
        sensor_id = self.ui.sensor_id_text.text()
        if sensor_id in valid_senor_ids:
            printReport(db_reports.report_5(sensor_id))
        else:
            QMessageBox.information(self, "Error", "Invalid ID")

    def rangerIDReport(self):
        valid_ranger_ids = ["1213", "1415", "1617", "1819"]
        ranger_id = self.ui.rangerid_text.text()
        if ranger_id in valid_ranger_ids:
            printReport(db_reports.report_6(ranger_id))
        else:
            QMessageBox.information(self, "Error", "Invalid ID")


def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    sys.exit(app.exec_())


def printReport(text):
    message = QMessageBox()
    message.setText(text)
    message.setStyleSheet("QLabel{min-width: 500px;}")
    message.exec_()


if __name__ == '__main__':
    main()
