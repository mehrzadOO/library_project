from dal.Repository import Repository
from be.human_book import Human


def add_human(name, family, username, password):
    repo = Repository()
    obj = Human(name, family, username, password)
    repo.Delete(obj)