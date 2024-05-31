from sqlalchemy import *
from sqlalchemy.orm import *

## инициализация
sqlite_database = "sqlite:///product.db"
engine = create_engine(sqlite_database)


# определение моделей
class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))  # one-to-many
    company = relationship("Company", back_populates="users")  # one-to-many


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("Person", back_populates="company")


def create_db():
    Base.metadata.create_all(bind=engine)


def add_test_date_db():
    with Session(autoflush=False, bind=engine) as db:
        microsoft = Company(name="Microsoft")
        google = Company(name="Google")
        db.add_all([microsoft, google])
        db.commit()

        user1 = Person(name="Сергей", age=28)
        user2 = Person(name="Владимир", age=32)
        user1.company = microsoft
        user2.company = google

        db.add_all([user1, user2])

        db.commit()

        #
        microsoft.users = [user1]
        google.users = [user2]


        #
        user3 = Person(name="Егор", age=22)
        user4 = Person(name="Павел", age=42)
        user4.company = microsoft
        db.add_all([user3, user4])
        db.commit()

create_db()
add_test_date_db()
