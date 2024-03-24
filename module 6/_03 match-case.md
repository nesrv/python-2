# Pattern matching

## Конструкция match

Pattern matching (сопоставление шаблонов) представляет применение конструкции match, которая позволяет сопоставить выражение с некоторым шаблоном.

И если выражение соответствует шаблону, то выполняются определенные действия.

В этом смысле конструкция match похожа на конструкцию if/else/elif, которая выполняет определенные действия в зависимости от некоторого условия.

Однако функциональность match гораздо шире - она также позволяет извлечь данные из составных типов и применить действия к различным частям объектов.

```python
match выражение:
    case шаблон_1:
        действие_1
    case шаблон_2:
        действие_2
    ................
    case шаблон_N:
        действие_N
    case _:
        действие_по_умолчанию
```

## Пример 1

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial(5)
```


## Пример использования match

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)

factorial(5)
```

## Пример использования match (case _)

```python
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")
 
print_hello("english")      
print_hello("german")       
print_hello("russian")      
```


## Пример использования match | 
### ( вертикальная черта)

```python
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "american english" | "british english" | "english":
            print("Hello")
        case _:
            print("Undefined")
 
 
print_hello("english")              
print_hello("american english")     
print_hello("spanish")                  
```


## Пример использования match. Код операции
### ( вертикальная черта)

```python
def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0
 
 
print(operation(10, 5, 1))      # 15
print(operation(10, 5, 2))      # 5
print(operation(10, 5, 3))      # 50
print(operation(10, 5, 4))      # 0 
```


## Пример использования match. 
### передача коллекций

```python
def get_color(*color):    
    match color:
        case 1, 1, 1:
            return "white"
        case 0, 0, 0:
            return "black"
        case 1, 0, 0:
            return "red"
        case 0, 1, 0:
            return "green"

        case _:
            raise ValueError("Неизвестный цвет")

res = get_color(0, 1, 0)
print(res)
```



## Пример использования match. 
### кортежи в pathern matching

```python
def print_data(user):
    match user:
        case "Олег", 37:
            print("Наш юзер")
        case "Олег", age:
            print(f"Возраст: {age}")
        case name, 22:
            print(f"Имя: {name}")
        case name, age:
            print(f"Имя: {name} возраст: {age}")


print_data(("Олег", 37))
print_data(("Олег", 28))
print_data(("Сергей", 22))
print_data(("Борис", 41))
print_data(("Олег", 33, "Google"))
```

 конструкция match сравнивает этот кортеж с рядом шаблонов.
 Первый шаблон предполагает, что кортеж user точно соответствует набору значений:

>  case "Олег", 37

Второй шаблон соответствует любому двухэлементному кортежу

>"Олег", age

и т.д.

Какая разница между __str__ и __repr__

```python
print(repr(2 / 3))
print(str(2 / 3))
```

а сейчас?

```python
import datetime
td = datetime.datetime.now()
print(td.__str__())
print(td.__repr__())
```

### Следующий пример


```python
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2D({repr(self.x)}, {repr(self.y)})"

p = Point2D(1,2) # (1, 2)
print(p)
```

Как вызвать метод __repr__?


### Далее. Использование matching в классах

```python
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f" x = {self.x}, y = {self.y}"

    def describe_point(point):
        match point:
            case Point2D(x=0, y=0):
                desc = "в начале координат"
            case Point2D(x=0, y=y):
                desc = f"на вертикальной оси, {y = }"
            case Point2D(x=x, y=0):
                desc = f"на горизонтальной оси, {x = }"
            case Point2D(x=x, y=y) if x == y:
                desc = f"по линии x = y, при этом x = y = {x}"
            case Point2D(x=x, y=y) if x == -y:
                desc = f"по линии x = -y, где x = {x} и y = {y}"
            case Point2D(x=x, y=y):
                desc = f"c координатами {point}"

        return "Точка : " + desc


p0= Point2D(0, 0)
p1 = Point2D(5, 0)
p2 = Point2D(0, 3)
p3 = Point2D(-3, -3)
p4 = Point2D(1, 2)
print(p0.describe_point())
print(p1.describe_point())
print(p2.describe_point())
print(p3.describe_point())
print(p4.describe_point())

```