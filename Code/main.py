import Sensor
import ControlProgram


def main():
    animal_type, noise, loc = Sensor.Triggered()
    ControlProgram.Request(animal_type, noise, loc)


if __name__ == "__main__":
    main()
