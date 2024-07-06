from pl.form import signup
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pydoc


screen = Tk()
screen.geometry("%dx%d+%d+%d" % (600, 400, 620, 300))
screen.resizable(False, False)
PageMe = signup.App(screen)
screen.mainloop()