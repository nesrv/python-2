class FloatValue:

    def __init__(self, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        return instance.__dict__[self._attr]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError(
                "Присваивать можно только вещественный тип данных.")
        instance.__dict__[self._attr] = value


class Cell:

    value = FloatValue(0.0)

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.cells = [[Cell()]*m for _ in range(n)]
        self.count = 1.0

    def create_cells(self, n):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.cells[i][j] = Cell(self.count)
                self.count += 1.0


table = TableSheet(5, 3)
table.create_cells(15)



# =============================================


class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):        
        return type(string) == str and self.min_length <= len(string) <= self.max_length
        


class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__ (self,instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)       
            
class RegisterForm:
    login = StringValue(validator=ValidateString()) 
    password = StringValue(validator=ValidateString())  
    email = StringValue(validator=ValidateString())

    def __init__(self,login, password, email):
        self.login = login
        self.password = password
        self.email = email
    
    
    
    def get_fields(self):
        return [self.login,self.password, self.email]
    
    def show(self):
        print(f'<form>\nЛогин: self.login\nПароль: self.password\nEmail: self.email</form>')
