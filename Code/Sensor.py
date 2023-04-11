"""
_____________________ Sensor Simulator: _______________________

This program simulate the sensor by user's input for testing purpose.
When a mountain lion is detected, an alarm is trigger. Only ranger with correct id
can turn it off, and classify the alert. After that, the alert information is passed
to the database.

"""
import db_operations


def Triggered():
    valid_words = ["lion", "Lion", "LION"]
    valid_loc = ["1001", "1002", "1003", "1004"]

    print("Sensor information")
    while True:
        animal_type = input("Animal type: ")
        while True:
            try:
                noise = int(input("Strength of noise: "))
                break
            except:
                print("Please enter a number")
        loc = input("Location of noise sent (1001-1004): ")
        if animal_type.lower() in valid_words and noise > 3 and loc.lower() in valid_loc:
            print("Lion detected!")
            # Create a sound file
            ranger_id = Alarm()
            evaluation = RangerEvaluation()
            print(evaluation, loc, ranger_id)
            db_operations.insert(evaluation, loc, ranger_id)
            break
        else:
            print("Cannot trigger sensor.")


def Alarm():
    print()
    print("Alarm: On")

    valid_ranger_ids = ["1213", "1415", "1617", "1819"]
    while True:
        ranger_id = input("Enter your id number: ")
        if ranger_id.lower() in valid_ranger_ids:
            val = input("Turn off alarm (y): ")
            while val != 'y':
                print("Alarm: On")
                val = input("Turn off alert (y): ")
            print("Alarm: Off")
            return ranger_id
        else:
            print("Invalid id number.")


def RangerEvaluation():
    print()
    valid_words = ["definite", "suspected", "false"]
    while True:
        evaluation = input("Evaluate (definite|suspected|false): ")
        if evaluation.lower() in valid_words:
            break
        else:
            print("Invalid input. Please try again.")
    if evaluation == "false":
        print("No mountain lion detected.")
    elif evaluation == "definite":
        print("Mountain lion detected confirmed.")
    else:
        print("Further evaluation needed.")
    return evaluation
