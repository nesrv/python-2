from sqlalchemy import *
from sqlalchemy.orm import *

# инициализация
sqlite_database = "sqlite:///product.db"
engine = create_engine(sqlite_database)


# определение моделей
class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    # company_id = Column(Integer, ForeignKey("companies.id")) # one-to-many
    # company = relationship("Company", back_populates="people") # one-to-many


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("User", back_populates="company")


# создание базы данных
def create_db():
    Base.metadata.create_all(bind=engine)


# crud - create user(s)
def add_user_to_db():
    with Session(autoflush=False, bind=engine) as db:
        user1 = Person(name="Сергей", age=28)
        user2 = Person(name="Владимир", age=32)
        db.add_all([user1, user2])
        db.commit()


# crud - read data)
def get_all_users_from_db():
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()
        for p in people:
            print(f"{p.id}.{p.name} ({p.age})")


def get_user_by_id(id):
    with Session(autoflush=False, bind=engine) as db:
        first_person = db.get(Person, id)
        print(f"{first_person.name} - {first_person.age}")


def get_filtered_users(age):
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).filter(Person.age > age).all()
        for p in people:
            print(f"{p.id}.{p.name} ({p.age})")


def get_user_by_filter(id):
    with Session(autoflush=False, bind=engine) as db:
        first = db.query(Person).filter(Person.id == id).first()
        print(f"{first.name} ({first.age})")


def update_user(id=1):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        if (user != None):
            print(f"{user.id}.{user.name} ({user.age})")
            user.name = "Борис"
            user.age = 22
            db.commit()
            # проверяем изменения
            check_user = db.query(Person).filter(Person.id == id).first()
            print(f"{check_user.id}.{check_user.name} ({check_user.age})")


def update_all_user():
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()
        for p in people:
            p.name = "Иван"
        db.commit()


def del_user(id=2):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        db.delete(user)
        db.commit()


def rollback_db():
    with Session(autoflush=False, bind=engine) as db:
        try:
            ...
            db.flush()
            db.commit()
        except:
            ...
            db.rollback()
        finally:
            db.close()


#
# get_all_users_from_db()
# get_user_by_id(1)
# get_filtered_users(40)
# get_user_by_filter(2)

# update_user()
# update_all_user()
# del_user()
rollback_db()
