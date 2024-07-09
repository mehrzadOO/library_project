from pl.form import library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pydoc


screen = Tk()
screen.geometry("%dx%d+%d+%d" % (1000, 500, 600, 300))
screen.resizable(False, False)
PageMe = library.App(screen)
screen.mainloop()