from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, Qt
import sys
import random

import db_reports
from db_operations import edit_classif
from reportwindow2 import Ui_reports_window
from editentrywindow import Ui_edit_entry_window
from graphical_report import sensor_data_to_list, graphical_report
from open_library import send_to_dir
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
        self.open_library_button.clicked.connect(self.openLibrary)

        # disable alarm button for a random time between 30 and 60 seconds
        self.disable_alarm_button(random.randint(30000, 40000))

    def disable_alarm_button(self, time):
        self.show_alerts_button.setDisabled(True)
        QtCore.QTimer.singleShot(time, lambda: self.show_alerts_button.setDisabled(False))

    def openReportWindow(self):
        self.openReportWindow = ReportGUI()

    def openEditEntryWindow(self):
        self.openEditEntryWindow = EditGUI()

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

    def openLibrary(self):
        send_to_dir()


class EditGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(EditGUI, self).__init__()
        self.ui = Ui_edit_entry_window()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.submitEdit)

    def submitEdit(self):
        valid_ranger_ids = ["1213", "1415", "1617"]
        valid_class = ["definite", "suspected", "false"]

        event = self.ui.lineEdit.text()
        ranger_id = self.ui.lineEdit_2.text()
        class_edit = self.ui.lineEdit_3.text()
        if ranger_id not in valid_ranger_ids:
            QMessageBox.information(self, "Error", "Invalid ranger ID.")
        if class_edit not in valid_class:
            QMessageBox.information(self, "Error", "Invalid classification.")
        if ranger_id in valid_ranger_ids and class_edit in valid_class:
            edit_classif(event, class_edit, ranger_id)
            self.close()


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
        self.ui.month_to_year_button.clicked.connect(self.monthToYearSum)
        self.ui.graphicalreport_button.clicked.connect(self.graphicalReport)

    def daysEntriesReport(self):
        printReport(db_reports.report_1())

    def monthToYearSum(self):
        printReport(db_reports.report_2())

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

    def rangerIDReport(self):
        valid_ranger_ids = ["1213", "1415", "1617", "1819"]
        ranger_id = self.ui.rangerid_text.text()
        if ranger_id in valid_ranger_ids:
            printReport(db_reports.report_6(ranger_id))

    def graphicalReport(self):
        longitude, latitude, sensor_count, sensor_month_count = sensor_data_to_list()
        graphical_report(longitude, latitude, sensor_count, sensor_month_count)


class ScrollMessageBox(QMessageBox):
    def __init__(self, text, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.content = QWidget()
        scroll.setWidget(self.content)
        lay = QVBoxLayout(self.content)
        for item in text.split('\n'):
            lay.addWidget(QLabel(item, self))
        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:500 px; min-height: 400px}")


def printReport(text):
    result = ScrollMessageBox(text, None)
    result.exec_()


def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
