lst_in = '''
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
'''
lst_in = lst_in.strip().split('\n')

print(lst_in)

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    #
    def insert(self, data):
        d = dict.fromkeys(self.FIELDS)
        for line in data:
            line = line.split()
            line = dict(zip(d, line))
            self.lst_data.append(line)
        # self.lst_data = [dict(zip(self.FIELDS, s.split())) for s in data]

    def select(self, a, b):
        return self.lst_data[a:b + 1]

    def __str__(self):
        return str(self.lst_data)


db = DataBase()
db.insert(lst_in)
print(db)
print(db.select(1, 1))



# или такая реализация возможна

def insert(self, data):
    self.lst_data = [dict(zip(self.FIELDS, s.split())) for s in data]
    
    
def insert(self, data):
    self.lst_data += [dict(zip(self.FIELDS, i.split())) for i in data]


def insert(self, data):
        for string in lst_in:
            s = string.split()
            d = {self.FIELDS[i]: s[i] for i in range(len(s))}
            self.lst_data.append(d)


# тесты 
res1 = db.select(0, 50)

lstgfghj8gh9jg2 = []
for d in lst_in:
    lstgfghj8gh9jg2.append(dict(zip(DataBase.FIELDS, d.split())))

assert res1 == lstgfghj8gh9jg2, "метод select вернул неверные данные"

res2 = db.select(0, 1)
assert res2 == lstgfghj8gh9jg2[0:2], "некорректно работает метод select"

print(True)