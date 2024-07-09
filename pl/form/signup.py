import os
from tkinter import *
from tkinter import ttk
from bll.blbook_human import *
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

        self.signupPage_label = ttk.Label(self.master, text="Signup Page", font="bold").pack()
        self.name_label = ttk.Label(self.master, text="Nmae").pack()
        self.name = StringVar()
        self.name_box = ttk.Entry(self.master, textvariable=self.name).pack()
        self.family_label = ttk.Label(self.master, text="Family").pack()
        self.family = StringVar()
        self.family_box = ttk.Entry(self.master, textvariable=self.family).pack()
        self.username_label = ttk.Label(self.master, text="Username").pack()
        self.username = StringVar()
        self.username_box = ttk.Entry(self.master, textvariable=self.username).pack()
        self.password_label = ttk.Label(self.master, text="Password").pack()
        self.password = StringVar()
        self.paswword_box = ttk.Entry(self.master, textvariable=self.password).pack()

        self.register_btn = ttk.Button(self.master, text="Register", command=self.onclickregister).pack()

    def onclickregister(self):
        res = add_human(self.name.get(), self.family.get(), self.username.get(), self.password.get())
        self.master.destroy()
        if res:
            os.system(f"python main.py")