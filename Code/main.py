import Sensor
import ControlProgram
import db_operations


def main():
    while True:
        Sensor.Triggered()
        ControlProgram.Request()


if __name__ == "__main__":
    main()
