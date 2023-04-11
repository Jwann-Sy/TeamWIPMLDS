def Triggered():
    print("Sensor information")
    animal_type = input("Animal type: ")
    # ensure noise and loc entered are integers
    noise = int(input("Strength of noise: "))
    loc = int(input("Location of noise sent (1-4): "))
    if animal_type == "Lion" or animal_type == "lion":
        print("Lion detected!")
        # Create a sound file
        Alarm()
        evaluation = RangerEvaluation()
        # insert this new alert info to the database
        print(animal_type, noise, loc, evaluation)
        return animal_type, noise, loc, evaluation
    else:
        print("Not a lion")
        Triggered()


def Alarm():
    print()
    print("Alarm: On")
    val = input("Turn off alarm (y): ")
    while val != 'y':
        val = input("Turn off alert (y): ")
    print("Alarm: Off")


def RangerEvaluation():
    print()
    evaluation = input("Evaluate (definite|suspected|false): ")
    if evaluation == "false":
        print("No mountain lion detected.")
    elif evaluation == "definite":
        print("Mountain lion detected confirmed.")
    elif evaluation == "suspected":
        print("Further evaluation needed.")
    else:
        print("Error.")
        RangerEvaluation()
    return evaluation
