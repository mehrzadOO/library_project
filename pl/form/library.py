import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
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

        self.mb = ttk.Menubutton(self.master, text="Menu", padding=5)
        self.mb.place(x=910, y=0)
        self.mb.menu = Menu(self.mb, tearoff=0)
        self.mb["menu"] = self.mb.menu

        mayoVar = IntVar()
        ketchVar = IntVar()
        self.mb.menu.add_command(label="Add Book", command=self.OnClickAddBook)
        self.mb.menu.add_command(label="Choose Book", command=self.OnClickChooseBook)

        self.add_Book_frame = Frame(self.master, bg="red", height=500, width=900)
        self.add_Book_frame.place(x=0, y=0)
        self.add_Book_frame.place_forget()

        self.choose_book_frame = Frame(self.master, bg="blue", height=500, width=900)
        self.choose_book_frame.place(x=0, y=0)
        self.choose_book_frame.place_forget()

    def OnClickAddBook(self):
        self.choose_book_frame.place_forget()
        self.add_Book_frame.place(x=0, y=0)

    def OnClickChooseBook(self):
        self.add_Book_frame.place_forget()
        self.choose_book_frame.place(x=0, y=0)