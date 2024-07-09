import os
from pl.form import signup
from dal.Repository import Repository
from be.human_book import Human
from tkinter import messagebox


def add_human(name, family, username, password):
    repo = Repository()
    obj = Human(name, family, username, password)
    res = repo.Add(obj)

    if res:
        messagebox.showinfo("Welcome", "you are registered.")
        return True
    else:
        messagebox.showerror("Error", "you are not registered.")
        return False


def login(username, password):
    check = False
    repo = Repository()
    res = repo.Read(Human)
    for item in res:
        if item.human_username == username and item.human_password == password:
            messagebox.showinfo("welcome", "welcome to library.")
            return True

    if not check:
        messagebox.showerror("Error", "account not founded.")
        return False
