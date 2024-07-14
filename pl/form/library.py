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

        self.check_table = 0
        self.mb = ttk.Menubutton(self.master, text="Menu", padding=5)
        self.mb.place(x=910, y=0)
        self.mb.menu = Menu(self.mb, tearoff=0)
        self.mb["menu"] = self.mb.menu

        self.mb.menu.add_command(label="Add Book", command=self.OnClickAddBook)
        self.mb.menu.add_command(label="Choose Book", command=self.OnClickChooseBook)

        # frame add book.
        self.add_Book_frame = Frame(self.master, height=500, width=900)
        self.add_Book_frame.place(x=0, y=0)
        self.add_Book_frame.place_forget()

        self.title = ttk.Label(self.add_Book_frame, text="Add Book", font="bold").place(x=450, y=20)
        self.name_book_label = ttk.Label(self.add_Book_frame,text="Name").place(x=800, y=50)
        self.name_book = StringVar()
        self.name_book_box = ttk.Entry(self.add_Book_frame, textvariable=self.name_book).place(x=750, y=80)
        self.genre_book_label = ttk.Label(self.add_Book_frame,text="Genre").place(x=800, y=110)
        self.genre_book = StringVar()
        self.genre_book_box = ttk.Entry(self.add_Book_frame, textvariable=self.genre_book).place(x=750, y=140)
        self.author_book_label = ttk.Label(self.add_Book_frame,text="Author").place(x=800, y=170)
        self.author_book = StringVar()
        self.author_book_box = ttk.Entry(self.add_Book_frame, textvariable=self.author_book).place(x=750, y=200)
        self.add_book_btn = ttk.Button(self.add_Book_frame, text="ADD", command=self.OnClickAddBtn).place(x=770, y=240)



        self.choose_book_frame = Frame(self.master, height=500, width=900)
        self.choose_book_frame.place(x=0, y=0)
        self.choose_book_frame.place_forget()
        self.table_book = ttk.Treeview(self.choose_book_frame, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", height=20)
        self.table_book.column("# 1", width=100)
        self.table_book.heading("# 1", text="ID")
        self.table_book.column("# 2", width=200)
        self.table_book.heading("# 2", text="Name")
        self.table_book.column("# 3", width=200)
        self.table_book.heading("# 3", text="Author")
        self.table_book.column("# 4", width=200)
        self.table_book.heading("# 4", text="Genre")
        self.table_book.column("# 5", width=100)
        self.table_book.heading("# 5", text="Human Id")
        self.table_book.place(x=0, y=0)

    def OnClickAddBook(self):
        if self.check_table == 0:
            self.AddBookInTable()
            self.check_table += 1
        self.choose_book_frame.place_forget()
        self.add_Book_frame.place(x=0, y=0)

    def OnClickChooseBook(self):
        if self.check_table == 0:
            self.AddBookInTable()
            self.check_table += 1
        self.add_Book_frame.place_forget()
        self.choose_book_frame.place(x=0, y=0)

    def OnClickAddBtn(self):
        res = AddBook(self.name_book.get(), self.genre_book.get(), self.author_book.get())
        for item in self.table_book.get_children():
            i = (str(item))
            self.table_book.delete(i)
        self.AddBookInTable()
        self.name_book.set("")
        self.author_book.set("")
        self.genre_book.set("")

    def AddBookInTable(self):
        list_books = AddBookInTable()
        for book in list_books:
            self.table_book.insert('', 'end', text="1", values=[book.book_id, book.book_name, book.book_author, book.book_genre, book.human_id])
