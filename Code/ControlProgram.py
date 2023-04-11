import db_reports as db


def Request():
    print()
    print("Request report (1)")
    print("Request graphical report (2)")
    print("Exit (0)")
    while True:
        try:
            action = int(input("Enter an action key: "))
            break
        except:
            print("Please enter a number")

    if action == 1:
        ShowReport()
    elif action == 2:
        ShowGraphicReport()
    elif action == 0:
        print()
        return
    else:
        Request()


def ShowReport():
    print()
    print("Show all mountain lion detections within 30 days (1)")
    print("Show summary of alerts older than 30 days (2)")
    print("Show all mountain lion detections at a specific sensor location (3)")
    print("Show detection classifications by ranger (4)")
    print("Return (0)")
    while True:
        try:
            report = int(input("Enter an action key: "))
            print()
            break
        except:
            print("Please enter a number")

    if report == 1:
        ShowRecent()
    elif report == 2:
        ShowSum()
    elif report == 3:
        ShowByLoc()
    elif report == 4:
        ShowByClass()
    elif report == 0:
        Request()
    else:
        print("Please enter a number from 0 to 3")
        ShowReport()


def ShowGraphicReport():
    BackToReport()


def ShowRecent():
    print("Alerts within 30 days:")
    db.report_1()
    BackToReport()


def ShowSum():
    db.report_2()
    BackToReport()


def ShowByLoc():
    valid_loc = ["1001", "1002", "1003", "1004"]
    while True:
        location = input("Sensor location (1001-1004):  ")
        if location.lower() in valid_loc:
            break
        else:
            print("Invalid location. Please try again.")
    db.report_5(location)
    BackToReport()


def ShowByClass():
    valid_words = ["definite", "suspected", "false"]
    while True:
        classification = input("Classification definite|suspected|false: ")
        if classification.lower() in valid_words:
            break
        else:
            print("Invalid classification. Please try again.")
    db.report_4(classification)
    BackToReport()


def BackToReport():
    key = input("Enter any key to go back: ")
    if key is not None:
        ShowReport()
