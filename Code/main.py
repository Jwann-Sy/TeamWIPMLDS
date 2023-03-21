import Sensor
import ControlProgram


def main():
    animal_type, noise, loc, evaluation = Sensor.Triggered()
    ControlProgram.Request()


if __name__ == "__main__":
    main()
