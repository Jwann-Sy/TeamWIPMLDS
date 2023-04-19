# ========== IMPORTS =====================
import tkinter as tk
from tkinter import ttk

import os

# Create instance of the tk class
win = tk.Tk()

# Title
win.title("Mountain Lion Detection System")

# =========== LABELS ====================

# Choose an option label
choose_option_label = ttk.Label(win, text="Choose an Option:")
choose_option_label.grid(column=0, row=0)

# Reports description label
reports_label = ttk.Label(win, text="Displays database reports.")
reports_label.grid(column=1, row=1)

# Library description label
lib_label = ttk.Label(win, text="Opens audio file directory.")
lib_label.grid(column=1, row=2)

# Alert description label

alert_label = ttk.Label(win, text="Displays alerts that need classification.")
alert_label.grid(column=1, row=3)

# Edit description label
edit_label = ttk.Label(win, text="Edit an entry by file name.")
edit_label.grid(column=1, row=4)


# =========== BUTTON DEFINITIONS ========
# Opens the sound file directory, given the path
def send_to_dir():
    os.startfile(r'C:\Users\spagh\Desktop\CS 532 Project\Sounds')


# =========== BUTTONS ==================
# Create reports button
rep_action = ttk.Button(win, text="Reports")
rep_action.grid(column=0, row=1)

# Create library button
lib_action = ttk.Button(win, text="Library", command=send_to_dir)
lib_action.grid(column=0, row=2)

# Create alerts button
alert_action = ttk.Button(win, text="Alerts")
alert_action.grid(column=0, row=3)

# Create edit button
edit_action = ttk.Button(win, text="Edit")
edit_action.grid(column=0, row=4)


# ================================
# START GUI
# ================================
win.mainloop()
