from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

conn = "mssql+pyodbc://mehrzad:123@./library_proj?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conn)
Session = sessionmaker(bind=engine)
session = Session()


class Repository():
    def Add(self, obj):
        try:
            session.add(obj)
            session.commit()
            return True
        except ConnectionError as e:
            return False

    def Delete(self, obj):
        try:
            session.delete(obj)
            session.commit()
            return True
        except:
            return False

    def Read(self,obj):
        return session.query(obj).all()

    def ReadById(self, obj, fil):
        return session.query(obj).filter(obj.human_id == fil).first()

    def Update(self, obj, id):
        newObj = self.ReadById(obj, id)
        newObj = obj
        session.commit()
