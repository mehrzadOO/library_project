from pl.form import login
from tkinter import *
# from be.db import dbContext


if __name__=="__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (600, 400, 520, 200))
    screen.title("Library")
    screen.resizable(False, False)
    PageMe = login.App(screen)
    screen.mainloop()