def Triggered():
    print("Sensor information")
    animal_type = input("Animal type: ")
    noise = int(input("Strength of noise: "))
    loc = int(input("Location of noise sent: "))
    if animal_type == "Lion" or animal_type == "lion":
        print("Lion detected!")
        Alarm()
    else:
        print("Not a lion")
        Triggered()
    return animal_type, noise, loc


def Alarm():
    print("Alarm: On")
    val = input("Turn off alarm (y): ")
    while val != 'y':
        val = input("Turn off alert (y): ")
    print("Alarm: Off")



