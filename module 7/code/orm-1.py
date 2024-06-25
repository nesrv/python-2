from sqlalchemy import *
from sqlalchemy.orm import *


sqlite_database = "sqlite:///product.db"
engine = create_engine(sqlite_database, echo=True)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)

# Base.metadata.create_all(bind=engine)

# Base.metadata.drop_all(engine, checkfirst=True)


# создаем движок SqlAlchemy

# создаем класс сессии
# Session = sessionmaker(autoflush=False, bind=engine)

# создаем саму сессию базы данных
with Session(autoflush=False, bind=engine) as db:
    user = Person(name="Егор1", age=138)
    db.add(user)  # добавляем в бд
    db.commit()  # сохраняем изменения
    db.refresh(user)
    print(user.id)  # можно получить установленный id

# with Session(autoflush=False, bind=engine) as db:
#     tom = Person(name="Егор", age=28)
#     db.add(tom)  # добавляем в бд
#     db.commit()  # сохраняем изменения
#     print(tom.id)  # можно получить установленный id
