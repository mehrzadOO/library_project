from sqlalchemy import create_engine, Column, Integer, String, TEXT, NVARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, declarative_base, relationship

conn = "mssql+pyodbc://mehrzad:123@./library_proj?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conn)
Base = declarative_base()


class Human(Base):
    __tablename__ = "Human"
    human_id = Column(Integer, primary_key=True)
    human_name = Column(NVARCHAR)
    human_family = Column(NVARCHAR)
    human_username = Column(NVARCHAR)
    human_password = Column(NVARCHAR)
    books = relationship("Book", back_populates="human")

    def __init__(self, human_name="", human_family="", human_usename="", human_password=""):
        self.human_name = human_name
        self.human_family = human_family
        self.human_username = human_usename
        self.human_password = human_password


class Book(Base):
    __tablename__ = "Book"
    book_id = Column(Integer, primary_key=True)
    book_name = Column(NVARCHAR)
    book_genre = Column(NVARCHAR)
    book_author = Column(NVARCHAR)
    human_id = Column(Integer, ForeignKey(Human.human_id))
    human = relationship("Human", back_populates="books")

    def __init__(self, book_name="", book_author="", book_genre="", human_id=0):
        self.book_name = book_name
        self.book_author = book_author
        self.human_id = human_id
        self.book_genre = book_genre


try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("Not Connection.")