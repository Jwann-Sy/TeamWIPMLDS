import sys
import random

from PyQt5.QtWidgets import QMessageBox

from db_operations import insert
from PyQt5 import QtWidgets, QtGui, QtCore

SensorID = 0
RangerID = 0
Submitted = False


def Triggered():
    global SensorID
    SensorID = random.randint(1001, 1004)
    return SensorID


class AlarmWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm")
        self.setGeometry(100, 100, 400, 300)

        # create label for sensor id
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, 200, 30))

        # create input text for ranger id
        self.ranger_id_label = QtWidgets.QLabel(self)
        self.ranger_id_label.setGeometry(QtCore.QRect(50, 70, 100, 30))
        self.ranger_id_label.setText("Ranger ID:")
        self.ranger_id_input = QtWidgets.QLineEdit(self)
        self.ranger_id_input.setGeometry(120, 75, 100, 20)
        self.ranger_id_input.textChanged.connect(self.handle_ranger_id_input)

        # create radio button group
        self.radio_group = QtWidgets.QGroupBox(self)
        self.radio_group.setGeometry(50, 120, 300, 70)
        self.radio_group.setTitle('Evaluation')

        self.suspected_radio = QtWidgets.QRadioButton('Suspected', self.radio_group)
        self.suspected_radio.setGeometry(20, 30, 100, 30)
        self.suspected_radio.toggled.connect(self.enable_turn_off)

        self.false_radio = QtWidgets.QRadioButton('False', self.radio_group)
        self.false_radio.setGeometry(120, 30, 100, 30)
        self.false_radio.toggled.connect(self.enable_turn_off)

        self.definite_radio = QtWidgets.QRadioButton('Definite', self.radio_group)
        self.definite_radio.setGeometry(220, 30, 100, 30)
        self.definite_radio.toggled.connect(self.enable_turn_off)

        # self.radio_group.buttonClicked.connect(self.handle_turn_off)

        # create turn off button
        self.turn_off_button = QtWidgets.QPushButton('Turn Off', self)
        self.turn_off_button.setGeometry(150, 250, 100, 20)
        self.turn_off_button.clicked.connect(self.handle_turn_off)

        self.radio_group.setEnabled(False)
        self.turn_off_button.setEnabled(False)

        self.triggered_number = None
        self.start_trigger()

    def start_trigger(self):
        self.triggered_number = None
        self.label.setText("Waiting for Triggered number...")
        QtCore.QTimer.singleShot(0, self.trigger)

    def trigger(self):
        self.triggered_number = Triggered()
        self.label.setText(f"Sensor ID: {self.triggered_number}")

    def handle_ranger_id_input(self):
        global RangerID
        valid_ranger_ids = ["1213", "1415", "1617"]
        ranger_id = self.ranger_id_input.text()
        if ranger_id in valid_ranger_ids:
            RangerID = ranger_id
            self.radio_group.setEnabled(True)
        else:
            self.radio_group.setEnabled(False)
            QMessageBox.information(self, "Error", "Invalid ranger ID")

    def enable_turn_off(self):
        if self.suspected_radio.isChecked() or self.false_radio.isChecked() or self.definite_radio.isChecked():
            self.turn_off_button.setEnabled(True)

    def handle_turn_off(self):
        global SensorID
        global RangerID
        global Submitted
        if self.suspected_radio.isChecked():
            insert("suspected", SensorID, RangerID)
        elif self.false_radio.isChecked():
            insert("false", SensorID, RangerID)
        elif self.definite_radio.isChecked():
            insert("definite", SensorID, RangerID)
        Submitted = True

    def closeEvent(self, evnt):
        global Submitted
        if Submitted:
            super(AlarmWindow, self).closeEvent(evnt)
        else:
            evnt.ignore()
            self.setWindowState(QtCore.Qt.WindowMinimized)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AlarmWindow()
    window.show()
    sys.exit(app.exec_())
