import os
from bll.blbook_human import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pydoc


class App(ttk.Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master = screen
        self.CreateWidget()

    def CreateWidget(self):
        style = ttk.Style()
        style.theme_use("vista")
        self.title_lable = ttk.Label(self.master, text="welcome to library", font="bold").pack()
        self.username = StringVar()
        self.username_label = ttk.Label(self.master, text="Username").place(x=275, y=70)
        self.username_box = ttk.Entry(style.master, textvariable=self.username).place(x=240, y=100)
        self.password = StringVar()
        self.password_label = ttk.Label(self.master, text="Password").place(x=275, y=140)
        self.password_box = ttk.Entry(style.master, textvariable=self.password).place(x=240, y=160)
        self.seach_btn = ttk.Button(self.master, text="Login", command=self.onclickseach).place(x=265, y=200)
        self.signup_btn = ttk.Button(self.master, text="signup", command=self.onclicksignup).place(x=265, y=240)


    def onclickseach(self):
        # res = login(self.username.get(), self.password.get())
        # if res:
        #     self.master.destroy()
        #     os.system(f"python pl/form/libraryM.py")
        self.master.destroy()
        os.system(f"python pl/form/libraryM.py")

    def onclicksignup(self):
        self.master.destroy()
        os.system(f"python pl/form/signupM.py")
