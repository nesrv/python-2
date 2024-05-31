## Удаление данных (CRUD - delete)

Для удаления у объекта Session применяется метод `delete()`, в который передается удаляемый объект:


```python
def del_user(id=2):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.id == id).first()
        db.delete(user)  
        db.commit()  

```

## Rollback


```python
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

```