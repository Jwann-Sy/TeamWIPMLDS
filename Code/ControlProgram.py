def RangerEvaluation(animal_type, noise, loc):
    print()
    print(animal_type, noise, loc)
    evaluation = input("Evaluate (definite|suspected|false): ")
    if evaluation == "false":
        print("No mountain lion detected.")
    elif evaluation == "definite":
        print("Mountain lion detected confirmed.")
    elif evaluation == "suspected":
        print("Further evaluation needed.")
    else:
        evaluation = "no"
    return animal_type, noise, loc, evaluation


def Request(animal_type, noise, loc):
    print()
    print("Evaluate (1)")
    print("Request report (2)")
    print("Request graphical report (3)")
    print("Exit: 0")
    action = int(input("action key: "))
    if action == 1:
        RangerEvaluation(animal_type, noise, loc)
        Request(animal_type, noise, loc)
    elif action == 0:
        return
    else:
        Request(animal_type, noise, loc)
