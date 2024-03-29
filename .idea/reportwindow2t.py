# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/johngill/PycharmProjects/pythonProject2/reportwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reports_window(object):
    def setupUi(self, reports_window):
        reports_window.setObjectName("reports_window")
        reports_window.resize(1440, 760)
        self.centralwidget = QtWidgets.QWidget(reports_window)
        self.centralwidget.setObjectName("centralwidget")
        self.days_entries_button = QtWidgets.QPushButton(self.centralwidget)
        self.days_entries_button.setGeometry(QtCore.QRect(20, 100, 131, 26))
        self.days_entries_button.setObjectName("days_entries_button")
        self.entries_by_date_button = QtWidgets.QPushButton(self.centralwidget)
        self.entries_by_date_button.setGeometry(QtCore.QRect(20, 130, 131, 26))
        self.entries_by_date_button.setObjectName("entries_by_date_button")
        self.graphicalreport_button = QtWidgets.QPushButton(self.centralwidget)
        self.graphicalreport_button.setGeometry(QtCore.QRect(20, 160, 131, 26))
        self.graphicalreport_button.setObjectName("graphicalreport_button")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(40, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.classification_label = QtWidgets.QLabel(self.centralwidget)
        self.classification_label.setGeometry(QtCore.QRect(20, 230, 201, 16))
        self.classification_label.setObjectName("classification_label")
        self.class_defo_button = QtWidgets.QPushButton(self.centralwidget)
        self.class_defo_button.setGeometry(QtCore.QRect(20, 260, 131, 26))
        self.class_defo_button.setObjectName("class_defo_button")
        self.class_sus_button = QtWidgets.QPushButton(self.centralwidget)
        self.class_sus_button.setGeometry(QtCore.QRect(180, 260, 131, 26))
        self.class_sus_button.setObjectName("class_sus_button")
        self.class_false_button = QtWidgets.QPushButton(self.centralwidget)
        self.class_false_button.setGeometry(QtCore.QRect(340, 260, 131, 26))
        self.class_false_button.setObjectName("class_false_button")
        self.sensor_entries_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_entries_label.setGeometry(QtCore.QRect(20, 330, 201, 16))
        self.sensor_entries_label.setObjectName("sensor_entries_label")
        self.sensor_id_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_id_label.setGeometry(QtCore.QRect(20, 360, 101, 16))
        self.sensor_id_label.setObjectName("sensor_id_label")
        self.sensor_id_text = QtWidgets.QLineEdit(self.centralwidget)
        self.sensor_id_text.setGeometry(QtCore.QRect(140, 360, 181, 22))
        self.sensor_id_text.setAutoFillBackground(False)
        self.sensor_id_text.setObjectName("sensor_id_text")
        self.sensorid_enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.sensorid_enter_button.setGeometry(QtCore.QRect(340, 360, 81, 26))
        self.sensorid_enter_button.setObjectName("sensorid_enter_button")
        self.entries_by_ranger_label = QtWidgets.QLabel(self.centralwidget)
        self.entries_by_ranger_label.setGeometry(QtCore.QRect(20, 410, 201, 16))
        self.entries_by_ranger_label.setObjectName("entries_by_ranger_label")
        self.rangerid_label = QtWidgets.QLabel(self.centralwidget)
        self.rangerid_label.setGeometry(QtCore.QRect(20, 440, 101, 16))
        self.rangerid_label.setObjectName("rangerid_label")
        self.rangerid_text = QtWidgets.QLineEdit(self.centralwidget)
        self.rangerid_text.setGeometry(QtCore.QRect(140, 440, 181, 22))
        self.rangerid_text.setAutoFillBackground(False)
        self.rangerid_text.setObjectName("rangerid_text")
        self.rangerid_enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.rangerid_enter_button.setGeometry(QtCore.QRect(340, 440, 81, 26))
        self.rangerid_enter_button.setObjectName("rangerid_enter_button")
        self.month_to_year_button = QtWidgets.QPushButton(self.centralwidget)
        self.month_to_year_button.setGeometry(QtCore.QRect(20, 190, 131, 26))
        self.month_to_year_button.setObjectName("month_to_year_button")
        reports_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reports_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        reports_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(reports_window)
        self.statusbar.setObjectName("statusbar")
        reports_window.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(reports_window)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(reports_window)
        QtCore.QMetaObject.connectSlotsByName(reports_window)

    def retranslateUi(self, reports_window):
        _translate = QtCore.QCoreApplication.translate
        reports_window.setWindowTitle(_translate("reports_window", "MainWindow"))
        self.days_entries_button.setText(_translate("reports_window", "30 Day Entries"))
        self.entries_by_date_button.setText(_translate("reports_window", "All Entries by date"))
        self.graphicalreport_button.setText(_translate("reports_window", "Graphical Report"))
        self.main_label.setText(_translate("reports_window", "REPORTS"))
        self.classification_label.setText(_translate("reports_window", "Display entries by classification"))
        self.class_defo_button.setText(_translate("reports_window", "Definite"))
        self.class_sus_button.setText(_translate("reports_window", "Suspected"))
        self.class_false_button.setText(_translate("reports_window", "False"))
        self.sensor_entries_label.setText(_translate("reports_window", "Display entries by sensor"))
        self.sensor_id_label.setText(_translate("reports_window", "enter sensor id:"))
        self.sensorid_enter_button.setText(_translate("reports_window", "enter"))
        self.entries_by_ranger_label.setText(_translate("reports_window", "Display entries by ranger"))
        self.rangerid_label.setText(_translate("reports_window", "enter ranger id:"))
        self.rangerid_enter_button.setText(_translate("reports_window", "enter"))
        self.month_to_year_button.setText(_translate("reports_window", "Month to Year"))
        self.menuFile.setTitle(_translate("reports_window", "File"))
        self.actionClose.setText(_translate("reports_window", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reports_window = QtWidgets.QMainWindow()
    ui = Ui_reports_window()
    ui.setupUi(reports_window)
    reports_window.show()
    sys.exit(app.exec_())
