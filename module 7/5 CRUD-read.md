## Получение данных (CRUD - READ)

Для получения объектов из базы данных вначале у объекта Session необходимо вызывать метод `query()` - в него передается тип модели, данные которой необходимо получить:

```python
db.query(Person)
```

Но данный метод просто создает объект `Query` - некоторый запрос, который будет выполнен в будущем при непосредственном получении данных.

Далее применяя к объекту Query различные методы, мы можем получить непосредственный результат.

Например, если надо получить все объекты, применяется метод `all()`:

```python
people = db.query(Person).all()
```

Метод `all` возращает список объектов модели. 

```python
# CRUD - read data
def get_all_users_from_db():
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()
        for p in people:
            print(f"{p.id}.{p.name} ({p.age})")
```

В результате программа получит объекты `Person` и выведет из данные на консоль:

```
1.Егор (28)
2.Владимир (32)
3.Сергей (28)
4.Владимир (32)
```

Для получения одного объекта по `id` применяется метод `get()` класса `Session`. 

В качестве параметров метод получает тип модели и идентификатор объекта, который надо получить. 

Например, получим один объект `Person`, у которого `id = 1`:

```python

def get__user_by_id(id):
    with Session(autoflush=False, bind=engine) as db:
        first_person = db.get(Person, id)
        print(f"{first_person.name} - {first_person.age}") 

```

Для фильтрации у объекта Query применяется метод `filter()`, который принимает условие фильтрации.

 Например:

```python
def get_filtered_users(age):
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).filter(Person.age > age).all()
        for p in people:
            print(f"{p.id}.{p.name} ({p.age})")

```

Здесь получаем все объекты `Person`, у которых значение атрибута `age` более `age`. 

`Метод filter()` также возвращает объект `Query`, поэтому для получения собственно списка объектов, которые соответствуют фильтру, в конце по цепочке применяется метод `all()`


Для получения только одного объекта применяется метод `first()` класса `Query`:

```python
def get_user_by_filter(id):
    with Session(autoflush=False, bind=engine) as db:
        first = db.query(Person).filter(Person.id==id).first()
        print(f"{first.name} ({first.age})")

```

В данном случае получаем объект `Person`, у которого `id = 1`.

Стоит отметить, что методы `get()` и `first()` возвращают `None`, если объект не найден.

Поэтому при получении единочного объекта желательно проверять его на значение `None`.

_листинг_ 

```python
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
        first = db.query(Person).filter(Person.id==id).first()
        print(f"{first.name} ({first.age})")


get_all_users_from_db()
get_user_by_id(1)
get_filtered_users(40)
get_user_by_filter(2)

```