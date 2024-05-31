## Обновление(изменение) данных (CRUD - update)

Для обновления объекта достаточно изменить значения его атрибутов и затем вызвать у объекта `Session метод commit()` для применения изменений:


```python
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

update_user()
```

Обновление всех пользователей

```python

def update_all_user():
    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()
        for p in people:
            p.name="Иван"
        db.commit()

```