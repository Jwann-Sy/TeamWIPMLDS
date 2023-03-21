def Request():
    print()
    print("Request report (1)")
    print("Request graphical report (2)")
    print("Exit (0)")
    action = input("Enter an action key: ")
    if action == "1":
        ShowReport()
    elif action == "2":
        ShowGraphicReport()
    elif action == "0":
        return
    else:
        Request()


def ShowReport():
    print()
    print("Show all mountain lion detections by date detected and by classification (1)")
    print("Show all mountain lion detections at a specific sensor location (2)")
    print("Show detection classifications by ranger (3)")
    print("Return (0)")
    # ensure users enter an integer
    report = int(input("Enter an action key: "))

    if report == 1:
        sort = input("(date|classification)")
        if sort == "date":
            ShowByDate()
        elif sort == "classification":
            ShowByClass()
    elif report == 2:
        ShowSpecLoc()
    elif report == 0:
        Request()
    else:
        ShowReport()


def ShowGraphicReport():
    return


def ShowByDate():
    return


def ShowByClass():
    return


def ShowSpecLoc():
    return


def ShowDetectionClass():
    return
